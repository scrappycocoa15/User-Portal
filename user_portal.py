"""
user_portal.py — Sales Rep & Leader App Portal
Deploy as a standalone Streamlit app on Community Cloud.
Edit the APPS list to add/remove/update entries.
"""

import streamlit as st

st.set_page_config(
    page_title="US SMB Sales Tools",
    page_icon="📊",
    layout="wide",
)

# ── Styling ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    .block-container { padding-top: 2rem; padding-bottom: 2rem; }
    .app-card {
        background: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 1.2rem 1.4rem 1rem 1.4rem;
        height: 100%;
        box-shadow: 0 1px 4px rgba(0,0,0,0.06);
    }
    .app-card h4 { margin: 0 0 0.3rem 0; color: #003F70; font-size: 1rem; }
    .app-card p  { margin: 0 0 0.8rem 0; color: #555; font-size: 0.85rem; line-height: 1.4; }
    .tag {
        display: inline-block;
        background: #E8F0FE;
        color: #003F70;
        border-radius: 4px;
        font-size: 0.72rem;
        padding: 1px 7px;
        margin-right: 4px;
        font-weight: 600;
    }
    .divider { border-top: 1px solid #eee; margin: 1.5rem 0; }
    h1 { color: #003F70; }
</style>
""", unsafe_allow_html=True)

# ── App registry ───────────────────────────────────────────────────────────
# Edit this list to add, remove, or update apps.
# tags: used to group/label apps. audience: "All" | "Leaders" | "Reps"
APPS = [
    {
        "name": "Account Snapshot",
        "description": "Pull a live ARR and utilization snapshot for any account directly from Salesforce. Useful before a QBR or renewal conversation.",
        "url": "https://your-app-url-1.streamlit.app",
        "tags": ["Salesforce", "Accounts"],
        "audience": "All",
    },
    {
        "name": "Territory Overview",
        "description": "See your full book of business by ARR band, utilization tier, and growth trend. Refreshes against the latest Salesforce data.",
        "url": "https://your-app-url-2.streamlit.app",
        "tags": ["Salesforce", "Territory"],
        "audience": "Reps",
    },
    {
        "name": "Pipeline & Forecast",
        "description": "Real-time pipeline view with CW projections by rep and segment. Includes LTC and Retention breakdowns.",
        "url": "https://your-app-url-3.streamlit.app",
        "tags": ["Salesforce", "Pipeline"],
        "audience": "Leaders",
    },
    {
        "name": "Quota Tracker",
        "description": "Track quota attainment YTD by rep. Pulls live from Salesforce — no manual refresh needed.",
        "url": "https://your-app-url-4.streamlit.app",
        "tags": ["Quota", "Salesforce"],
        "audience": "All",
    },
    {
        "name": "Account Scoring",
        "description": "View potential, momentum, and noise scores for accounts in your territory. Helps prioritize outreach.",
        "url": "https://your-app-url-5.streamlit.app",
        "tags": ["Accounts", "Scoring"],
        "audience": "Reps",
    },
    {
        "name": "Team Performance Dashboard",
        "description": "Segment-level view of CW ARR, attainment, and deal velocity. Updated daily.",
        "url": "https://your-app-url-6.streamlit.app",
        "tags": ["Reporting", "Leaders"],
        "audience": "Leaders",
    },
]

AUDIENCE_COLOR = {"All": "#E6F4EA", "Leaders": "#FFF3CD", "Reps": "#E8F0FE"}
AUDIENCE_LABEL = {"All": "All Users", "Leaders": "Leaders", "Reps": "Reps"}

# ── Header ─────────────────────────────────────────────────────────────────
col_logo, col_title = st.columns([1, 10])
with col_title:
    st.markdown("# US SMB Sales Tools")
    st.markdown("All your Salesforce-connected tools in one place. Click any card to open the app.")

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ── Filter ─────────────────────────────────────────────────────────────────
audience_filter = st.segmented_control(
    "Show apps for:",
    options=["All Users", "Leaders only", "Reps only"],
    default="All Users",
)

filter_map = {"All Users": None, "Leaders only": "Leaders", "Reps only": "Reps"}
selected = filter_map[audience_filter]
filtered = [a for a in APPS if selected is None or a["audience"] in (selected, "All")]

st.markdown(f"<p style='color:#888;font-size:0.85rem'>{len(filtered)} app{'s' if len(filtered)!=1 else ''} shown</p>",
            unsafe_allow_html=True)

# ── App cards ──────────────────────────────────────────────────────────────
COLS = 3
rows = [filtered[i:i+COLS] for i in range(0, len(filtered), COLS)]

for row in rows:
    cols = st.columns(COLS, gap="medium")
    for col, app in zip(cols, row):
        with col:
            tag_html = "".join(f'<span class="tag">{t}</span>' for t in app["tags"])
            aud_bg   = AUDIENCE_COLOR.get(app["audience"], "#eee")
            aud_lbl  = AUDIENCE_LABEL.get(app["audience"], app["audience"])
            st.markdown(f"""
            <div class="app-card">
                <h4>{app['name']}</h4>
                <p>{app['description']}</p>
                {tag_html}
                <span style="float:right;font-size:0.72rem;background:{aud_bg};
                    padding:1px 7px;border-radius:4px;color:#555;font-weight:600">{aud_lbl}</span>
            </div>
            """, unsafe_allow_html=True)
            st.link_button("Open app →", app["url"], use_container_width=True)
    st.markdown("")

# ── Footer ─────────────────────────────────────────────────────────────────
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown("<p style='color:#aaa;font-size:0.8rem;text-align:center'>Questions or issues? Reach out to GTM Ops.</p>",
            unsafe_allow_html=True)
