"""
user_portal.py — US SMB Sales Tools Portal
SAP Classic Corporate style: Dark Navy (#002A86) header, SAP Blue (#1B90FF) accents.
Edit the APPS list to add/remove/update entries.
"""

import streamlit as st

st.set_page_config(
    page_title="US SMB Sales Tools",
    page_icon="https://upload.wikimedia.org/wikipedia/commons/5/59/SAP_2011_logo.svg",
    layout="wide",
)

# ── SAP Brand Colors ────────────────────────────────────────────────────────
# Classic Corporate style system
# Primary:    #1B90FF  (SAP Blue)
# Dark Navy:  #002A86  (headers, accents)
# Deep Navy:  #00144A  (hero bar)
# Light Sky:  #D1EFFF  (tag backgrounds)
# Light Gray: #EAECEE  (card borders, subtle bg)
# Gray text:  #666666

st.markdown("""
<style>
    /* ── Reset & base ── */
    .block-container { padding: 0 !important; max-width: 100% !important; }
    section[data-testid="stSidebar"] { display: none; }

    /* ── Hero header ── */
    .sap-hero {
        background: #002A86;
        padding: 0.9rem 2.5rem;
        display: flex;
        align-items: center;
        gap: 1.2rem;
        margin-bottom: 0;
    }
    .sap-hero-logo {
        font-size: 1.35rem;
        font-weight: 800;
        color: #FFFFFF;
        letter-spacing: 0.04em;
        background: #1B90FF;
        padding: 0.18rem 0.7rem;
        border-radius: 3px;
        font-family: '72', Arial, sans-serif;
    }
    .sap-hero-divider {
        width: 1px; height: 28px;
        background: rgba(255,255,255,0.3);
    }
    .sap-hero-title {
        color: #FFFFFF;
        font-size: 1.05rem;
        font-weight: 600;
        font-family: '72', Arial, sans-serif;
        letter-spacing: 0.01em;
    }
    .sap-hero-sub {
        color: #89D1FF;
        font-size: 0.8rem;
        margin-left: auto;
        font-family: '72', Arial, sans-serif;
    }

    /* ── Content area ── */
    .sap-body { padding: 1.8rem 2.5rem 2rem 2.5rem; }

    /* ── Section label ── */
    .sap-section-label {
        font-size: 0.7rem;
        font-weight: 700;
        color: #002A86;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin-bottom: 0.8rem;
        border-left: 3px solid #1B90FF;
        padding-left: 0.5rem;
    }

    /* ── App card ── */
    .sap-card {
        background: #FFFFFF;
        border: 1px solid #EAECEE;
        border-top: 3px solid #1B90FF;
        border-radius: 4px;
        padding: 1.1rem 1.3rem 0.9rem 1.3rem;
        box-shadow: 0 1px 3px rgba(0,42,134,0.07);
        margin-bottom: 0.5rem;
    }
    .sap-card-name {
        color: #002A86;
        font-size: 0.95rem;
        font-weight: 700;
        margin: 0 0 0.45rem 0;
        font-family: '72', Arial, sans-serif;
    }
    .sap-card-desc {
        color: #444444;
        font-size: 0.83rem;
        line-height: 1.5;
        margin: 0 0 0.7rem 0;
    }
    .sap-tag {
        display: inline-block;
        background: #D1EFFF;
        color: #002A86;
        border-radius: 2px;
        font-size: 0.68rem;
        font-weight: 700;
        padding: 2px 7px;
        margin-right: 4px;
        text-transform: uppercase;
        letter-spacing: 0.04em;
    }
    .sap-aud-badge {
        float: right;
        font-size: 0.68rem;
        font-weight: 700;
        padding: 2px 8px;
        border-radius: 2px;
        text-transform: uppercase;
        letter-spacing: 0.04em;
    }
    .aud-all     { background: #D1EFFF; color: #002A86; }
    .aud-leaders { background: #FFF3CD; color: #7A5800; }
    .aud-reps    { background: #E6F4EA; color: #1B6B3A; }

    /* ── How-to doc ── */
    .howto-step {
        display: flex;
        gap: 0.7rem;
        margin-bottom: 0.55rem;
        align-items: flex-start;
    }
    .howto-num {
        background: #002A86;
        color: #FFFFFF;
        font-size: 0.68rem;
        font-weight: 700;
        min-width: 20px;
        height: 20px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-top: 1px;
        flex-shrink: 0;
    }
    .howto-text { font-size: 0.82rem; color: #333; line-height: 1.45; }
    .howto-note {
        background: #D1EFFF;
        border-left: 3px solid #1B90FF;
        border-radius: 2px;
        padding: 0.5rem 0.75rem;
        font-size: 0.8rem;
        color: #002A86;
        margin-top: 0.6rem;
    }
    .sid-header {
        font-size: 0.75rem;
        font-weight: 700;
        color: #002A86;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin: 0.9rem 0 0.5rem 0;
        border-top: 1px solid #EAECEE;
        padding-top: 0.75rem;
    }

    /* ── Filter bar ── */
    .filter-label {
        font-size: 0.72rem;
        font-weight: 700;
        color: #666666;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-bottom: 0.4rem;
    }

    /* ── Footer ── */
    .sap-footer {
        text-align: center;
        color: #999999;
        font-size: 0.75rem;
        padding: 1.5rem 0 1rem 0;
        border-top: 1px solid #EAECEE;
        margin-top: 1rem;
    }

    /* Override Streamlit button */
    div[data-testid="stLinkButton"] a {
        background: #002A86 !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 3px !important;
        font-weight: 600 !important;
        font-size: 0.82rem !important;
        letter-spacing: 0.02em !important;
    }
    div[data-testid="stLinkButton"] a:hover {
        background: #1B90FF !important;
    }
    div[data-testid="stExpander"] {
        border: 1px solid #EAECEE !important;
        border-radius: 3px !important;
        margin-top: 0.4rem !important;
    }
</style>
""", unsafe_allow_html=True)

