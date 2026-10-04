"""
user_portal.py — US SMB Sales Tools Portal
"""
import base64, io
import streamlit as st
from PIL import Image

# ── Favicon: square 64×64, SAP logo centred on dark navy ─────────────────────
_FAV_B64 = "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"
_favicon = Image.open(io.BytesIO(base64.b64decode(_FAV_B64)))

st.set_page_config(
    page_title="US SMB Sales Tools",
    page_icon=_favicon,
    layout="wide",
)

# ── NAV LOGO: pre-baked PNG data URI (defined in CSS — survives Streamlit) ────
_NAV_LOGO = "data:image/png;base64,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"

# ── Global CSS ─────────────────────────────────────────────────────────────────
st.markdown(f"""
<style>
    /* ── Page ── */
    .block-container {{
        padding-top: 0 !important;
        padding-bottom: 2rem !important;
        max-width: 1180px !important;
    }}
    body, [data-testid="stAppViewContainer"] {{
        background-color: #F5F7FA !important;
    }}

    /* ── SAP logo class — data URI lives here, not in HTML ── */
    .sap-logo-img {{
        background-image: url("{_NAV_LOGO}");
        background-repeat: no-repeat;
        background-size: contain;
        background-position: center left;
        display: inline-block;
        width: 72px;
        height: 36px;
        vertical-align: middle;
    }}

    /* ── Navigation ── */
    .sap-nav {{
        background: linear-gradient(100deg, #00144A 0%, #002A86 55%, #1B5CA8 100%);
        padding: 13px 32px;
        margin: -4rem -4rem 2rem -4rem;
        border-bottom: 2px solid #1B90FF;
    }}
    .sap-nav-divider {{
        display: inline-block;
        width: 1px;
        height: 22px;
        background: rgba(255,255,255,0.35);
        vertical-align: middle;
        margin: 0 12px;
    }}
    .sap-nav-title {{
        color: #ffffff;
        font-size: 1rem;
        font-weight: 600;
        font-family: Arial, sans-serif;
        vertical-align: middle;
        letter-spacing: 0.01em;
    }}
    .sap-nav-sub {{
        color: #89D1FF;
        font-size: 0.78rem;
        font-family: Arial, sans-serif;
        float: right;
        margin-top: 9px;
    }}

    /* ── Section label ── */
    .sap-label {{
        font-size: 0.68rem;
        font-weight: 700;
        color: #002A86;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin: 0 0 0.5rem 0;
        padding-left: 0.6rem;
        border-left: 3px solid #1B90FF;
    }}

    /* ── App card ── */
    .sap-card {{
        background: #ffffff;
        border: 1px solid #D9E1E8;
        border-top: 3px solid #1B90FF;
        border-radius: 4px;
        padding: 1rem 1.2rem 0.85rem 1.2rem;
        box-shadow: 0 2px 6px rgba(0,42,134,0.08);
        margin-bottom: 0.4rem;
        transition: box-shadow 0.15s ease;
    }}
    .sap-card:hover {{
        box-shadow: 0 4px 12px rgba(0,42,134,0.14);
    }}
    .sap-card-title {{
        color: #002A86;
        font-size: 0.95rem;
        font-weight: 700;
        margin: 0 0 0.4rem 0;
        font-family: Arial, sans-serif;
        line-height: 1.3;
    }}
    .sap-card-desc {{
        color: #4A4A4A;
        font-size: 0.82rem;
        line-height: 1.5;
        margin: 0 0 0.75rem 0;
    }}
    .sap-tag {{
        display: inline-block;
        background: #E8F2FF;
        color: #00144A;
        border-radius: 2px;
        font-size: 0.66rem;
        font-weight: 700;
        padding: 2px 6px;
        margin-right: 4px;
        text-transform: uppercase;
        letter-spacing: 0.04em;
    }}
    .sap-badge {{
        font-size: 0.66rem;
        font-weight: 700;
        padding: 2px 7px;
        border-radius: 2px;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        float: right;
    }}

    /* ── Open app button ── */
    div[data-testid="stLinkButton"] a {{
        background: #002A86 !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 3px !important;
        font-weight: 600 !important;
        font-size: 0.82rem !important;
    }}
    div[data-testid="stLinkButton"] a:hover {{
        background: #1B90FF !important;
    }}

    /* ── Expander ── */
    div[data-testid="stExpander"] {{
        border: 1px solid #D9E1E8 !important;
        border-radius: 3px !important;
        background: #ffffff !important;
    }}

    /* ── Footer ── */
    .sap-footer {{
        text-align: center;
        color: #888;
        font-size: 0.74rem;
        padding: 1.5rem 0 0.5rem;
        border-top: 1px solid #D9E1E8;
        margin-top: 1rem;
        font-family: Arial, sans-serif;
    }}
</style>
""", unsafe_allow_html=True)

