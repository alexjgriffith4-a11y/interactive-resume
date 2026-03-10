import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ── Page config ──────────────────────────────────────────────
st.set_page_config(
    page_title="Alex Griffith | Resume",
    page_icon="📊",
    layout="wide",
)

# ── Custom CSS ────────────────────────────────────────────────
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@300;400;500&display=swap');
  html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
  h1, h2, h3 { font-family: 'DM Serif Display', serif; }
  .hero { background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
          color: white; padding: 2.5rem 2rem; border-radius: 12px; margin-bottom: 1.5rem; }
  .hero h1 { font-size: 2.6rem; margin-bottom: 0.2rem; color: white; }
  .hero p  { font-size: 1rem; opacity: 0.85; margin: 0; }
  .metric-card { background: #f8f9fb; border-left: 4px solid #2c5364;
                 padding: 1rem 1.2rem; border-radius: 8px; margin-bottom: 0.8rem; }
  .tag { display: inline-block; background: #e8f0fe; color: #1a56db;
         padding: 2px 10px; border-radius: 20px; font-size: 0.78rem; margin: 2px; }
</style>
""", unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <h1>Alex Griffith</h1>
  <p>📍 Toronto, ON &nbsp;|&nbsp; ✉️ alexjgriffith4@gmail.com &nbsp;|&nbsp;
     🔗 linkedin.com/in/alexjordangriffith/ &nbsp;|&nbsp; 📞 (437) 229-4971</p>
</div>
""", unsafe_allow_html=True)

# ── Sidebar navigation ────────────────────────────────────────
st.sidebar.title("Navigate")
section = st.sidebar.radio("Go to", ["Overview", "Experience", "Skills", "Education"])

# ════════════════════════════════════════════════════════════
#  OVERVIEW
# ════════════════════════════════════════════════════════════
if section == "Overview":
    st.subheader("👋 About Me")
    st.write(
        "Data Scientist and finance professional with a background spanning insurance analytics, "
        "venture capital, and machine learning. Currently completing an MMA at Rotman (June 2026) "
        "and holding CFA Level II."
    )

    col1, col2, col3 = st.columns(3)
    col1.metric("Years of Experience", "3+")
    col2.metric("CFA Level", "II Passed")
    col3.metric("Portfolio Managed", "$400M")

    st.divider()

    # ── Widget 1: quick-filter tags ──
    st.subheader("🔍 Filter Highlights by Domain")
    domain = st.selectbox("Choose a domain", ["All", "Data Science", "Finance", "Venture Capital"])

    highlights = {
        "Data Science": [
            "Built two-stage tree-based classification & regression model (PySpark / Scikit-learn)",
            "Exploratory statistical analysis within Databricks across England & Wales property data",
            "Proposed structural improvements to point-in-time datasets for trend analysis",
        ],
        "Finance": [
            "Analyzed $400M multi-asset insurance portfolio (1,000+ holdings)",
            "Reverse-engineered ALIRT quantitative rating methodology into Excel scoring model",
            "Built 5-year RBC forecasting model with scenario & stress-testing modules",
        ],
        "Venture Capital": [
            "Assessed 20+ African fintech startups for product viability & investment fit",
            "Analyzed VC/PE trends across multiple African markets for deal sourcing",
        ],
    }

    shown = highlights if domain == "All" else {domain: highlights[domain]}
    for dom, items in shown.items():
        st.markdown(f"**{dom}**")
        for item in items:
            st.markdown(f"- {item}")

# ════════════════════════════════════════════════════════════
#  EXPERIENCE
# ════════════════════════════════════════════════════════════
elif section == "Experience":
    st.subheader("💼 Work Experience")

    # ── Widget 2: company selector ──
    company = st.selectbox("Select a role to expand", [
        "Ryan LLC — Data Scientist (2026–Present)",
        "Sagicor Life Insurance — Accounting & Finance Technician (2022–2025)",
        "Havaic Inc. — Venture Capital Intern (2021)",
    ])

    details = {
        "Ryan LLC — Data Scientist (2026–Present)": {
            "desc": "Global tax services & software firm serving multinational corporations.",
            "bullets": [
                "PySpark & Python (Pandas, NumPy, Scikit-learn) within Databricks for location-driven feature analysis",
                "Two-stage tree-based classification & regression model across England and Wales",
                "Identified structural limitations in property datasets; presented improvements to Senior DS leadership",
            ],
            "tags": ["Python", "PySpark", "Scikit-learn", "Databricks", "ML"],
        },
        "Sagicor Life Insurance — Accounting & Finance Technician (2022–2025)": {
            "desc": "U.S.-based life insurance provider; $400M multi-asset portfolio.",
            "bullets": [
                "Total return & sector allocation variance analysis; quarterly benchmark-relative reporting",
                "Reduced reporting preparation time ~60% via template streamlining",
                "Reverse-engineered ALIRT rating methodology into a weighted Excel scoring model",
                "Built 5-year RBC forecasting model with base, best-case, and downside scenarios",
            ],
            "tags": ["Excel", "Power BI", "Clearwater Analytics", "FP&A", "RBC"],
        },
        "Havaic Inc. — Venture Capital Intern (2021)": {
            "desc": "Leading VC firm investing in African startups.",
            "bullets": [
                "Market research & financial analysis on 20+ African fintech startups",
                "VC/PE trend analysis across multiple African markets for deal sourcing",
            ],
            "tags": ["Market Research", "Financial Analysis", "VC", "Fintech"],
        },
    }

    d = details[company]
    st.caption(d["desc"])
    for b in d["bullets"]:
        st.markdown(f"- {b}")
    tags_html = " ".join(f'<span class="tag">{t}</span>' for t in d["tags"])
    st.markdown(tags_html, unsafe_allow_html=True)

    st.divider()

    # ── Timeline chart ──
    st.subheader("📅 Experience Timeline")
    timeline_data = pd.DataFrame({
        "Role": ["VC Intern", "Finance Technician", "Data Scientist"],
        "Company": ["Havaic Inc.", "Sagicor Life", "Ryan LLC"],
        "Start": [2021.5, 2022.0, 2026.0],
        "End":   [2021.7, 2025.0, 2026.5],
        "Color": ["#4db6ac", "#1565c0", "#6a1b9a"],
    })

    fig = go.Figure()
    for _, row in timeline_data.iterrows():
        fig.add_trace(go.Bar(
            x=[row["End"] - row["Start"]],
            y=[row["Role"]],
            base=[row["Start"]],
            orientation="h",
            marker_color=row["Color"],
            name=row["Company"],
            text=row["Company"],
            textposition="inside",
            hovertemplate=f"<b>{row['Role']}</b><br>{row['Company']}<br>{row['Start']:.0f}–{row['End']:.0f}<extra></extra>",
        ))

    fig.update_layout(
        barmode="overlay",
        xaxis=dict(title="Year", range=[2020.5, 2027]),
        yaxis=dict(title=""),
        showlegend=False,
        height=250,
        margin=dict(l=20, r=20, t=20, b=40),
        plot_bgcolor="#f8f9fb",
    )
    st.plotly_chart(fig, use_container_width=True)