# ── Session ID how-to (shared across all SF-connected apps) ─────────────────
SESSION_ID_STEPS = [
    ("Open Salesforce in your browser and make sure you are fully logged in.", False),
    ("Open your browser's developer tools using <strong>either</strong> of these methods:<br>"
     "&nbsp;&nbsp;• Press <strong>F12</strong> on your keyboard<br>"
     "&nbsp;&nbsp;• <strong>Right-click</strong> anywhere on the Salesforce page → select <strong>Inspect</strong> or <strong>Inspect Element</strong>",
     False),
    ("In the developer tools panel, click the <strong>Application</strong> tab "
     "(Chrome / Edge) or the <strong>Storage</strong> tab (Firefox).", False),
    ("In the left panel, expand <strong>Cookies</strong> and click on the Salesforce domain "
     "(e.g. <code>*.salesforce.com</code> or <code>*.lightning.force.com</code>).", False),
    ("Find the cookie named <strong><code>sid</code></strong> in the list. "
     "Click on it and copy the full value — it is a long alphanumeric string.", False),
    ("Paste the value into the <strong>Session ID</strong> field in the app and click Connect.", False),
    ("Your session ID expires when you log out of Salesforce or after a period of inactivity. "
     "If the app stops pulling data, refresh your Salesforce page and grab a new ID.", True),
]

def render_session_id():
    steps_html = '<p class="sid-header">🔑 How to get your Salesforce Session ID</p>'
    for i, (text, is_note) in enumerate(SESSION_ID_STEPS[:-1], 1):
        steps_html += f'''
        <div class="howto-step">
            <div class="howto-num">{i}</div>
            <div class="howto-text">{text}</div>
        </div>'''
    steps_html += f'<div class="howto-note">💡 {SESSION_ID_STEPS[-1][0]}</div>'
    return steps_html