# ── Navigation bar ─────────────────────────────────────────────────────────────
# Logo via CSS class (background-image defined above — not in HTML attrs)
# Simple inline HTML: no nested divs, no flex, just text
st.markdown("""
<div class="sap-nav">
    <span class="sap-logo-img"></span>
    <span class="sap-nav-divider"></span>
    <span class="sap-nav-title">US SMB Sales Tools</span>
    <span class="sap-nav-sub">GTM Operations</span>
</div>
""", unsafe_allow_html=True)

# ── Session ID how-to ─────────────────────────────────────────────────────────
def _sid_html():
    steps = [
        "Open Salesforce and make sure you are fully logged in.",
        ("Open developer tools using <strong>either</strong> method:<br>"
         "&nbsp;&nbsp;&#8226; Press <strong>F12</strong> on your keyboard<br>"
         "&nbsp;&nbsp;&#8226; <strong>Right-click</strong> anywhere on the page "
         "&rarr; <strong>Inspect</strong> or <strong>Inspect Element</strong>"),
        "Click the <strong>Application</strong> tab (Chrome / Edge) or "
        "<strong>Storage</strong> tab (Firefox).",
        "Expand <strong>Cookies</strong> in the left panel and click the Salesforce domain.",
        "Find the cookie named <code>sid</code> and copy the full value.",
        "Paste it into the <strong>Session ID</strong> field and click Connect.",
    ]
    note = "Session IDs expire on logout or after inactivity — grab a fresh one if the app stops responding."
    html = ('<p style="font-size:0.72rem;font-weight:700;color:#002A86;'
            'text-transform:uppercase;letter-spacing:0.08em;'
            'border-top:1px solid #D9E1E8;padding-top:0.75rem;margin-top:1rem;">'
            '&#128273;&nbsp; Getting your Salesforce Session ID</p>')
    for i, s in enumerate(steps, 1):
        html += (f'<div style="display:flex;gap:0.55rem;margin-bottom:0.45rem;align-items:flex-start;">'
                 f'<div style="min-width:19px;height:19px;border-radius:50%;'
                 f'background:#002A86;color:#fff;font-size:0.65rem;font-weight:700;'
                 f'display:flex;align-items:center;justify-content:center;'
                 f'flex-shrink:0;margin-top:2px;">{i}</div>'
                 f'<div style="font-size:0.81rem;color:#333;line-height:1.45;">{s}</div>'
                 f'</div>')
    html += (f'<div style="background:#E8F2FF;border-left:3px solid #1B90FF;'
             f'border-radius:2px;padding:0.45rem 0.7rem;'
             f'font-size:0.78rem;color:#00144A;margin-top:0.4rem;">'
             f'&#128161; {note}</div>')
    return html

# ── App registry ───────────────────────────────────────────────────────────────
APPS = [
    {
        "name": "Performance Dashboard \u2014 US SMB",
        "description": "Track your attainment against plan in real time. Breaks down your total quota credit into its individual components \u2014 Closed-Won ARR, LTC Incentive, Retention Incentive, and Complete Incentive.",
        "url": "https://smb-client-sales-performance-dashboard-fnbeugwlcwmxwvtgwneup3.streamlit.app/",
        "tags": ["Performance", "Quota", "Salesforce"],
        "audience": "All", "uses_sf": True,
        "how_to": [
            "Enter your Salesforce Session ID when prompted (instructions below).",
            "Select your name from the rep dropdown, or a team/segment view if you are a leader.",
            "Your YTD attainment and component breakdown load automatically.",
            "Use the date range filter to view a specific period.",
            "Hover over each bar for exact CW ARR, LTC, Retention, and Complete amounts.",
        ],
    },
    {
        "name": "Performance Dashboard \u2014 Global SMB",
        "description": "Same quota attainment and component breakdown as the US dashboard \u2014 Closed-Won ARR, LTC, Retention, and Complete Incentives \u2014 built for the UK, Australia, and Canada SMB teams.",
        "url": "https://global-smb-client-sales-performance-dashboard.streamlit.app/",
        "tags": ["Performance", "Quota", "Global"],
        "audience": "All", "uses_sf": True,
        "how_to": [
            "Enter your Salesforce Session ID when prompted (instructions below).",
            "Select your region (UK, Australia, or Canada) then your name.",
            "Your YTD attainment and component breakdown load automatically.",
            "Use the date range filter to view a specific period.",
            "Hover over each bar for exact amounts.",
        ],
    },
    {
        "name": "Watermark Dashboard \u2014 US SMB",
        "description": "See all accounts in your book with an active watermark deficit. Shows the deficit amount, effective date, and expiry \u2014 so you\u2019re never caught off guard on a renewal.",
        "url": "https://smb-watermark-tool-usclientsales.streamlit.app/",
        "tags": ["Accounts", "Watermark", "Salesforce"],
        "audience": "All", "uses_sf": True,
        "how_to": [
            "Enter your Salesforce Session ID when prompted (instructions below).",
            "Your active watermark accounts load automatically.",
            "Each row shows deficit amount, effective date, and expiry.",
            "Accounts expiring within 30 days are highlighted.",
            "Export as CSV using the download button.",
        ],
    },
    {
        "name": "Watermark Dashboard \u2014 Global SMB",
        "description": "Same watermark visibility as the US tool \u2014 active deficits, effective dates, and expiry dates \u2014 built for the UK, Australia, and Canada SMB teams.",
        "url": "https://watermark-appglobal-smb.streamlit.app/",
        "tags": ["Accounts", "Watermark", "Global"],
        "audience": "All", "uses_sf": True,
        "how_to": [
            "Enter your Salesforce Session ID when prompted (instructions below).",
            "Select your region (UK, Australia, or Canada).",
            "Your active watermark accounts load with deficit, effective date, and expiry.",
            "Accounts expiring within 30 days are highlighted.",
            "Export as CSV if needed.",
        ],
    },
    {
        "name": "Split Calculator",
        "description": "Submit and calculate credit splits when two or more accounts consolidate. The tool calculates each rep\u2019s percentage, emails Field Services, and logs the submission.",
        "url": "https://github.wdf.sap.corp/pages/I521094/Split-Calculator/",
        "tags": ["Splits", "Leaders"],
        "audience": "Leaders", "uses_sf": False,
        "how_to": [
            "Open the app \u2014 no Salesforce login required.",
            "Paste the Salesforce URL for the consolidating account and opportunity.",
            "Enter expense transaction amounts for each entity.",
            "Review the calculated credit percentage \u2014 adjust if needed.",
            "Click Submit to email Field Services and log the submission.",
        ],
    },
]

