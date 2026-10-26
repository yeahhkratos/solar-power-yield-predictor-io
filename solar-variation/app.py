import streamlit as st
import pandas as pd
import numpy as np

from weather_service import fetch_weather_forecast
from solar_model import (
    compute_physics_power,
    train_and_predict_xgboost,
    calculate_solar_summary
)
from ui_components import (
    inject_custom_styles,
    render_hero_island,
    render_weather_strip,
    render_metric_cards,
    render_power_irradiance_chart,
    render_daily_yield_bar_chart,
    render_cumulative_energy_chart,
    render_irradiance_components_chart,
    render_cloud_humidity_chart,
    render_temp_efficiency_chart,
    render_model_delta_chart,
    render_data_download_section,
    render_contributors_section,
    render_sidebar_contributors
)

# Set Streamlit Page Configuration
st.set_page_config(
    page_title="Solar Power Yield Predictor AI",
    page_icon="☀️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject Apple Liquid Glass true glassmorphic CSS, ambient mesh orbs & spring motion
inject_custom_styles()

# Preset Locations Dictionary
PRESET_LOCATIONS = {
    "Raghogarh-Vijaipur, MP 🇮🇳": (24.4442, 77.3150),
    "New Delhi, India 🇮🇳": (28.6139, 77.2090),
    "Tokyo, Japan 🇯🇵": (35.6762, 139.6503),
    "Berlin, Germany 🇩🇪": (52.5200, 13.4050),
    "Los Angeles, USA 🇺🇸": (34.0522, -118.2437),
    "Sydney, Australia 🇦🇺": (-33.8688, 151.2093),
    "Custom Location 📍": (None, None)
}

def main():
    # Sidebar: Apple Control Center Glass Panel
    st.sidebar.markdown("## ⚙️ Control Center")
    
    # 1. Solar Photovoltaic Hardware Specifications
    st.sidebar.markdown("### 📐 Photovoltaic Array Specs")
    area_m2 = st.sidebar.number_input(
        "Active Array Area (m²)",
        min_value=1.0,
        max_value=10000.0,
        value=10.0,
        step=1.0,
        help="Total surface area of your solar photovoltaic installation in square meters."
    )

    efficiency_pct = st.sidebar.slider(
        "Rated Module Efficiency (%)",
        min_value=10.0,
        max_value=25.0,
        value=18.0,
        step=0.5,
        help="Manufacturer rated solar panel efficiency under STC (Standard Test Conditions: 1000 W/m², 25°C)."
    )

    performance_ratio = st.sidebar.slider(
        "System Performance Ratio (PR)",
        min_value=0.70,
        max_value=0.95,
        value=0.75,
        step=0.01,
        help="Balance of System (BOS) factor accounting for inverter conversion, cabling resistance, soiling, and shading (default 0.75)."
    )

    # 2. Financial & Tariff Rates
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 💰 Financial & Tariff Rates")
    
    currency_choice = st.sidebar.selectbox(
        "Currency Unit",
        options=["₹ INR", "$ USD"],
        index=0
    )
    currency_symbol = "₹" if "INR" in currency_choice else "$"
    default_tariff = 7.50 if currency_symbol == "₹" else 0.15
    tariff_step = 0.50 if currency_symbol == "₹" else 0.01

    tariff_rate = st.sidebar.number_input(
        f"Electricity Tariff Rate ({currency_symbol}/kWh)",
        min_value=0.01,
        max_value=500.0,
        value=default_tariff,
        step=tariff_step,
        help="Local utility grid electricity cost per kilowatt-hour for financial yield estimation."
    )

    # 3. Geographic Coordinates & Forecast Duration
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🌐 Location & Horizon")

    selected_preset = st.sidebar.selectbox(
        "Location Presets",
        options=list(PRESET_LOCATIONS.keys()),
        index=0
    )

    preset_lat, preset_lon = PRESET_LOCATIONS[selected_preset]
    default_lat = preset_lat if preset_lat is not None else 24.4442
    default_lon = preset_lon if preset_lon is not None else 77.3150

    lat = st.sidebar.number_input(
        "Latitude (°)",
        min_value=-90.0,
        max_value=90.0,
        value=default_lat,
        format="%.4f"
    )

    lon = st.sidebar.number_input(
        "Longitude (°)",
        min_value=-180.0,
        max_value=180.0,
        value=default_lon,
        format="%.4f"
    )

    forecast_days = st.sidebar.radio(
        "Forecast Horizon",
        options=[3, 5, 7],
        index=0,
        format_func=lambda x: f"{x} Days",
        horizontal=True
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown("""
        <div style="background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.12); border-radius: 14px; padding: 0.9rem; font-size: 0.8rem; color: #98989D;">
            <div style="display: flex; align-items: center; gap: 0.4rem; color: #30D158; font-weight: 700; margin-bottom: 0.3rem;">
                <span style="width: 7px; height: 7px; background: #30D158; border-radius: 50%; display: inline-block;"></span>
                <span>Open-Meteo High-Res API</span>
            </div>
            Global satellite-calibrated NWP solar flux forecasting refreshed real-time.
        </div>
    """, unsafe_allow_html=True)

    # Project Contributors Sidebar List
    render_sidebar_contributors()

    # Main Execution Flow
    with st.spinner("🛰️ Ingesting atmospheric forecast & calibrating AI prediction matrix..."):
        try:
            df_weather = fetch_weather_forecast(lat=lat, lon=lon, forecast_days=forecast_days)
        except Exception as e:
            st.error("Failed to load weather data. Please adjust inputs or retry.")
            return

    # Calculate Physics Model Power & Derating
    df_physics = compute_physics_power(
        df=df_weather,
        area_m2=area_m2,
        efficiency_pct=efficiency_pct,
        performance_ratio=performance_ratio
    )

    # Train & Predict with XGBoost ML Model
    df_full, r2_score = train_and_predict_xgboost(
        df_forecast=df_physics,
        area_m2=area_m2,
        efficiency_pct=efficiency_pct,
        performance_ratio=performance_ratio
    )

    # Compute Summary Statistics
    summary = calculate_solar_summary(df_full, tariff_rate=tariff_rate, currency_symbol=currency_symbol)

    # 1. Apple Dynamic Island Hero Header
    render_hero_island(
        location_name=selected_preset,
        lat=lat,
        lon=lon,
        area_m2=area_m2,
        efficiency_pct=efficiency_pct
    )

    # 2. Atmospheric Telemetry Quick Strip
    render_weather_strip(df_full, energy_today_kwh=summary['energy_today_kwh'])

    # 3. Apple iOS Lockscreen / Control Center KPI Widgets
    render_metric_cards(summary)

    # 4. Interactive Dashboard Views (Apple Segmented Control Tabs)
    tab_charts, tab_radiation, tab_thermal, tab_ai, tab_data = st.tabs([
        "📈 Generation Curves (3 Graphs)",
        "☀️ Solar Radiation & Atmosphere (2 Graphs)",
        "🌡️ Thermal Derating (1 Graph)",
        "🤖 AI Model Benchmark (1 Graph)",
        "👥 Contributors & System Data"
    ])

    # View 1: Generation & Solar Radiation Curves
    with tab_charts:
        st.markdown("""
            <div class="glass-chart-container">
                <div class="chart-header-title">⚡ 1. Hourly Power Output & Solar Radiation Curve</div>
                <div class="chart-header-sub">XGBoost ML predictive output (kW) overlaid with theoretical physics baseline and shortwave radiation (W/m²).</div>
            </div>
        """, unsafe_allow_html=True)
        fig_power = render_power_irradiance_chart(df_full)
        st.plotly_chart(fig_power, use_container_width=True)

        col_g1, col_g2 = st.columns(2)
        with col_g1:
            st.markdown("""
                <div class="glass-chart-container">
                    <div class="chart-header-title">📅 2. Daily Energy Yield & Savings</div>
                    <div class="chart-header-sub">Estimated kWh output and electricity cost savings for each forecast day.</div>
                </div>
            """, unsafe_allow_html=True)
            fig_daily = render_daily_yield_bar_chart(df_full, tariff_rate=tariff_rate, currency_symbol=currency_symbol)
            st.plotly_chart(fig_daily, use_container_width=True)

        with col_g2:
            st.markdown("""
                <div class="glass-chart-container">
                    <div class="chart-header-title">📈 3. Cumulative Horizon Yield (kWh)</div>
                    <div class="chart-header-sub">Cumulative total generation trajectory across the multi-day forecast horizon.</div>
                </div>
            """, unsafe_allow_html=True)
            fig_cum = render_cumulative_energy_chart(df_full)
            st.plotly_chart(fig_cum, use_container_width=True)

    # View 2: Solar Radiation & Atmospheric Dynamics
    with tab_radiation:
        col_r1, col_r2 = st.columns(2)
        with col_r1:
            st.markdown("""
                <div class="glass-chart-container">
                    <div class="chart-header-title">☀️ 4. Direct Normal (DNI) vs Global Radiation</div>
                    <div class="chart-header-sub">Comparison of direct solar beam flux (DNI) vs total global horizontal shortwave flux (W/m²).</div>
                </div>
            """, unsafe_allow_html=True)
            fig_rad = render_irradiance_components_chart(df_full)
            st.plotly_chart(fig_rad, use_container_width=True)

        with col_r2:
            st.markdown("""
                <div class="glass-chart-container">
                    <div class="chart-header-title">☁️ 5. Cloud Cover & Humidity Attenuation</div>
                    <div class="chart-header-sub">Atmospheric weather factors influencing solar attenuation and diffuse scattering.</div>
                </div>
            """, unsafe_allow_html=True)
            fig_cloud = render_cloud_humidity_chart(df_full)
            st.plotly_chart(fig_cloud, use_container_width=True)

    # View 3: Thermal Dynamics
    with tab_thermal:
        st.markdown("""
            <div class="glass-chart-container">
                <div class="chart-header-title">🌡️ 6. Ambient Temperature & Thermal Efficiency Derating</div>
                <div class="chart-header-sub">Quantifying semiconductor cell efficiency degradation when module temperature exceeds 25°C STC standard.</div>
            </div>
        """, unsafe_allow_html=True)
        fig_temp = render_temp_efficiency_chart(df_full)
        st.plotly_chart(fig_temp, use_container_width=True)

    # View 4: AI Model Benchmark
    with tab_ai:
        st.markdown(f"""
            <div class="spec-tile" style="margin-bottom: 1.5rem;">
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.8rem; flex-wrap: wrap; gap: 0.6rem;">
                    <span style="font-weight: 800; font-size: 1.15rem; color: #FFFFFF;">🤖 7. XGBoost ML Model vs Physics Baseline</span>
                    <span class="hero-status-pill" style="margin: 0; background: rgba(48, 209, 88, 0.12); border-color: rgba(48, 209, 88, 0.35); color: #30D158;">
                        Validation Confidence R² = {r2_score:.3f}
                    </span>
                </div>
                <p style="color: #A1A1A6; line-height: 1.6; margin: 0; font-size: 0.94rem;">
                    The physical model computes linear theoretical power based strictly on <b>P = A × G × η × PR</b> with temperature derating. 
                    The <b>XGBoost gradient boosting engine</b> refines this baseline by learning complex non-linear meteorological phenomena: diffuse light scattering during heavy cloud cover, atmospheric humidity attenuation, and non-linear inverter clipping profiles.
                </p>
            </div>
        """, unsafe_allow_html=True)

        # Delta comparison calculation
        df_full["power_diff_kw"] = df_full["xgb_power_kw"] - df_full["physics_power_kw"]
        diff_val = summary['energy_today_kwh'] - summary['physics_today_kwh']
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
                <div class="spec-tile">
                    <div style="font-size: 0.77rem; font-weight: 700; text-transform: uppercase; color: #8E8E93; letter-spacing: 0.08em; margin-bottom: 0.4rem;">
                        Today's Expected Yield (XGBoost)
                    </div>
                    <div style="font-size: 2.1rem; font-weight: 900; color: #FFFFFF; display: flex; align-items: baseline; gap: 0.4rem;">
                        {summary['energy_today_kwh']} <span style="font-size: 1rem; color: #FF9F0A;">kWh</span>
                    </div>
                    <div style="font-size: 0.83rem; color: {'#30D158' if diff_val >= 0 else '#FF453A'}; margin-top: 0.4rem; font-weight: 600;">
                        {'+' if diff_val >= 0 else ''}{diff_val:.2f} kWh vs Physics Baseline
                    </div>
                </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
                <div class="spec-tile">
                    <div style="font-size: 0.77rem; font-weight: 700; text-transform: uppercase; color: #8E8E93; letter-spacing: 0.08em; margin-bottom: 0.4rem;">
                        Peak Generation Capacity
                    </div>
                    <div style="font-size: 2.1rem; font-weight: 900; color: #FFFFFF; display: flex; align-items: baseline; gap: 0.4rem;">
                        {summary['peak_kw']} <span style="font-size: 1rem; color: #0A84FF;">kW</span>
                    </div>
                    <div style="font-size: 0.83rem; color: #30D158; margin-top: 0.4rem; font-weight: 600;">
                        {r2_score*100:.1f}% Fit Confidence Score
                    </div>
                </div>
            """, unsafe_allow_html=True)

        st.markdown("""
            <div class="glass-chart-container">
                <div class="chart-header-title">🤖 Machine Learning Refinement Delta (XGBoost − Physics kW)</div>
                <div class="chart-header-sub">Quantifying exact hourly power delta where machine learning improves upon naive physics assumptions.</div>
            </div>
        """, unsafe_allow_html=True)
        fig_delta = render_model_delta_chart(df_full)
        st.plotly_chart(fig_delta, use_container_width=True)

        st.dataframe(
            df_full[["time", "shortwave_radiation", "temperature_2m", "cloud_cover", "physics_power_kw", "xgb_power_kw", "power_diff_kw"]]
            .rename(columns={
                "time": "Timestamp",
                "shortwave_radiation": "Irradiance (W/m²)",
                "temperature_2m": "Temp (°C)",
                "cloud_cover": "Cloud Cover (%)",
                "physics_power_kw": "Physics (kW)",
                "xgb_power_kw": "XGBoost (kW)",
                "power_diff_kw": "Refinement Delta (kW)"
            }),
            use_container_width=True,
            hide_index=True
        )

    # View 5: Data & System Specifications
    with tab_data:
        st.markdown("""
            <div class="glass-chart-container" style="padding-bottom: 0.5rem; margin-bottom: 1.5rem;">
                <div class="chart-header-title">⚙️ Solar Photovoltaic Hardware & Geographic Parameters</div>
                <div class="chart-header-sub">Operational coefficients, thermodynamic derating indices, and spatial coordinates configured for this forecast simulation.</div>
            </div>
        """, unsafe_allow_html=True)
        
        spec_col1, spec_col2 = st.columns(2)
        with spec_col1:
            st.markdown(f"""
                <div class="spec-tile">
                    <div style="font-size: 0.98rem; font-weight: 800; color: #FFFFFF; margin-bottom: 0.9rem;">
                        ☀️ Hardware Installation
                    </div>
                    <div style="display: flex; flex-direction: column; gap: 0.65rem; font-size: 0.88rem; color: #A1A1A6;">
                        <div style="display: flex; justify-content: space-between;">
                            <span>Active Array Surface Area:</span>
                            <span style="font-weight: 600; color: #FFFFFF;">{area_m2:.1f} m²</span>
                        </div>
                        <div style="display: flex; justify-content: space-between;">
                            <span>Rated STC Module Efficiency:</span>
                            <span style="font-weight: 600; color: #FF9F0A;">{efficiency_pct:.1f}%</span>
                        </div>
                        <div style="display: flex; justify-content: space-between;">
                            <span>System Performance Ratio (PR):</span>
                            <span style="font-weight: 600; color: #64D2FF;">{performance_ratio:.2f}</span>
                        </div>
                        <div style="display: flex; justify-content: space-between;">
                            <span>Geographic Coordinates:</span>
                            <span style="font-weight: 600; color: #FFFFFF;">{lat:.4f}°, {lon:.4f}°</span>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

        with spec_col2:
            st.markdown(f"""
                <div class="spec-tile">
                    <div style="font-size: 0.98rem; font-weight: 800; color: #FFFFFF; margin-bottom: 0.9rem;">
                        🌐 Atmospheric & Financial Baseline
                    </div>
                    <div style="display: flex; flex-direction: column; gap: 0.65rem; font-size: 0.88rem; color: #A1A1A6;">
                        <div style="display: flex; justify-content: space-between;">
                            <span>Thermal Derating Coefficient:</span>
                            <span style="font-weight: 600; color: #FF453A;">-0.40% / °C (&gt; 25°C)</span>
                        </div>
                        <div style="display: flex; justify-content: space-between;">
                            <span>Forecast Window Duration:</span>
                            <span style="font-weight: 600; color: #BF5AF2;">{forecast_days} Days ({len(df_full)} hrs)</span>
                        </div>
                        <div style="display: flex; justify-content: space-between;">
                            <span>Configured Electricity Tariff:</span>
                            <span style="font-weight: 600; color: #30D158;">{currency_symbol}{tariff_rate:.2f} / kWh</span>
                        </div>
                        <div style="display: flex; justify-content: space-between;">
                            <span>Weather API Provider:</span>
                            <span style="font-weight: 600; color: #FFFFFF;">Open-Meteo High-Res</span>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

        st.markdown("""
            <div class="glass-chart-container" style="padding-bottom: 0.5rem; margin-top: 1.5rem;">
                <div class="chart-header-title">📋 Comprehensive Hourly Forecast Telemetry</div>
                <div class="chart-header-sub">Exportable hourly timeseries dataset containing raw weather indicators and dual-model solar generation projections.</div>
            </div>
        """, unsafe_allow_html=True)
        render_data_download_section(df_full)

        # Project Contributors & Engineering Team Section
        render_contributors_section()

if __name__ == "__main__":
    main()
