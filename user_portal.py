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
        "name": "Performance Dashboard — US SMB",
        "description": "Track your attainment against plan in real time. Breaks down your total quota credit into its individual components — Closed-Won ARR, LTC Incentive, Retention Incentive, and Complete Incentive — so you can see exactly where you stand and where to focus.",
        "url": "https://smb-client-sales-performance-dashboard-fnbeugwlcwmxwvtgwneup3.streamlit.app/",
        "tags": ["Performance", "Quota", "Salesforce"],
        "audience": "All",
    },
    {
        "name": "Performance Dashboard — Global SMB",
        "description": "Same quota attainment and component breakdown as the US dashboard — Closed-Won ARR, LTC, Retention, and Complete Incentives — built for the UK, Australia, and Canada SMB teams.",
        "url": "https://global-smb-client-sales-performance-dashboard.streamlit.app/",
        "tags": ["Performance", "Quota", "Global"],
        "audience": "All",
    },
    {
        "name": "Watermark Dashboard — US SMB",
        "description": "See all accounts in your book that currently carry an active watermark deficit. Shows the deficit amount, the date it went into effect, and when it expires — so you're never caught off guard on a renewal or expansion deal.",
        "url": "https://smb-watermark-tool-usclientsales.streamlit.app/",
        "tags": ["Accounts", "Watermark", "Salesforce"],
        "audience": "All",
    },
    {
        "name": "Watermark Dashboard — Global SMB",
        "description": "Same watermark visibility as the US tool — active deficits, effective dates, and expiry dates — built for the UK, Australia, and Canada SMB teams.",
        "url": "https://watermark-appglobal-smb.streamlit.app/",
        "tags": ["Accounts", "Watermark", "Global"],
        "audience": "All",
    },
    {
        "name": "Split Calculator",
        "description": "Submit and calculate credit splits when two or more accounts consolidate. Paste the account and opportunity links, enter each entity's expense transactions, and the tool calculates the percentage each rep receives. Hitting submit fires an email directly to Field Services to process the split and logs the submission for your own records.",
        "url": "https://github.wdf.sap.corp/pages/I521094/Split-Calculator/",
        "tags": ["Splits", "Leaders"],
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
