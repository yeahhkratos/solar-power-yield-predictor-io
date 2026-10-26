import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def render_html(html_str: str):
    """
    Renders HTML cleanly in Streamlit without markdown parsing interference,
    eliminating accidental indented code-block rendering.
    """
    cleaned = "".join([line.strip() for line in html_str.strip().split("\n") if line.strip()])
    st.markdown(cleaned, unsafe_allow_html=True)


def inject_custom_styles():
    """
    Injects high-end Apple Liquid Glass (iOS 18 / visionOS) glassmorphism styling,
    semantic design tokens, floating chromatic ambient mesh orbs, and iPhone spring physics animations.
    """
    css_content = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap');
    
    :root {
        --bg-canvas: #070A12;
        --surface-glass-primary: linear-gradient(135deg, rgba(255, 255, 255, 0.08) 0%, rgba(255, 255, 255, 0.02) 100%);
        --surface-glass-card: linear-gradient(145deg, rgba(255, 255, 255, 0.07) 0%, rgba(255, 255, 255, 0.015) 100%);
        --border-glass: rgba(255, 255, 255, 0.14);
        --border-glass-specular: rgba(255, 255, 255, 0.32);
        
        --solar-gold: #FF9F0A;
        --solar-gold-glow: rgba(255, 159, 10, 0.4);
        --electric-azure: #0A84FF;
        --electric-azure-glow: rgba(10, 132, 255, 0.4);
        --emerald-mint: #30D158;
        --emerald-mint-glow: rgba(48, 209, 88, 0.4);
        --royal-purple: #BF5AF2;
        --royal-purple-glow: rgba(191, 90, 242, 0.4);
        --coral-red: #FF453A;
        
        --text-heading: #FFFFFF;
        --text-body: #E5E5EA;
        --text-secondary: #98989D;

        --radius-sm: 10px;
        --radius-md: 16px;
        --radius-lg: 22px;
        --radius-xl: 28px;
        --radius-pill: 9999px;

        --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
        --ease-ios: cubic-bezier(0.25, 1, 0.5, 1);
        --duration-fast: 0.22s;
        --duration-smooth: 0.38s;
    }

    html, body, [class*="css"], .stApp {
        font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", "Inter", sans-serif !important;
        letter-spacing: -0.018em;
        color: var(--text-body);
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
    }

    .stApp {
        background-color: var(--bg-canvas) !important;
        background-image: 
            radial-gradient(circle at 12% 16%, rgba(255, 159, 10, 0.15) 0%, transparent 42%),
            radial-gradient(circle at 88% 22%, rgba(10, 132, 255, 0.16) 0%, transparent 48%),
            radial-gradient(circle at 50% 82%, rgba(191, 90, 242, 0.13) 0%, transparent 46%),
            radial-gradient(circle at 82% 92%, rgba(48, 209, 88, 0.10) 0%, transparent 38%) !important;
        background-attachment: fixed !important;
        background-size: cover !important;
    }

    header[data-testid="stHeader"] {
        background: rgba(7, 10, 18, 0.45) !important;
        backdrop-filter: blur(24px) !important;
        -webkit-backdrop-filter: blur(24px) !important;
        border-bottom: 1px solid rgba(255, 255, 255, 0.08) !important;
    }

    .ambient-mesh-canvas {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        pointer-events: none;
        z-index: 0;
        overflow: hidden;
    }

    .ambient-mesh-orb {
        position: absolute;
        border-radius: 50%;
        filter: blur(100px);
        opacity: 0.62;
        mix-blend-mode: screen;
        animation: orbFloatCycle 24s ease-in-out infinite alternate;
    }

    .mesh-orb-solar {
        width: 540px;
        height: 540px;
        background: radial-gradient(circle, rgba(255, 159, 10, 0.42) 0%, rgba(255, 90, 0, 0.08) 65%, transparent 100%);
        top: -140px;
        left: 8%;
        animation-duration: 20s;
    }

    .mesh-orb-azure {
        width: 580px;
        height: 580px;
        background: radial-gradient(circle, rgba(10, 132, 255, 0.38) 0%, rgba(0, 60, 220, 0.08) 65%, transparent 100%);
        top: 35%;
        right: -120px;
        animation-duration: 26s;
        animation-delay: -6s;
    }

    .mesh-orb-violet {
        width: 500px;
        height: 500px;
        background: radial-gradient(circle, rgba(191, 90, 242, 0.32) 0%, rgba(130, 20, 220, 0.06) 65%, transparent 100%);
        bottom: -100px;
        left: 32%;
        animation-duration: 22s;
        animation-delay: -11s;
    }

    @keyframes orbFloatCycle {
        0% { transform: translate(0px, 0px) scale(1); }
        33% { transform: translate(45px, -35px) scale(1.08); }
        66% { transform: translate(-35px, 40px) scale(0.94); }
        100% { transform: translate(35px, 15px) scale(1.04); }
    }

    .block-container {
        position: relative;
        z-index: 1;
        padding-top: 1.8rem !important;
        padding-bottom: 4rem !important;
        max-width: 1380px !important;
    }

    .dynamic-island-hero {
        background: var(--surface-glass-primary);
        backdrop-filter: blur(36px) saturate(220%);
        -webkit-backdrop-filter: blur(36px) saturate(220%);
        border: 1px solid var(--border-glass);
        border-radius: var(--radius-xl);
        padding: 2.2rem 2.2rem 1.8rem 2.2rem;
        margin-bottom: 1.6rem;
        text-align: center;
        box-shadow: 0 24px 64px -12px rgba(0, 0, 0, 0.65), inset 0 1.5px 2px 0 var(--border-glass-specular);
        position: relative;
        overflow: hidden;
    }

    .hero-status-pill {
        display: inline-flex;
        align-items: center;
        gap: 0.6rem;
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid var(--border-glass);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        padding: 0.42rem 1.25rem;
        border-radius: var(--radius-pill);
        font-size: 0.78rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: #E2E8F0;
        margin-bottom: 1rem;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.25);
    }

    .pulse-live-dot {
        width: 8.5px;
        height: 8.5px;
        background-color: var(--emerald-mint);
        border-radius: 50%;
        box-shadow: 0 0 10px var(--emerald-mint);
        animation: pulseAura 2s infinite ease-in-out;
    }

    @keyframes pulseAura {
        0% { transform: scale(0.9); opacity: 0.7; box-shadow: 0 0 4px var(--emerald-mint); }
        50% { transform: scale(1.3); opacity: 1; box-shadow: 0 0 16px var(--emerald-mint); }
        100% { transform: scale(0.9); opacity: 0.7; box-shadow: 0 0 4px var(--emerald-mint); }
    }

    .hero-headline {
        font-size: 3rem;
        font-weight: 900;
        line-height: 1.15;
        background: linear-gradient(135deg, #FFFFFF 15%, #FFE082 55%, var(--solar-gold) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.65rem;
        letter-spacing: -0.035em;
    }

    .hero-subheadline {
        font-size: 1.05rem;
        color: var(--text-secondary);
        max-width: 820px;
        margin: 0 auto;
        line-height: 1.6;
        font-weight: 400;
    }

    .weather-telemetry-strip {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 1rem;
        margin-bottom: 1.8rem;
    }

    .weather-chip {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(24px) saturate(190%);
        -webkit-backdrop-filter: blur(24px) saturate(190%);
        border: 1px solid var(--border-glass);
        border-radius: var(--radius-md);
        padding: 0.95rem 1.15rem;
        display: flex;
        align-items: center;
        gap: 0.9rem;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3), inset 0 1px 1px rgba(255, 255, 255, 0.18);
        transition: transform var(--duration-fast) var(--ease-spring), border-color var(--duration-fast) var(--ease-ios);
    }

    .weather-chip:hover {
        transform: translateY(-3px) scale(1.02);
        border-color: rgba(255, 255, 255, 0.3);
    }

    .weather-chip-icon {
        font-size: 1.35rem;
        width: 38px;
        height: 38px;
        border-radius: 10px;
        background: rgba(255, 255, 255, 0.08);
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .weather-chip-content {
        display: flex;
        flex-direction: column;
    }

    .weather-chip-label {
        font-size: 0.72rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: var(--text-secondary);
    }

    .weather-chip-val {
        font-size: 1.15rem;
        font-weight: 800;
        color: var(--text-heading);
        letter-spacing: -0.02em;
    }

    .metric-card-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1.25rem;
        margin-bottom: 2.2rem;
    }

    .metric-card {
        background: var(--surface-glass-card);
        backdrop-filter: blur(34px) saturate(215%);
        -webkit-backdrop-filter: blur(34px) saturate(215%);
        border: 1px solid var(--border-glass);
        border-radius: var(--radius-xl);
        padding: 1.45rem 1.55rem;
        box-shadow: 0 18px 45px -10px rgba(0, 0, 0, 0.5), inset 0 1.2px 1.8px 0 var(--border-glass-specular);
        position: relative;
        overflow: hidden;
        transition: transform var(--duration-smooth) var(--ease-spring), box-shadow var(--duration-smooth) var(--ease-ios);
        cursor: default;
    }

    .metric-card:hover {
        transform: translateY(-6px) scale(1.02);
        box-shadow: 0 28px 60px -10px rgba(0, 0, 0, 0.7), 0 0 32px 0 var(--accent-glow, rgba(255, 159, 10, 0.25));
        border-color: var(--accent-border, rgba(255, 159, 10, 0.5));
    }

    .metric-card:active {
        transform: scale(0.972);
    }

    .metric-card::after {
        content: '';
        position: absolute;
        top: 0;
        left: -160%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.14), transparent);
        transform: skewX(-24deg);
        transition: left 0.85s var(--ease-ios);
        pointer-events: none;
    }

    .metric-card:hover::after {
        left: 160%;
    }

    .metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 3.5px;
        background: linear-gradient(90deg, #FFB800 0%, #FF8A00 100%);
    }

    .metric-card.gold-theme {
        --accent-glow: var(--solar-gold-glow);
        --accent-border: rgba(255, 159, 10, 0.55);
    }
    .metric-card.gold-theme::before {
        background: linear-gradient(90deg, #FFD54F 0%, var(--solar-gold) 100%);
    }

    .metric-card.blue-theme {
        --accent-glow: var(--electric-azure-glow);
        --accent-border: rgba(10, 132, 255, 0.55);
    }
    .metric-card.blue-theme::before {
        background: linear-gradient(90deg, #64D2FF 0%, var(--electric-azure) 100%);
    }

    .metric-card.green-theme {
        --accent-glow: var(--emerald-mint-glow);
        --accent-border: rgba(48, 209, 88, 0.55);
    }
    .metric-card.green-theme::before {
        background: linear-gradient(90deg, var(--emerald-mint) 0%, #00B0FF 100%);
    }

    .metric-card.purple-theme {
        --accent-glow: var(--royal-purple-glow);
        --accent-border: rgba(191, 90, 242, 0.55);
    }
    .metric-card.purple-theme::before {
        background: linear-gradient(90deg, var(--royal-purple) 0%, #FF375F 100%);
    }

    .metric-header-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 0.9rem;
    }

    .metric-glyph-icon {
        width: 40px;
        height: 40px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.25rem;
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid var(--border-glass);
        box-shadow: 0 4px 14px rgba(0, 0, 0, 0.25);
    }

    .metric-title {
        font-size: 0.77rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.09em;
        color: var(--text-secondary);
    }

    .metric-value {
        font-size: 2.35rem;
        font-weight: 900;
        color: var(--text-heading);
        line-height: 1.05;
        display: flex;
        align-items: baseline;
        gap: 0.35rem;
        letter-spacing: -0.03em;
        margin-bottom: 0.55rem;
    }

    .metric-unit-chip {
        font-size: 0.88rem;
        font-weight: 700;
        padding: 0.2rem 0.65rem;
        border-radius: var(--radius-pill);
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid var(--border-glass);
    }

    .metric-sub-pill {
        font-size: 0.79rem;
        color: var(--text-secondary);
        display: flex;
        align-items: center;
        gap: 0.35rem;
        margin-top: 0.35rem;
    }

    [data-testid="stSidebar"] {
        background: rgba(10, 15, 28, 0.68) !important;
        backdrop-filter: blur(40px) saturate(220%) !important;
        -webkit-backdrop-filter: blur(40px) saturate(220%) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.12) !important;
    }

    div[data-baseweb="input"],
    div[data-baseweb="select"] > div,
    .stNumberInput input,
    .stTextInput input {
        background: rgba(255, 255, 255, 0.06) !important;
        border: 1px solid var(--border-glass) !important;
        border-radius: var(--radius-md) !important;
        color: #FFFFFF !important;
    }

    div[data-baseweb="input"]:focus-within,
    div[data-baseweb="select"]:focus-within > div,
    .stNumberInput input:focus {
        border-color: rgba(255, 159, 10, 0.7) !important;
        box-shadow: 0 0 0 3.5px rgba(255, 159, 10, 0.25) !important;
    }

    .stTabs [data-baseweb="tab-list"] {
        background: rgba(255, 255, 255, 0.06) !important;
        backdrop-filter: blur(32px) saturate(205%) !important;
        -webkit-backdrop-filter: blur(32px) saturate(205%) !important;
        border: 1px solid var(--border-glass) !important;
        border-radius: var(--radius-pill) !important;
        padding: 6px !important;
        gap: 6px !important;
        margin-bottom: 2rem !important;
    }

    .stTabs [data-baseweb="tab"] {
        border-radius: var(--radius-pill) !important;
        font-weight: 600 !important;
        font-size: 0.93rem !important;
        padding: 9px 22px !important;
        color: var(--text-secondary) !important;
        border: 1px solid transparent !important;
        background: transparent !important;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.2) 0%, rgba(255, 255, 255, 0.08) 100%) !important;
        color: #FFFFFF !important;
        border: 1px solid var(--border-glass-specular) !important;
    }

    .glass-chart-container {
        background: var(--surface-glass-card);
        backdrop-filter: blur(34px) saturate(205%);
        -webkit-backdrop-filter: blur(34px) saturate(205%);
        border: 1px solid var(--border-glass);
        border-radius: var(--radius-xl);
        padding: 1.6rem 1.4rem 1.1rem 1.4rem;
        margin-bottom: 2rem;
        box-shadow: 0 22px 52px -12px rgba(0, 0, 0, 0.55), inset 0 1px 1.5px var(--border-glass-specular);
    }

    .chart-header-title {
        font-size: 1.2rem;
        font-weight: 800;
        color: var(--text-heading);
        letter-spacing: -0.02em;
        margin-bottom: 0.25rem;
    }

    .chart-header-sub {
        font-size: 0.85rem;
        color: var(--text-secondary);
        margin-bottom: 0.95rem;
    }

    button[kind="primary"],
    button[kind="secondary"],
    div.stDownloadButton button {
        background: linear-gradient(135deg, rgba(255, 159, 10, 0.3) 0%, rgba(255, 100, 0, 0.18) 100%) !important;
        border: 1px solid rgba(255, 159, 10, 0.48) !important;
        border-radius: var(--radius-pill) !important;
        color: #FFFFFF !important;
        font-weight: 700 !important;
        padding: 0.65rem 1.5rem !important;
    }

    .spec-tile {
        background: var(--surface-glass-card);
        backdrop-filter: blur(28px);
        border: 1px solid var(--border-glass);
        border-radius: var(--radius-lg);
        padding: 1.4rem;
        margin-bottom: 1.1rem;
    }
    </style>

    <div class="ambient-mesh-canvas">
        <div class="ambient-mesh-orb mesh-orb-solar"></div>
        <div class="ambient-mesh-orb mesh-orb-azure"></div>
        <div class="ambient-mesh-orb mesh-orb-violet"></div>
    </div>
    """
    render_html(css_content)


def render_hero_island(location_name: str, lat: float, lon: float, area_m2: float, efficiency_pct: float):
    """
    Renders the Apple Dynamic Island Hero Header cleanly.
    """
    html = f"""
    <div class="dynamic-island-hero">
        <div class="hero-status-pill">
            <span class="pulse-live-dot"></span>
            <span>Live Open-Meteo Telemetry • AI Hybrid Model Active</span>
        </div>
        <h1 class="hero-headline">☀️ Solar Yield Predictor AI</h1>
        <p class="hero-subheadline">
            Hyper-local solar photovoltaic irradiance forecasting & hourly yield estimation combining thermodynamic semiconductor physics with synthetic XGBoost gradient boosting.
        </p>
        <div style="display: flex; justify-content: center; gap: 0.75rem; margin-top: 1.2rem; flex-wrap: wrap;">
            <span class="hero-status-pill" style="margin: 0; background: rgba(255, 255, 255, 0.06); font-size: 0.75rem;">
                📍 {location_name} ({lat:.2f}°, {lon:.2f}°)
            </span>
            <span class="hero-status-pill" style="margin: 0; background: rgba(255, 159, 10, 0.12); border-color: rgba(255, 159, 10, 0.3); color: #FF9F0A; font-size: 0.75rem;">
                📐 Array Surface: {area_m2:.1f} m²
            </span>
            <span class="hero-status-pill" style="margin: 0; background: rgba(10, 132, 255, 0.12); border-color: rgba(10, 132, 255, 0.3); color: #64D2FF; font-size: 0.75rem;">
                ⚡ Module Efficiency: {efficiency_pct:.1f}% STC
            </span>
        </div>
    </div>
    """
    render_html(html)


def render_weather_strip(df: pd.DataFrame, energy_today_kwh: float):
    """
    Renders an iOS-style quick atmospheric telemetry strip cleanly.
    """
    max_temp = df["temperature_2m"].max()
    min_temp = df["temperature_2m"].min()
    peak_rad = df["shortwave_radiation"].max()
    avg_cloud = df["cloud_cover"].mean()
    co2_offset_kg = round(energy_today_kwh * 0.72, 1)

    html = f"""
    <div class="weather-telemetry-strip">
        <div class="weather-chip">
            <div class="weather-chip-icon" style="color: #FF6961;">🌡️</div>
            <div class="weather-chip-content">
                <span class="weather-chip-label">Ambient Range</span>
                <span class="weather-chip-val">{min_temp:.1f}° – {max_temp:.1f}°C</span>
            </div>
        </div>
        <div class="weather-chip">
            <div class="weather-chip-icon" style="color: #FF9F0A;">☀️</div>
            <div class="weather-chip-content">
                <span class="weather-chip-label">Peak Radiation</span>
                <span class="weather-chip-val">{peak_rad:.0f} W/m²</span>
            </div>
        </div>
        <div class="weather-chip">
            <div class="weather-chip-icon" style="color: #64D2FF;">☁️</div>
            <div class="weather-chip-content">
                <span class="weather-chip-label">Avg Cloud Cover</span>
                <span class="weather-chip-val">{avg_cloud:.1f}%</span>
            </div>
        </div>
        <div class="weather-chip">
            <div class="weather-chip-icon" style="color: #30D158;">🌿</div>
            <div class="weather-chip-content">
                <span class="weather-chip-label">CO₂ Offset (Today)</span>
                <span class="weather-chip-val">{co2_offset_kg} kg</span>
            </div>
        </div>
    </div>
    """
    render_html(html)


def render_metric_cards(summary: dict):
    """
    Renders high-fidelity Apple-style Glassmorphic Widget Cards.
    """
    currency = summary.get('currency_symbol', '₹')
    html = f"""
    <div class="metric-card-container">
        <div class="metric-card gold-theme">
            <div class="metric-header-row">
                <span class="metric-title">Expected Yield</span>
                <div class="metric-glyph-icon" style="color: #FFB800;">⚡</div>
            </div>
            <div class="metric-value">
                {summary['energy_today_kwh']} 
                <span class="metric-unit-chip" style="color: #FFB800;">kWh</span>
            </div>
            <div class="metric-sub-pill">
                <span>🎯</span> Baseline: {summary['physics_today_kwh']} kWh
            </div>
        </div>
        <div class="metric-card blue-theme">
            <div class="metric-header-row">
                <span class="metric-title">Peak Output</span>
                <div class="metric-glyph-icon" style="color: #0A84FF;">🔥</div>
            </div>
            <div class="metric-value">
                {summary['peak_kw']} 
                <span class="metric-unit-chip" style="color: #64D2FF;">kW</span>
            </div>
            <div class="metric-sub-pill">
                <span>⏱️</span> Instantaneous peak generation
            </div>
        </div>
        <div class="metric-card green-theme">
            <div class="metric-header-row">
                <span class="metric-title">Daily Savings</span>
                <div class="metric-glyph-icon" style="color: #30D158;">💰</div>
            </div>
            <div class="metric-value">
                {currency}{summary['cost_savings']}
            </div>
            <div class="metric-sub-pill">
                <span>📊</span> Calculated at active tariff
            </div>
        </div>
        <div class="metric-card purple-theme">
            <div class="metric-header-row">
                <span class="metric-title">Horizon Total</span>
                <div class="metric-glyph-icon" style="color: #BF5AF2;">📅</div>
            </div>
            <div class="metric-value">
                {summary['total_forecast_kwh']} 
                <span class="metric-unit-chip" style="color: #BF5AF2;">kWh</span>
            </div>
            <div class="metric-sub-pill">
                <span>📈</span> Multi-day forecast span
            </div>
        </div>
    </div>
    """
    render_html(html)


def get_base_plotly_layout(height: int = 440) -> dict:
    """Returns standard high-fidelity dark glass Plotly layout options."""
    return dict(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(10, 15, 28, 0.45)",
        font=dict(family="-apple-system, BlinkMacSystemFont, SF Pro Display, Inter, sans-serif", color="#E2E8F0"),
        height=height,
        margin=dict(l=20, r=20, t=30, b=30),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.04,
            xanchor="right",
            x=1,
            bgcolor="rgba(255, 255, 255, 0.05)",
            bordercolor="rgba(255, 255, 255, 0.12)",
            borderwidth=1,
            font=dict(size=11, color="#A1A1A6")
        ),
        hovermode="x unified",
        hoverlabel=dict(
            bgcolor="rgba(15, 23, 42, 0.92)",
            bordercolor="rgba(255, 255, 255, 0.2)",
            font=dict(family="-apple-system, BlinkMacSystemFont, SF Pro Display, Inter, sans-serif", color="#FFFFFF", size=12)
        )
    )


# --- CHART 1: Hourly Power & Irradiance ---
def render_power_irradiance_chart(df: pd.DataFrame) -> go.Figure:
    fig = make_subplots(specs=[[{"secondary_y": True}]], subplot_titles=("",))

    fig.add_trace(
        go.Scatter(
            x=df["time"],
            y=df["xgb_power_kw"],
            name="XGBoost Power (kW)",
            mode="lines",
            line=dict(color="#FF9F0A", width=3.4),
            fill="tozeroy",
            fillcolor="rgba(255, 159, 10, 0.16)",
            hovertemplate="<b>%{x|%a, %b %d • %H:%M}</b><br>⚡ XGBoost: <b>%{y:.2f} kW</b><extra></extra>"
        ),
        secondary_y=False
    )
    fig.add_trace(
        go.Scatter(
            x=df["time"],
            y=df["physics_power_kw"],
            name="Physics Baseline (kW)",
            mode="lines",
            line=dict(color="#FF453A", width=2, dash="dash"),
            hovertemplate="<b>%{x|%a, %b %d • %H:%M}</b><br>📐 Physics: <b>%{y:.2f} kW</b><extra></extra>"
        ),
        secondary_y=False
    )
    fig.add_trace(
        go.Scatter(
            x=df["time"],
            y=df["shortwave_radiation"],
            name="Solar Irradiance (W/m²)",
            mode="lines",
            line=dict(color="#30D158", width=2, dash="dot"),
            hovertemplate="<b>%{x|%a, %b %d • %H:%M}</b><br>☀️ Irradiance: <b>%{y:.1f} W/m²</b><extra></extra>"
        ),
        secondary_y=True
    )

    fig.update_layout(get_base_plotly_layout(460))
    fig.update_xaxes(showgrid=True, gridcolor="rgba(255, 255, 255, 0.05)", tickfont=dict(color="#8E8E93", size=11))
    fig.update_yaxes(title_text="<b>Power Output (kW)</b>", secondary_y=False, showgrid=True, gridcolor="rgba(255, 255, 255, 0.05)", color="#FF9F0A")
    fig.update_yaxes(title_text="<b>Irradiance (W/m²)</b>", secondary_y=True, showgrid=False, color="#30D158")
    return fig


# --- CHART 2: Daily Yield & Monetary Savings Bar Chart ---
def render_daily_yield_bar_chart(df: pd.DataFrame, tariff_rate: float, currency_symbol: str) -> go.Figure:
    df_copy = df.copy()
    df_copy["date_str"] = df_copy["time"].dt.strftime("%a, %b %d")
    daily = df_copy.groupby("date_str", sort=False).agg({
        "xgb_power_kw": "sum",
        "physics_power_kw": "sum"
    }).reset_index()

    daily["savings"] = daily["xgb_power_kw"] * tariff_rate

    fig = make_subplots(specs=[[{"secondary_y": True}]], subplot_titles=("",))
    fig.add_trace(
        go.Bar(
            x=daily["date_str"],
            y=daily["xgb_power_kw"],
            name="Daily Yield (kWh)",
            marker=dict(
                color="rgba(255, 159, 10, 0.75)",
                line=dict(color="#FF9F0A", width=1.5)
            ),
            hovertemplate="<b>%{x}</b><br>⚡ Energy: <b>%{y:.2f} kWh</b><extra></extra>"
        ),
        secondary_y=False
    )
    fig.add_trace(
        go.Scatter(
            x=daily["date_str"],
            y=daily["savings"],
            name=f"Est. Savings ({currency_symbol})",
            mode="lines+markers",
            line=dict(color="#30D158", width=3),
            marker=dict(size=8, color="#30D158"),
            hovertemplate=f"<b>%{{x}}</b><br>💰 Savings: <b>{currency_symbol}%{{y:.2f}}</b><extra></extra>"
        ),
        secondary_y=True
    )

    fig.update_layout(get_base_plotly_layout(400))
    fig.update_xaxes(showgrid=False, tickfont=dict(color="#8E8E93", size=11))
    fig.update_yaxes(title_text="<b>Daily Yield (kWh)</b>", secondary_y=False, showgrid=True, gridcolor="rgba(255, 255, 255, 0.05)", color="#FF9F0A")
    fig.update_yaxes(title_text=f"<b>Daily Savings ({currency_symbol})</b>", secondary_y=True, showgrid=False, color="#30D158")
    return fig


# --- CHART 3: Direct Beam (DNI) vs Global Shortwave Radiation ---
def render_irradiance_components_chart(df: pd.DataFrame) -> go.Figure:
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df["time"],
            y=df["shortwave_radiation"],
            name="Global Shortwave Radiation (W/m²)",
            mode="lines",
            line=dict(color="#FF9F0A", width=2.5),
            fill="tozeroy",
            fillcolor="rgba(255, 159, 10, 0.12)",
            hovertemplate="<b>%{x|%a, %b %d • %H:%M}</b><br>☀️ Global: <b>%{y:.1f} W/m²</b><extra></extra>"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df["time"],
            y=df["direct_normal_irradiance"],
            name="Direct Normal Irradiance DNI (W/m²)",
            mode="lines",
            line=dict(color="#FFE082", width=2.5),
            hovertemplate="<b>%{x|%a, %b %d • %H:%M}</b><br>🎯 DNI: <b>%{y:.1f} W/m²</b><extra></extra>"
        )
    )

    layout = get_base_plotly_layout(420)
    fig.update_layout(layout)
    fig.update_xaxes(showgrid=True, gridcolor="rgba(255, 255, 255, 0.05)", tickfont=dict(color="#8E8E93", size=11))
    fig.update_yaxes(title_text="<b>Solar Irradiance (W/m²)</b>", showgrid=True, gridcolor="rgba(255, 255, 255, 0.05)", color="#FF9F0A")
    return fig


# --- CHART 4: Ambient Temperature vs Solar Efficiency Derating ---
def render_temp_efficiency_chart(df: pd.DataFrame) -> go.Figure:
    fig = make_subplots(specs=[[{"secondary_y": True}]], subplot_titles=("",))

    fig.add_trace(
        go.Scatter(
            x=df["time"],
            y=df["temperature_2m"],
            name="Ambient Temp (°C)",
            mode="lines+markers",
            line=dict(color="#FF6961", width=2.6),
            marker=dict(size=4.5, color="#FF6961"),
            hovertemplate="<b>%{x|%a, %b %d • %H:%M}</b><br>🌡️ Temp: <b>%{y:.1f} °C</b><extra></extra>"
        ),
        secondary_y=False
    )

    fig.add_trace(
        go.Scatter(
            x=df["time"],
            y=[25.0] * len(df),
            name="STC Standard (25°C)",
            mode="lines",
            line=dict(color="rgba(255, 255, 255, 0.35)", width=1.5, dash="dash"),
            hoverinfo="none"
        ),
        secondary_y=False
    )

    fig.add_trace(
        go.Bar(
            x=df["time"],
            y=df["efficiency_loss_pct"],
            name="Efficiency Derating (%)",
            marker=dict(color="rgba(255, 69, 58, 0.65)", line=dict(color="rgba(255, 69, 58, 0.9)", width=1)),
            hovertemplate="<b>%{x|%a, %b %d • %H:%M}</b><br>📉 Derating: <b>-%{y:.2f}%</b><extra></extra>"
        ),
        secondary_y=True
    )

    fig.update_layout(get_base_plotly_layout(410))
    fig.update_xaxes(showgrid=True, gridcolor="rgba(255, 255, 255, 0.05)", tickfont=dict(color="#8E8E93", size=11))
    fig.update_yaxes(title_text="<b>Temperature (°C)</b>", secondary_y=False, showgrid=True, gridcolor="rgba(255, 255, 255, 0.05)", color="#FF6961")
    fig.update_yaxes(title_text="<b>Efficiency Loss (%)</b>", secondary_y=True, showgrid=False, color="#FF453A")
    return fig


# --- CHART 5: Cloud Cover & Relative Humidity Attenuation ---
def render_cloud_humidity_chart(df: pd.DataFrame) -> go.Figure:
    fig = make_subplots(specs=[[{"secondary_y": True}]], subplot_titles=("",))

    fig.add_trace(
        go.Scatter(
            x=df["time"],
            y=df["cloud_cover"],
            name="Cloud Cover (%)",
            mode="lines",
            line=dict(color="#64D2FF", width=2.4),
            fill="tozeroy",
            fillcolor="rgba(100, 210, 255, 0.15)",
            hovertemplate="<b>%{x|%a, %b %d • %H:%M}</b><br>☁️ Cloud Cover: <b>%{y:.1f}%</b><extra></extra>"
        ),
        secondary_y=False
    )

    fig.add_trace(
        go.Scatter(
            x=df["time"],
            y=df["relative_humidity_2m"],
            name="Relative Humidity (%)",
            mode="lines",
            line=dict(color="#BF5AF2", width=2),
            hovertemplate="<b>%{x|%a, %b %d • %H:%M}</b><br>💧 Humidity: <b>%{y:.1f}%</b><extra></extra>"
        ),
        secondary_y=True
    )

    fig.update_layout(get_base_plotly_layout(410))
    fig.update_xaxes(showgrid=True, gridcolor="rgba(255, 255, 255, 0.05)", tickfont=dict(color="#8E8E93", size=11))
    fig.update_yaxes(title_text="<b>Cloud Cover (%)</b>", secondary_y=False, showgrid=True, gridcolor="rgba(255, 255, 255, 0.05)", color="#64D2FF")
    fig.update_yaxes(title_text="<b>Humidity (%)</b>", secondary_y=True, showgrid=False, color="#BF5AF2")
    return fig


# --- CHART 6: XGBoost vs Physics Refinement Delta Curve ---
def render_model_delta_chart(df: pd.DataFrame) -> go.Figure:
    fig = go.Figure()
    df_copy = df.copy()
    diff = df_copy["xgb_power_kw"] - df_copy["physics_power_kw"]

    fig.add_trace(
        go.Scatter(
            x=df_copy["time"],
            y=diff,
            name="Refinement Delta (kW)",
            mode="lines",
            line=dict(color="#30D158", width=2.5),
            fill="tozeroy",
            fillcolor="rgba(48, 209, 88, 0.15)",
            hovertemplate="<b>%{x|%a, %b %d • %H:%M}</b><br>🤖 Delta: <b>%{y:+.2f} kW</b><extra></extra>"
        )
    )

    fig.add_hline(y=0, line_dash="dash", line_color="rgba(255, 255, 255, 0.35)", annotation_text="Baseline Reference")

    fig.update_layout(get_base_plotly_layout(410))
    fig.update_xaxes(showgrid=True, gridcolor="rgba(255, 255, 255, 0.05)", tickfont=dict(color="#8E8E93", size=11))
    fig.update_yaxes(title_text="<b>Δ Power Difference (kW)</b>", showgrid=True, gridcolor="rgba(255, 255, 255, 0.05)", color="#30D158")
    return fig


# --- CHART 7: Cumulative Energy Production Trajectory ---
def render_cumulative_energy_chart(df: pd.DataFrame) -> go.Figure:
    fig = go.Figure()
    cum_xgb = df["xgb_power_kw"].cumsum()
    cum_physics = df["physics_power_kw"].cumsum()

    fig.add_trace(
        go.Scatter(
            x=df["time"],
            y=cum_xgb,
            name="XGBoost Cumulative Yield (kWh)",
            mode="lines",
            line=dict(color="#FF9F0A", width=3.2),
            fill="tozeroy",
            fillcolor="rgba(255, 159, 10, 0.12)",
            hovertemplate="<b>%{x|%a, %b %d • %H:%M}</b><br>⚡ XGB Cum: <b>%{y:.2f} kWh</b><extra></extra>"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df["time"],
            y=cum_physics,
            name="Physics Cumulative Baseline (kWh)",
            mode="lines",
            line=dict(color="#FF453A", width=2, dash="dash"),
            hovertemplate="<b>%{x|%a, %b %d • %H:%M}</b><br>📐 Physics Cum: <b>%{y:.2f} kWh</b><extra></extra>"
        )
    )

    fig.update_layout(get_base_plotly_layout(420))
    fig.update_xaxes(showgrid=True, gridcolor="rgba(255, 255, 255, 0.05)", tickfont=dict(color="#8E8E93", size=11))
    fig.update_yaxes(title_text="<b>Cumulative Yield (kWh)</b>", showgrid=True, gridcolor="rgba(255, 255, 255, 0.05)", color="#FF9F0A")
    return fig


def render_data_download_section(df: pd.DataFrame):
    """
    Renders downloadable CSV summary with an iOS-style glass action header and styled dataframe.
    """
    export_df = df[[
        "time",
        "shortwave_radiation",
        "direct_normal_irradiance",
        "temperature_2m",
        "cloud_cover",
        "relative_humidity_2m",
        "physics_power_kw",
        "xgb_power_kw",
        "efficiency_loss_pct"
    ]].copy()

    export_df.columns = [
        "Timestamp",
        "Shortwave Irradiance (W/m2)",
        "Direct Normal Irradiance (W/m2)",
        "Temperature (°C)",
        "Cloud Cover (%)",
        "Relative Humidity (%)",
        "Physics Power (kW)",
        "XGBoost Predicted (kW)",
        "Thermal Loss (%)"
    ]

    csv_bytes = export_df.to_csv(index=False).encode('utf-8')

    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f"Dataset preview: **{len(export_df)} hourly telemetric records** processed.")
    with col2:
        st.download_button(
            label="📥 Export Dataset (CSV)",
            data=csv_bytes,
            file_name="solar_power_forecast_summary.csv",
            mime="text/csv",
            use_container_width=True
        )

    st.dataframe(
        export_df,
        use_container_width=True,
        height=390,
        hide_index=True
    )


def render_contributors_section():
    """
    Renders an Apple-grade glassmorphic project contributors / engineering team section.
    """
    contributors = [
        {
            "name": "Akshat Jain",
            "role": "Project Leader",
            "badge": "Leader",
            "color": "#FF9F0A",
            "glow": "rgba(255, 159, 10, 0.4)",
            "icon": "👑",
            "initials": "AJ"
        },
        {
            "name": "Gaurik Mishra",
            "role": "Project Co-Leader",
            "badge": "Co-Leader",
            "color": "#0A84FF",
            "glow": "rgba(10, 132, 255, 0.4)",
            "icon": "🌟",
            "initials": "GM"
        },
        {
            "name": "Raj Sahu",
            "role": "Project Coordinator",
            "badge": "Coordinator",
            "color": "#30D158",
            "glow": "rgba(48, 209, 88, 0.4)",
            "icon": "🎯",
            "initials": "RS"
        },
        {
            "name": "Pratiksha Agarwal",
            "role": "Project Coordinator",
            "badge": "Coordinator",
            "color": "#BF5AF2",
            "glow": "rgba(191, 90, 242, 0.4)",
            "icon": "✨",
            "initials": "PA"
        },
        {
            "name": "Mudit Bairagi",
            "role": "Project Coordinator",
            "badge": "Coordinator",
            "color": "#64D2FF",
            "glow": "rgba(100, 210, 255, 0.4)",
            "icon": "⚙️",
            "initials": "MB"
        }
    ]

    cards_html = ""
    for c in contributors:
        cards_html += f"""
        <div style="background: linear-gradient(145deg, rgba(255, 255, 255, 0.07) 0%, rgba(255, 255, 255, 0.02) 100%); backdrop-filter: blur(28px); border: 1px solid rgba(255, 255, 255, 0.14); border-radius: 20px; padding: 1.35rem 1.15rem; text-align: center; box-shadow: 0 14px 36px rgba(0,0,0,0.4), inset 0 1px 1.5px rgba(255,255,255,0.22); transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1); cursor: default;">
            <div style="width: 52px; height: 52px; border-radius: 50%; margin: 0 auto 0.75rem auto; display: flex; align-items: center; justify-content: center; font-weight: 900; font-size: 1.15rem; color: {c['color']}; background: radial-gradient(circle, rgba(255, 255, 255, 0.12) 0%, rgba(255, 255, 255, 0.03) 100%); border: 1.5px solid {c['color']}; box-shadow: 0 0 18px {c['glow']};">
                {c['initials']}
            </div>
            <div style="font-size: 1.05rem; font-weight: 800; color: #FFFFFF; letter-spacing: -0.015em;">
                {c['name']}
            </div>
            <div style="margin-top: 0.5rem;">
                <span style="display: inline-flex; align-items: center; gap: 0.3rem; padding: 0.22rem 0.75rem; border-radius: 9999px; font-size: 0.76rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; background: {c['glow'].replace('0.4', '0.14')}; border: 1px solid {c['color']}; color: {c['color']};">
                    <span>{c['icon']}</span> {c['badge']}
                </span>
            </div>
            <div style="font-size: 0.78rem; color: #8E8E93; margin-top: 0.45rem;">
                {c['role']}
            </div>
        </div>
        """

    html = f"""
    <div class="glass-chart-container" style="margin-top: 1.5rem; margin-bottom: 2rem;">
        <div class="chart-header-title">👥 Project Contributors & Engineering Team</div>
        <div class="chart-header-sub">Core researchers and developers behind the Solar Yield Predictor AI project.</div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 1.1rem; margin-top: 1.1rem;">
            {cards_html}
        </div>
    </div>
    """
    render_html(html)


def render_sidebar_contributors():
    """
    Renders a compact, sleek glassmorphic team list inside the Streamlit sidebar.
    """
    html = """
    <div style="background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.12); border-radius: 16px; padding: 1rem; margin-top: 1.2rem; box-shadow: 0 8px 24px rgba(0,0,0,0.3);">
        <div style="font-weight: 800; font-size: 0.92rem; color: #FFFFFF; display: flex; align-items: center; gap: 0.45rem; margin-bottom: 0.75rem;">
            <span>👥 Project Contributors</span>
        </div>
        <div style="display: flex; flex-direction: column; gap: 0.55rem; font-size: 0.82rem;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="font-weight: 700; color: #FFFFFF;">1. Akshat Jain</span>
                <span style="background: rgba(255, 159, 10, 0.18); border: 1px solid rgba(255, 159, 10, 0.45); color: #FF9F0A; padding: 0.15rem 0.55rem; border-radius: 9999px; font-size: 0.72rem; font-weight: 700;">Leader 👑</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="font-weight: 700; color: #FFFFFF;">2. Gaurik Mishra</span>
                <span style="background: rgba(10, 132, 255, 0.18); border: 1px solid rgba(10, 132, 255, 0.45); color: #64D2FF; padding: 0.15rem 0.55rem; border-radius: 9999px; font-size: 0.72rem; font-weight: 700;">Co-Leader 🌟</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="font-weight: 600; color: #E2E8F0;">3. Raj Sahu</span>
                <span style="background: rgba(48, 209, 88, 0.15); border: 1px solid rgba(48, 209, 88, 0.35); color: #30D158; padding: 0.15rem 0.55rem; border-radius: 9999px; font-size: 0.72rem; font-weight: 700;">Coordinator 🎯</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="font-weight: 600; color: #E2E8F0;">4. Pratiksha Agarwal</span>
                <span style="background: rgba(191, 90, 242, 0.15); border: 1px solid rgba(191, 90, 242, 0.35); color: #BF5AF2; padding: 0.15rem 0.55rem; border-radius: 9999px; font-size: 0.72rem; font-weight: 700;">Coordinator ✨</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="font-weight: 600; color: #E2E8F0;">5. Mudit Bairagi</span>
                <span style="background: rgba(100, 210, 255, 0.15); border: 1px solid rgba(100, 210, 255, 0.35); color: #64D2FF; padding: 0.15rem 0.55rem; border-radius: 9999px; font-size: 0.72rem; font-weight: 700;">Coordinator ⚙️</span>
            </div>
        </div>
    </div>
    """
    render_html(html)