# ── App registry ────────────────────────────────────────────────────────────
APPS = [
    {
        "name": "Performance Dashboard — US SMB",
        "description": "Track your attainment against plan in real time. Breaks down your total quota credit into its individual components — Closed-Won ARR, LTC Incentive, Retention Incentive, and Complete Incentive — so you can see exactly where you stand and where to focus.",
        "url": "https://smb-client-sales-performance-dashboard-fnbeugwlcwmxwvtgwneup3.streamlit.app/",
        "tags": ["Performance", "Quota", "Salesforce"],
        "audience": "All",
        "uses_sf_session": True,
        "how_to": [
            ("Open the app and enter your Salesforce Session ID when prompted. See below for how to get it.", False),
            ("Select your name from the rep dropdown, or choose a team/segment view if you are a leader.", False),
            ("Your YTD attainment and component breakdown will load automatically.", False),
            ("Use the date range filter to view performance for a specific period.", False),
            ("The component chart breaks your total credit into CW ARR, LTC, Retention, and Complete — hover over each bar for exact amounts.", False),
        ],
    },
    {
        "name": "Performance Dashboard — Global SMB",
        "description": "Same quota attainment and component breakdown as the US dashboard — Closed-Won ARR, LTC, Retention, and Complete Incentives — built for the UK, Australia, and Canada SMB teams.",
        "url": "https://global-smb-client-sales-performance-dashboard.streamlit.app/",
        "tags": ["Performance", "Quota", "Global"],
        "audience": "All",
        "uses_sf_session": True,
        "how_to": [
            ("Open the app and enter your Salesforce Session ID when prompted. See below for how to get it.", False),
            ("Select your region (UK, Australia, or Canada) and then your name from the dropdown.", False),
            ("Your YTD attainment and component breakdown will load automatically.", False),
            ("Use the date range filter to view performance for a specific period.", False),
            ("The component chart breaks your total credit into CW ARR, LTC, Retention, and Complete — hover over each bar for exact amounts.", False),
        ],
    },
    {
        "name": "Watermark Dashboard — US SMB",
        "description": "See all accounts in your book that currently carry an active watermark deficit. Shows the deficit amount, the date it went into effect, and when it expires — so you're never caught off guard on a renewal or expansion deal.",
        "url": "https://smb-watermark-tool-usclientsales.streamlit.app/",
        "tags": ["Accounts", "Watermark", "Salesforce"],
        "audience": "All",
        "uses_sf_session": True,
        "how_to": [
            ("Open the app and enter your Salesforce Session ID when prompted. See below for how to get it.", False),
            ("Your active watermark accounts will load automatically — no additional filters needed.", False),
            ("Each row shows the account name, deficit amount, effective date, and expiry date.", False),
            ("Accounts with deficits expiring within 30 days are highlighted — prioritize those for renewal conversations.", False),
            ("You can export the list as a CSV using the download button at the top of the table.", False),
        ],
    },
    {
        "name": "Watermark Dashboard — Global SMB",
        "description": "Same watermark visibility as the US tool — active deficits, effective dates, and expiry dates — built for the UK, Australia, and Canada SMB teams.",
        "url": "https://watermark-appglobal-smb.streamlit.app/",
        "tags": ["Accounts", "Watermark", "Global"],
        "audience": "All",
        "uses_sf_session": True,
        "how_to": [
            ("Open the app and enter your Salesforce Session ID when prompted. See below for how to get it.", False),
            ("Select your region (UK, Australia, or Canada).", False),
            ("Your active watermark accounts will load — each row shows the deficit amount, effective date, and expiry date.", False),
            ("Accounts with deficits expiring within 30 days are highlighted.", False),
            ("Export the list as CSV using the download button if needed.", False),
        ],
    },
    {
        "name": "Split Calculator",
        "description": "Submit and calculate credit splits when two or more accounts consolidate. Paste the account and opportunity links, enter each entity's expense transactions, and the tool calculates the percentage each rep receives. Hitting submit fires an email directly to Field Services to process the split and logs the submission for your own records.",
        "url": "https://github.wdf.sap.corp/pages/I521094/Split-Calculator/",
        "tags": ["Splits", "Leaders"],
        "audience": "Leaders",
        "uses_sf_session": False,
        "how_to": [
            ("Open the app — no Salesforce login required.", False),
            ("Paste the Salesforce URL for the consolidating account and the opportunity that needs to be split.", False),
            ("Enter the expense transaction amounts for each entity involved in the consolidation.", False),
            ("The tool calculates the credit percentage for each rep automatically based on the transactions.", False),
            ("Review the split breakdown. Adjust any values if needed.", False),
            ("Click <strong>Submit</strong> — this sends an email directly to Field Services with the split details and logs the submission in your history.", False),
            ("You can view past submissions in the log at the bottom of the page.", False),
        ],
    },
]

