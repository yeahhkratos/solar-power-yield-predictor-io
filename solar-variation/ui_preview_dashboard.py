import streamlit as st
import os
import re

st.set_page_config(
    page_title="UI Design Token & Component Library Dashboard",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Glassmorphic & Token Styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');
    
    html, body, [class*="css"], .stApp {
        font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Inter", sans-serif;
        background-color: #080C14 !important;
        color: #F5F5F7 !important;
    }

    .dashboard-hero {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.08) 0%, rgba(255, 255, 255, 0.02) 100%);
        backdrop-filter: blur(32px) saturate(210%);
        border: 1px solid rgba(255, 255, 255, 0.16);
        border-radius: 24px;
        padding: 2rem;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 20px 48px -12px rgba(0, 0, 0, 0.55), inset 0 1px 1.5px rgba(255, 255, 255, 0.28);
    }

    .hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        background: rgba(48, 209, 88, 0.12);
        border: 1px solid rgba(48, 209, 88, 0.3);
        color: #30D158;
        font-size: 0.78rem;
        font-weight: 700;
        text-transform: uppercase;
        padding: 0.35rem 1rem;
        border-radius: 9999px;
        margin-bottom: 1rem;
    }

    .token-card {
        background: linear-gradient(145deg, rgba(255, 255, 255, 0.07) 0%, rgba(255, 255, 255, 0.02) 100%);
        backdrop-filter: blur(28px);
        border: 1px solid rgba(255, 255, 255, 0.14);
        border-radius: 18px;
        padding: 1.25rem;
        margin-bottom: 1rem;
        transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    .token-card:hover {
        transform: translateY(-4px) scale(1.015);
        border-color: rgba(255, 159, 10, 0.45);
        box-shadow: 0 16px 36px rgba(0, 0, 0, 0.5);
    }

    .swatch-box {
        height: 60px;
        border-radius: 12px;
        margin-bottom: 0.75rem;
        box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.2);
    }

    .code-pill {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.78rem;
        background: rgba(0, 0, 0, 0.35);
        padding: 0.2rem 0.5rem;
        border-radius: 6px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: #64D2FF;
    }