AUD_BG    = {"All": "#E8F2FF", "Leaders": "#FFF3CD", "Reps": "#E6F4EA"}
AUD_COLOR = {"All": "#00144A", "Leaders": "#7A5800", "Reps": "#1B6B3A"}
AUD_LABEL = {"All": "All Users", "Leaders": "Leaders Only", "Reps": "Reps Only"}

# ── Subtitle ───────────────────────────────────────────────────────────────────
st.markdown(
    "<p style='color:#4A4A4A;font-size:0.88rem;margin:0 0 1.4rem 0;'>"
    "All your Salesforce-connected tools in one place. "
    "Click <strong>Open app</strong> on any card to launch in a new tab.</p>",
    unsafe_allow_html=True)

# ── Filter ─────────────────────────────────────────────────────────────────────
st.markdown("<p class='sap-label'>Filter by audience</p>", unsafe_allow_html=True)

audience_filter = st.segmented_control(
    label="filter", label_visibility="collapsed",
    options=["All Users", "Leaders only", "Reps only"], default="All Users",
)
_map     = {"All Users": None, "Leaders only": "Leaders", "Reps only": "Reps"}
selected = _map[audience_filter]
filtered = [a for a in APPS if selected is None or a["audience"] in (selected, "All")]

st.markdown(
    f"<p style='color:#888;font-size:0.78rem;margin:0.4rem 0 1.4rem 0;'>"
    f"{len(filtered)} app{'s' if len(filtered) != 1 else ''}</p>",
    unsafe_allow_html=True)

# ── Cards ──────────────────────────────────────────────────────────────────────
for batch in [filtered[i:i+3] for i in range(0, len(filtered), 3)]:
    cols = st.columns(3, gap="medium")
    for col, app in zip(cols, batch):
        with col:
            tags = "".join(f'<span class="sap-tag">{t}</span>' for t in app["tags"])
            ab, ac, al = AUD_BG[app["audience"]], AUD_COLOR[app["audience"]], AUD_LABEL[app["audience"]]
            st.markdown(
                f'<div class="sap-card">' +
                f'<span class="sap-badge" style="background:{ab};color:{ac};">{al}</span>' +
                f'<p class="sap-card-title">{app["name"]}</p>' +
                f'<p class="sap-card-desc">{app["description"]}</p>' +
                f'{tags}</div>',
                unsafe_allow_html=True)
            st.link_button("Open app \u2192", app["url"], use_container_width=True)
            with st.expander("How to use this app"):
                html = ""
                for n, step in enumerate(app["how_to"], 1):
                    html += (
                        f'<div style="display:flex;gap:0.55rem;margin-bottom:0.45rem;align-items:flex-start;">' +
                        f'<div style="min-width:19px;height:19px;border-radius:50%;' +
                        f'background:#002A86;color:#fff;font-size:0.65rem;font-weight:700;' +
                        f'display:flex;align-items:center;justify-content:center;' +
                        f'flex-shrink:0;margin-top:2px;">{n}</div>' +
                        f'<div style="font-size:0.81rem;color:#333;line-height:1.45;">{step}</div></div>'
                    )
                if app["uses_sf"]:
                    html += _sid_html()
                st.markdown(html, unsafe_allow_html=True)
    st.markdown("")

# ── Footer ─────────────────────────────────────────────────────────────────────
st.markdown(
    '<div class="sap-footer">SAP SE &nbsp;&middot;&nbsp; GTM Operations' +
    ' &nbsp;&middot;&nbsp; Questions? Contact your GTM Ops rep</div>',
    unsafe_allow_html=True)