AUD_CLASS = {"All": "aud-all", "Leaders": "aud-leaders", "Reps": "aud-reps"}
AUD_LABEL = {"All": "All Users", "Leaders": "Leaders Only", "Reps": "Reps Only"}

# ── Hero header ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="sap-hero">
    <span class="sap-hero-logo">SAP</span>
    <div class="sap-hero-divider"></div>
    <span class="sap-hero-title">US SMB Sales Tools</span>
    <span class="sap-hero-sub">GTM Operations</span>
</div>
<div class="sap-body">
""", unsafe_allow_html=True)

st.markdown(
    "<p style='color:#666;font-size:0.88rem;margin-bottom:1.2rem'>"
    "All your Salesforce-connected tools in one place. "
    "Click <strong>Open app</strong> on any card to launch it in a new tab.</p>",
    unsafe_allow_html=True,
)

# ── Filter ───────────────────────────────────────────────────────────────────
st.markdown('<p class="filter-label">Filter by audience</p>', unsafe_allow_html=True)
audience_filter = st.segmented_control(
    label="filter",
    options=["All Users", "Leaders only", "Reps only"],
    default="All Users",
    label_visibility="collapsed",
)
filter_map = {"All Users": None, "Leaders only": "Leaders", "Reps only": "Reps"}
selected    = filter_map[audience_filter]
filtered    = [a for a in APPS if selected is None or a["audience"] in (selected, "All")]

st.markdown(
    f"<p style='color:#999;font-size:0.78rem;margin:0.4rem 0 1.2rem 0'>"
    f"{len(filtered)} app{'s' if len(filtered)!=1 else ''}</p>",
    unsafe_allow_html=True,
)

# ── App cards ────────────────────────────────────────────────────────────────
COLS = 3
rows = [filtered[i:i+COLS] for i in range(0, len(filtered), COLS)]

for row in rows:
    cols = st.columns(COLS, gap="medium")
    for col, app in zip(cols, row):
        with col:
            # Card header (HTML)
            tags_html = "".join(f'<span class="sap-tag">{t}</span>' for t in app["tags"])
            aud_cls   = AUD_CLASS.get(app["audience"], "aud-all")
            aud_lbl   = AUD_LABEL.get(app["audience"], app["audience"])
            st.markdown(f"""
            <div class="sap-card">
                <span class="sap-aud-badge {aud_cls}">{aud_lbl}</span>
                <p class="sap-card-name">{app['name']}</p>
                <p class="sap-card-desc">{app['description']}</p>
                {tags_html}
            </div>
            """, unsafe_allow_html=True)

            # Open app button
            st.link_button("Open app →", app["url"], use_container_width=True)

            # How-to expander
            with st.expander("How to use this app"):
                steps_html = ""
                for i, (text, is_note) in enumerate(app["how_to"], 1):
                    if is_note:
                        steps_html += f'<div class="howto-note">💡 {text}</div>'
                    else:
                        steps_html += f'''
                        <div class="howto-step">
                            <div class="howto-num">{i}</div>
                            <div class="howto-text">{text}</div>
                        </div>'''

                if app["uses_sf_session"]:
                    steps_html += render_session_id()

                st.markdown(steps_html, unsafe_allow_html=True)

        st.markdown("")

# ── Footer ───────────────────────────────────────────────────────────────────
st.markdown("""
</div>
<div class="sap-footer">
    SAP SE &nbsp;·&nbsp; GTM Operations &nbsp;·&nbsp; Questions? Contact your GTM Ops rep
</div>
""", unsafe_allow_html=True)