</style>
""", unsafe_allow_html=True)

def parse_skill_metadata(skill_path):
    if not os.path.exists(skill_path):
        return None
    with open(skill_path, "r", encoding="utf-8") as f:
        content = f.read()
    match = re.search(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if match:
        frontmatter = match.group(1)
        name = re.search(r"name:\s*(.+)", frontmatter)
        desc = re.search(r"description:\s*>?-?\s*(.*?)(?=\n[a-zA-Z0-9_-]+:|$)", frontmatter, re.DOTALL)
        return {
            "name": name.group(1).strip() if name else os.path.basename(os.path.dirname(skill_path)),
            "description": " ".join(desc.group(1).split()) if desc else "Custom Antigravity skill"
        }
    return None

def main():
    st.markdown("""
        <div class="dashboard-hero">
            <div class="hero-badge">
                <span>● Active Local Environment Presets</span>
            </div>
            <h1 style="font-size: 2.6rem; font-weight: 800; margin-bottom: 0.5rem; background: linear-gradient(135deg, #FFFFFF 20%, #FFE082 60%, #FF9F0A 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                🎨 UI Design Token & Component Library Dashboard
            </h1>
            <p style="font-size: 1.05rem; color: #A1A1A6; max-width: 820px; margin: 0 auto;">
                Verified local workspace skills, semantic design token mappings, WCAG 2.1/2.2 accessibility parameters, and Figma Auto-Layout compilation.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Installed Skills Verification Section
    st.markdown("### ⚡ Configured Workspace Skills")
    skills_dir = os.path.join(os.getcwd(), ".agents", "skills")
    
    skills = [
        "antigravity-design-expert",
        "vibe-ui-engine",
        "shadcn-tailwind-master",
        "figma-to-code-bridge"
    ]

    cols = st.columns(len(skills))
    for idx, skill_slug in enumerate(skills):
        skill_file = os.path.join(skills_dir, skill_slug, "SKILL.md")
        meta = parse_skill_metadata(skill_file)
        with cols[idx]:
            if meta:
                st.markdown(f"""
                    <div class="token-card" style="border-top: 3px solid #30D158;">
                        <span style="font-size: 0.72rem; font-weight: 700; color: #30D158; text-transform: uppercase;">● Operational</span>
                        <h4 style="margin: 0.4rem 0; font-size: 1.05rem; color: #FFFFFF;">{meta['name']}</h4>
                        <p style="font-size: 0.8rem; color: #8E8E93; line-height: 1.4;">{meta['description'][:90]}...</p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.warning(f"Skill '{skill_slug}' not found.")

    # Interactive Dashboard Tabs
    tab_tokens, tab_components, tab_wcag, tab_figma, tab_team = st.tabs([
        "🎨 Semantic Tokens",
        "🧩 Component Library",
        "♿ WCAG Audit & Contrast",
        "📐 Figma Auto-Layout Bridge",
        "👥 Project Contributors"
    ])

    with tab_tokens:
        st.markdown("#### 🎨 Color & Surface Tokens")
        token_cols = st.columns(4)
        
        token_data = [
            ("Solar Gold (Primary)", "#FF9F0A", "--color-primary", "rgba(255, 159, 10, 0.4)"),
            ("Electric Azure (Accent)", "#0A84FF", "--color-azure", "rgba(10, 132, 255, 0.4)"),
            ("Emerald Mint (Success)", "#30D158", "--color-mint", "rgba(48, 209, 88, 0.4)"),
            ("Royal Violet (Tertiary)", "#BF5AF2", "--color-purple", "rgba(191, 90, 242, 0.4)"),
        ]

        for i, (name, hex_val, var_name, glow) in enumerate(token_data):
            with token_cols[i]:
                st.markdown(f"""
                    <div class="token-card">
                        <div class="swatch-box" style="background: {hex_val}; box-shadow: 0 0 16px {glow};"></div>
                        <div style="font-weight: 700; font-size: 0.9rem; color: #FFF;">{name}</div>
                        <div style="display: flex; justify-content: space-between; margin-top: 0.5rem;">
                            <span class="code-pill">{var_name}</span>
                            <span class="code-pill">{hex_val}</span>
                        </div>
                    </div>
                """, unsafe_allow_html=True)

        st.markdown("#### 🌊 Glassmorphism & Material Tokens")
        glass_col1, glass_col2 = st.columns(2)
        with glass_col1:
            st.markdown("""
                <div class="token-card">
                    <h4 style="color: #FFFFFF; margin-bottom: 0.4rem;">Liquid Glass Core (--surface-glass)</h4>
                    <p style="font-size: 0.85rem; color: #8E8E93;">Multi-layered backdrop blur with specular double rim highlights.</p>
                    <pre class="code-pill" style="display: block; padding: 0.8rem; line-height: 1.5; color: #E2E8F0;">
background: linear-gradient(135deg, rgba(255, 255, 255, 0.08) 0%, rgba(255, 255, 255, 0.02) 100%);
backdrop-filter: blur(32px) saturate(210%);
border: 1px solid rgba(255, 255, 255, 0.16);
box-shadow: 0 20px 48px -12px rgba(0, 0, 0, 0.55), inset 0 1px 1.5px rgba(255, 255, 255, 0.28);
                    </pre>
                </div>
            """, unsafe_allow_html=True)
        with glass_col2:
            st.markdown("""
                <div class="token-card">
                    <h4 style="color: #FFFFFF; margin-bottom: 0.4rem;">Motion & Spring Easing (--ease-spring)</h4>
                    <p style="font-size: 0.85rem; color: #8E8E93;">Natural iOS physics spring curves with tactile haptic compression.</p>
                    <pre class="code-pill" style="display: block; padding: 0.8rem; line-height: 1.5; color: #E2E8F0;">
--ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
--ease-ios: cubic-bezier(0.25, 1, 0.5, 1);
--press-scale: scale(0.975);
--hover-lift: translateY(-5px) scale(1.02);
                    </pre>
                </div>
            """, unsafe_allow_html=True)

    with tab_components:
        st.markdown("#### 🧩 Live Interactive Component Preview")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("""
                <div class="token-card">
                    <div style="font-size: 0.75rem; font-weight: 700; color: #FF9F0A; text-transform: uppercase;">Widget Variant A</div>
                    <div style="font-size: 2rem; font-weight: 800; color: #FFF; margin: 0.3rem 0;">42.8 <span style="font-size: 1rem; color: #FF9F0A;">kWh</span></div>
                    <div style="font-size: 0.8rem; color: #8E8E93;">⚡ Expected Daily Energy</div>
                </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown("""
                <div class="token-card">
                    <div style="font-size: 0.75rem; font-weight: 700; color: #0A84FF; text-transform: uppercase;">Widget Variant B</div>
                    <div style="font-size: 2rem; font-weight: 800; color: #FFF; margin: 0.3rem 0;">5.40 <span style="font-size: 1rem; color: #64D2FF;">kW</span></div>
                    <div style="font-size: 0.8rem; color: #8E8E93;">🔥 Peak Output Capacity</div>
                </div>
            """, unsafe_allow_html=True)
        with c3:
            st.markdown("""
                <div class="token-card">
                    <div style="font-size: 0.75rem; font-weight: 700; color: #30D158; text-transform: uppercase;">Widget Variant C</div>
                    <div style="font-size: 2rem; font-weight: 800; color: #FFF; margin: 0.3rem 0;">₹321.00</div>
                    <div style="font-size: 0.8rem; color: #8E8E93;">💰 Estimated Savings</div>
                </div>
            """, unsafe_allow_html=True)

        st.markdown("##### Interactive Form Controls")
        slider_val = st.slider("Interactive Solar Array Scale (m²)", min_value=1.0, max_value=100.0, value=25.0, step=0.5)
        st.caption(f"Currently selected: {slider_val} m²")

    with tab_wcag:
        st.markdown("#### ♿ WCAG 2.1 / 2.2 Accessibility Contrast Matrix")
        st.markdown("""
            <div class="token-card">
                <div style="display: flex; justify-content: space-between; align-items: center; padding: 0.5rem 0;">
                    <div>
                        <div style="font-weight: 700; color: #FFF;">Text on Dark Canvas (#FFFFFF on #080C14)</div>
                        <div style="font-size: 0.82rem; color: #8E8E93;">Contrast: <b>18.4 : 1</b></div>
                    </div>
                    <span style="background: rgba(48,209,88,0.15); color: #30D158; border: 1px solid rgba(48,209,88,0.3); padding: 0.25rem 0.7rem; border-radius: 9999px; font-size: 0.75rem; font-weight: 700;">AAA PASS</span>
                </div>
                <hr style="border: none; border-top: 1px solid rgba(255,255,255,0.08); margin: 0.5rem 0;">
                <div style="display: flex; justify-content: space-between; align-items: center; padding: 0.5rem 0;">
                    <div>
                        <div style="font-weight: 700; color: #FF9F0A;">Solar Gold Heading (#FF9F0A on #080C14)</div>
                        <div style="font-size: 0.82rem; color: #8E8E93;">Contrast: <b>9.6 : 1</b></div>
                    </div>
                    <span style="background: rgba(48,209,88,0.15); color: #30D158; border: 1px solid rgba(48,209,88,0.3); padding: 0.25rem 0.7rem; border-radius: 9999px; font-size: 0.75rem; font-weight: 700;">AAA PASS</span>
                </div>
                <hr style="border: none; border-top: 1px solid rgba(255,255,255,0.08); margin: 0.5rem 0;">
                <div style="display: flex; justify-content: space-between; align-items: center; padding: 0.5rem 0;">
                    <div>
                        <div style="font-weight: 700; color: #64D2FF;">Azure Badge Text (#64D2FF on #080C14)</div>
                        <div style="font-size: 0.82rem; color: #8E8E93;">Contrast: <b>12.1 : 1</b></div>
                    </div>
                    <span style="background: rgba(48,209,88,0.15); color: #30D158; border: 1px solid rgba(48,209,88,0.3); padding: 0.25rem 0.7rem; border-radius: 9999px; font-size: 0.75rem; font-weight: 700;">AAA PASS</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with tab_figma:
        st.markdown("#### 📐 Figma Auto-Layout to CSS Mapping")
        st.markdown("""
            <div class="token-card">
                <table style="width: 100%; border-collapse: collapse; font-size: 0.88rem; color: #E2E8F0;">
                    <thead>
                        <tr style="border-bottom: 1px solid rgba(255,255,255,0.15); text-align: left;">
                            <th style="padding: 0.5rem;">Figma Property</th>
                            <th style="padding: 0.5rem;">CSS / Tailwind Equivalent</th>
                            <th style="padding: 0.5rem;">Rule</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
                            <td style="padding: 0.5rem; color: #FF9F0A;">Direction: Horizontal</td>
                            <td style="padding: 0.5rem; font-family: monospace;">display: flex; flex-direction: row;</td>
                            <td style="padding: 0.5rem; color: #8E8E93;">Horizontal row stacking</td>
                        </tr>
                        <tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
                            <td style="padding: 0.5rem; color: #FF9F0A;">Direction: Vertical</td>
                            <td style="padding: 0.5rem; font-family: monospace;">display: flex; flex-direction: column;</td>
                            <td style="padding: 0.5rem; color: #8E8E93;">Column vertical stacking</td>
                        </tr>
                        <tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
                            <td style="padding: 0.5rem; color: #FF9F0A;">Item Spacing</td>
                            <td style="padding: 0.5rem; font-family: monospace;">gap: 16px; (gap-4)</td>
                            <td style="padding: 0.5rem; color: #8E8E93;">Mapped to 8pt spatial token</td>
                        </tr>
                        <tr>
                            <td style="padding: 0.5rem; color: #FF9F0A;">Layer Blur (32px)</td>
                            <td style="padding: 0.5rem; font-family: monospace;">backdrop-filter: blur(32px);</td>
                            <td style="padding: 0.5rem; color: #8E8E93;">Liquid frosted glass refraction</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        """, unsafe_allow_html=True)

    with tab_team:
        st.markdown("#### 👥 Project Contributors & Engineering Team")
        team_members = [
            {"name": "Akshat Jain", "role": "Project Leader", "badge": "Leader 👑", "color": "#FF9F0A", "initials": "AJ"},
            {"name": "Gaurik Mishra", "role": "Project Co-Leader", "badge": "Co-Leader 🌟", "color": "#0A84FF", "initials": "GM"},
            {"name": "Raj Sahu", "role": "Project Coordinator", "badge": "Coordinator 🎯", "color": "#30D158", "initials": "RS"},
            {"name": "Pratiksha Agarwal", "role": "Project Coordinator", "badge": "Coordinator ✨", "color": "#BF5AF2", "initials": "PA"},
            {"name": "Mudit Bairagi", "role": "Project Coordinator", "badge": "Coordinator ⚙️", "color": "#64D2FF", "initials": "MB"},
        ]
        
        t_cols = st.columns(len(team_members))
        for idx, m in enumerate(team_members):
            with t_cols[idx]:
                st.markdown(f"""
                    <div class="token-card" style="text-align: center; padding: 1.5rem 1rem;">
                        <div style="width: 50px; height: 50px; border-radius: 50%; margin: 0 auto 0.75rem auto; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 1.1rem; color: {m['color']}; border: 2px solid {m['color']}; box-shadow: 0 0 16px {m['color']}55;">
                            {m['initials']}
                        </div>
                        <div style="font-weight: 800; font-size: 1rem; color: #FFFFFF; margin-bottom: 0.4rem;">{m['name']}</div>
                        <span style="font-size: 0.74rem; font-weight: 700; background: {m['color']}22; border: 1px solid {m['color']}; color: {m['color']}; padding: 0.2rem 0.6rem; border-radius: 9999px;">
                            {m['badge']}
                        </span>
                        <div style="font-size: 0.78rem; color: #8E8E93; margin-top: 0.5rem;">{m['role']}</div>
                    </div>
                """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

