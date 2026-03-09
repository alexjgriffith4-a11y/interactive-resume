import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Alex Morgan | Resume",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .hero { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            padding: 2.5rem 2rem; border-radius: 16px; color: white; margin-bottom: 1.5rem; }
    .hero h1 { font-size: 2.6rem; font-weight: 700; margin: 0; }
    .hero p  { font-size: 1.1rem; opacity: .85; margin: .4rem 0 0; }
    .badge { display:inline-block; background:#e94560; color:#fff;
             padding:.25rem .75rem; border-radius:999px; font-size:.8rem;
             font-weight:600; margin:.2rem; }
    .section-title { font-size:1.4rem; font-weight:700; color:#0f3460;
                     border-left:4px solid #e94560; padding-left:.6rem;
                     margin:1.5rem 0 .8rem; }
    .card { background:#f8f9ff; border-radius:12px; padding:1.2rem 1.5rem;
            border:1px solid #e0e4f0; margin-bottom:1rem; }
    .card h4 { margin:0 0 .3rem; color:#1a1a2e; font-size:1rem; font-weight:600; }
    .card p  { margin:0; color:#555; font-size:.9rem; }
    .metric-box { text-align:center; background:#0f3460; color:white;
                  border-radius:12px; padding:1rem; }
    .metric-box .num { font-size:2rem; font-weight:700; color:#e94560; }
    .metric-box .lbl { font-size:.8rem; opacity:.8; }
</style>
""", unsafe_allow_html=True)

# ── Data ──────────────────────────────────────────────────────────────────────
SKILLS = {
    "Python":90, "Machine Learning":85, "SQL":88, "Data Visualization":82,
    "Deep Learning":75, "Cloud (AWS/GCP)":78, "Spark / Big Data":70,
    "Statistics":87, "React / JS":60, "Docker / DevOps":65,
}

EXPERIENCE = [
    {"Company":"NovaTech AI","Role":"Senior Data Scientist","Start":2022,"End":2025,
     "Desc":"Led ML platform development; reduced model deployment time by 60%."},
    {"Company":"DataBridge Corp","Role":"Data Scientist","Start":2019,"End":2022,
     "Desc":"Built recommendation engine generating $4M additional annual revenue."},
    {"Company":"InsightLab","Role":"Data Analyst","Start":2017,"End":2019,
     "Desc":"Designed dashboards and automated ETL pipelines for 12 clients."},
    {"Company":"Freelance","Role":"ML Consultant","Start":2015,"End":2017,
     "Desc":"Computer-vision and NLP projects for start-ups across North America."},
]

EDUCATION = [
    {"Degree":"M.Sc. Computer Science (AI)","Institution":"University of Toronto","Year":2017,"GPA":"3.9/4.0"},
    {"Degree":"B.Sc. Statistics & Mathematics","Institution":"McGill University","Year":2015,"GPA":"3.8/4.0"},
]

PROJECTS = [
    {"name":"Fraud Detection Engine","tech":"Python · XGBoost · Kafka","desc":"Real-time transaction scoring at 50k events/sec with 98.7% precision."},
    {"name":"NLP Sentiment Platform","tech":"PyTorch · Transformers · FastAPI","desc":"Fine-tuned BERT model deployed as REST API; serves 2M requests/day."},
    {"name":"Sales Forecasting Dashboard","tech":"Prophet · Streamlit · Plotly","desc":"Interactive forecasting tool adopted by 5 enterprise clients."},
    {"name":"Medical Image Classifier","tech":"TensorFlow · ResNet · DICOM","desc":"CNN achieving radiologist-level accuracy on chest X-ray pathology detection."},
]

CERTS = ["AWS Certified ML Specialist","Google Professional Data Engineer",
         "TensorFlow Developer Certificate","Databricks Certified Associate"]

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.image("https://api.dicebear.com/7.x/avataaars/svg?seed=AlexMorgan&backgroundColor=0f3460",
             width=120)
    st.markdown("## Alex Morgan")
    st.caption("Senior Data Scientist · Toronto, CA")
    st.markdown("---")
    st.markdown("### 🎛️ Customize View")

    section = st.selectbox(
        "Jump to section",
        ["Overview", "Skills", "Experience", "Education", "Projects", "Contact"],
    )

    skill_threshold = st.slider(
        "Show skills above proficiency (%)", 0, 100, 60, 5,
        help="Filter the skills chart by minimum proficiency level",
    )

    show_all_exp = st.checkbox("Show all experience", value=True)
    dark_chart = st.checkbox("Dark chart theme", value=False)

    st.markdown("---")
    st.markdown("📧 alex.morgan@email.com")
    st.markdown("🔗 [LinkedIn](#)  |  [GitHub](#)")

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <h1>👋 Alex Morgan</h1>
  <p>Senior Data Scientist · 10+ years turning messy data into business impact</p>
  <p style="margin-top:.8rem">
    <span class="badge">Machine Learning</span>
    <span class="badge">Python</span>
    <span class="badge">Deep Learning</span>
    <span class="badge">Cloud</span>
    <span class="badge">Big Data</span>
  </p>
</div>
""", unsafe_allow_html=True)

# ── Metrics row ───────────────────────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)
for col, num, lbl in zip(
    [c1, c2, c3, c4],
    ["10+", "25+", "$12M+", "4"],
    ["Years Experience", "Projects Shipped", "Revenue Generated", "Certifications"],
):
    col.markdown(f"""
    <div class="metric-box">
      <div class="num">{num}</div>
      <div class="lbl">{lbl}</div>
    </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Skills ────────────────────────────────────────────────────────────────────
if section in ("Overview", "Skills"):
    st.markdown('<div class="section-title">🧠 Skills Proficiency</div>', unsafe_allow_html=True)

    filtered = {k: v for k, v in SKILLS.items() if v >= skill_threshold}
    if not filtered:
        st.info("No skills above that threshold — try lowering the slider.")
    else:
        df_skills = pd.DataFrame(filtered.items(), columns=["Skill", "Proficiency"]).sort_values("Proficiency")
        template = "plotly_dark" if dark_chart else "plotly_white"
        fig = px.bar(df_skills, x="Proficiency", y="Skill", orientation="h",
                     color="Proficiency", color_continuous_scale="RdBu",
                     range_x=[0, 100], template=template,
                     labels={"Proficiency": "Proficiency (%)"},
                     title=f"Skills ≥ {skill_threshold}% proficiency")
        fig.update_layout(height=40 * len(filtered) + 120, coloraxis_showscale=False,
                          margin=dict(l=10, r=10, t=40, b=10))
        fig.update_traces(text=df_skills["Proficiency"].astype(str) + "%", textposition="outside")
        st.plotly_chart(fig, use_container_width=True)

# ── Experience ────────────────────────────────────────────────────────────────
if section in ("Overview", "Experience"):
    st.markdown('<div class="section-title">💼 Work Experience</div>', unsafe_allow_html=True)

    display_exp = EXPERIENCE if show_all_exp else EXPERIENCE[:2]

    # Timeline chart
    df_exp = pd.DataFrame(display_exp)
    template = "plotly_dark" if dark_chart else "plotly_white"
    fig2 = go.Figure()
    colors = ["#e94560", "#0f3460", "#533483", "#e94560"]
    for i, row in df_exp.iterrows():
        fig2.add_trace(go.Bar(
            x=[row["End"] - row["Start"]],
            y=[row["Company"]],
            base=row["Start"],
            orientation="h",
            marker_color=colors[i % len(colors)],
            name=row["Role"],
            hovertemplate=f"<b>{row['Role']}</b> @ {row['Company']}<br>{row['Start']}–{row['End']}<extra></extra>",
        ))
    fig2.update_layout(barmode="overlay", template=template,
                       title="Career Timeline", xaxis_title="Year",
                       height=250, showlegend=False, margin=dict(l=10, r=10, t=40, b=10))
    st.plotly_chart(fig2, use_container_width=True)

    # Cards
    for job in display_exp:
        st.markdown(f"""
        <div class="card">
          <h4>{job['Role']} — {job['Company']} ({job['Start']}–{job['End']})</h4>
          <p>{job['Desc']}</p>
        </div>""", unsafe_allow_html=True)

# ── Education ─────────────────────────────────────────────────────────────────
if section in ("Overview", "Education"):
    st.markdown('<div class="section-title">🎓 Education</div>', unsafe_allow_html=True)
    df_edu = pd.DataFrame(EDUCATION)
    st.dataframe(
        df_edu.rename(columns={"Degree":"Degree / Programme","Institution":"School","Year":"Grad Year","GPA":"GPA"}),
        use_container_width=True, hide_index=True,
    )

# ── Projects ──────────────────────────────────────────────────────────────────
if section in ("Overview", "Projects"):
    st.markdown('<div class="section-title">🚀 Featured Projects</div>', unsafe_allow_html=True)
    cols = st.columns(2)
    for i, proj in enumerate(PROJECTS):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="card">
              <h4>{proj['name']}</h4>
              <p style="color:#e94560;font-size:.8rem;margin-bottom:.4rem">{proj['tech']}</p>
              <p>{proj['desc']}</p>
            </div>""", unsafe_allow_html=True)

    # Certifications table
    st.markdown('<div class="section-title">🏅 Certifications</div>', unsafe_allow_html=True)
    df_certs = pd.DataFrame({"Certification": CERTS, "Status": ["✅ Active"] * len(CERTS)})
    st.dataframe(df_certs, use_container_width=True, hide_index=True)

# ── Contact ───────────────────────────────────────────────────────────────────
if section == "Contact":
    st.markdown('<div class="section-title">📬 Get In Touch</div>', unsafe_allow_html=True)
    with st.form("contact_form"):
        name  = st.text_input("Your Name")
        email = st.text_input("Your Email")
        msg   = st.text_area("Message")
        if st.form_submit_button("Send Message 🚀"):
            if name and email and msg:
                st.success(f"Thanks {name}! Message received — I'll reply to {email} shortly.")
            else:
                st.warning("Please fill in all fields.")

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("---")
st.caption("Built with ❤️ using Streamlit · © 2025 Alex Morgan")