# ════════════════════════════════════════════════════════════
#  SKILLS
# ════════════════════════════════════════════════════════════
elif section == "Skills":
    st.subheader("🛠 Skills & Proficiency")

    # ── Widget 3: slider to filter minimum proficiency ──
    min_prof = st.slider("Show skills with proficiency ≥", 1, 10, 5)

    skills = pd.DataFrame({
        "Skill":       ["Python", "SQL", "R", "Excel", "Tableau", "Power BI",
                        "PySpark", "Scikit-learn", "Clearwater Analytics", "Databricks"],
        "Category":    ["Programming", "Programming", "Programming", "Software", "Software", "Software",
                        "Programming", "Programming", "Software", "Software"],
        "Proficiency": [9, 8, 6, 9, 7, 7, 7, 8, 6, 7],
    })

    filtered = skills[skills["Proficiency"] >= min_prof]

    # Radar / bar chart
    fig2 = px.bar(
        filtered.sort_values("Proficiency", ascending=True),
        x="Proficiency", y="Skill", color="Category",
        orientation="h",
        color_discrete_map={"Programming": "#1565c0", "Software": "#4db6ac"},
        range_x=[0, 10],
    )
    fig2.update_layout(height=400, margin=dict(l=10, r=10, t=10, b=30), plot_bgcolor="#f8f9fb")
    st.plotly_chart(fig2, use_container_width=True)

    st.divider()
    st.subheader("📋 Skills Table")
    st.dataframe(
        filtered[["Skill", "Category", "Proficiency"]].sort_values("Proficiency", ascending=False).reset_index(drop=True),
        use_container_width=True,
    )

# ════════════════════════════════════════════════════════════
#  EDUCATION
# ════════════════════════════════════════════════════════════
elif section == "Education":
    st.subheader("🎓 Education")

    edu = pd.DataFrame({
        "Institution": ["Rotman School of Management", "CFA Institute", "Rollins College"],
        "Credential":  ["MMA Candidate (June 2026)", "CFA Level II Pass (2024)", "BA International Business (2022)"],
        "Location":    ["Toronto, ON", "Charlottesville, VA", "Winter Park, FL"],
        "Award":       ["Entrance Award $5K + GAB Scholarship $2K", "—", "Alonzo Rollins Scholarship $27.5K/yr"],
    })

    st.dataframe(edu, use_container_width=True, hide_index=True)

    st.divider()

    # ── Widget 4: checkbox to show extracurriculars ──
    show_extra = st.checkbox("Show extracurricular activities", value=True)
    if show_extra:
        extras = {
            "Rotman School of Management": ["MMA Director, Rotman Asset Management Association"],
            "Rollins College": ["Recruitment Chair, Chi Psi Fraternity"],
        }
        for inst, activities in extras.items():
            st.markdown(f"**{inst}**")
            for a in activities:
                st.markdown(f"- {a}")

    st.divider()
    st.subheader("📊 Scholarship Value Comparison")
    award_fig = px.bar(
        pd.DataFrame({
            "Institution": ["Rollins College\n(per year)", "Rotman MMA\n(entrance)", "Rotman MMA\n(GAB)"],
            "Amount ($)":  [27500, 5000, 2000],
        }),
        x="Institution", y="Amount ($)",
        color="Institution",
        color_discrete_sequence=["#1565c0", "#4db6ac", "#6a1b9a"],
        text_auto=True,
    )
    award_fig.update_layout(showlegend=False, plot_bgcolor="#f8f9fb", height=320)
    st.plotly_chart(award_fig, use_container_width=True)
