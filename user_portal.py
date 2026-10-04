"""
user_portal.py — US SMB Sales Tools Portal
SAP-styled using color system only. No embedded images that fight Streamlit's renderer.
"""
import streamlit as st
from PIL import Image, ImageDraw

# ── Favicon: SAP Dark Navy square (PIL only, no cairosvg needed) ─────────────
# SAP logo PNG pre-baked as base64 — no cairosvg needed at runtime
_SAP_PNG_B64 = "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"

def _favicon():
    import base64, io
    return Image.open(io.BytesIO(base64.b64decode(_SAP_PNG_B64)))

st.set_page_config(
    page_title="US SMB Sales Tools",
    page_icon=_favicon(),
    layout="wide",
)

# ── CSS — SAP Classic Corporate color system ──────────────────────────────────
st.markdown("""
<style>
    /* Page layout */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 2rem !important;
        max-width: 1200px !important;
    }

    /* SAP-style nav bar — text only, no images, fully reliable */
    .sap-nav {
        background: #002A86;
        padding: 14px 0 14px 0;
        margin: -1rem -5rem 2rem -5rem;
        border-bottom: 3px solid #1B90FF;
    }
    .sap-nav-inner {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 1rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .sap-nav-title {
        color: #ffffff;
        font-size: 1.05rem;
        font-weight: 700;
        font-family: Arial, sans-serif;
        letter-spacing: 0.01em;
    }
    .sap-nav-brand {
        color: #1B90FF;
        font-size: 0.85rem;
        font-weight: 800;
        font-family: Arial, sans-serif;
        letter-spacing: 0.08em;
        background: rgba(27,144,255,0.15);
        padding: 3px 10px;
        border-radius: 3px;
    }
    .sap-nav-sub {
        color: #89D1FF;
        font-size: 0.78rem;
        font-family: Arial, sans-serif;
    }

    /* Section label */
    .sap-label {
        font-size: 0.68rem;
        font-weight: 700;
        color: #002A86;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin: 0 0 0.5rem 0;
        padding-left: 0.6rem;
        border-left: 3px solid #1B90FF;
    }

    /* App card */
    .sap-card {
        background: #ffffff;
        border: 1px solid #EAECEE;
        border-top: 3px solid #1B90FF;
        border-radius: 4px;
        padding: 1.1rem 1.3rem 0.9rem 1.3rem;
        box-shadow: 0 1px 4px rgba(0, 42, 134, 0.06);
        margin-bottom: 0.4rem;
        min-height: 160px;
    }
    .sap-card-title {
        color: #002A86;
        font-size: 0.95rem;
        font-weight: 700;
        margin: 0 0 0.45rem 0;
        font-family: Arial, sans-serif;
    }
    .sap-card-desc {
        color: #444444;
        font-size: 0.82rem;
        line-height: 1.5;
        margin: 0 0 0.75rem 0;
    }
    .sap-tag {
        display: inline-block;
        background: #D1EFFF;
        color: #002A86;
        border-radius: 2px;
        font-size: 0.67rem;
        font-weight: 700;
        padding: 2px 7px;
        margin-right: 4px;
        text-transform: uppercase;
        letter-spacing: 0.04em;
    }
    .sap-badge {
        float: right;
        font-size: 0.67rem;
        font-weight: 700;
        padding: 2px 8px;
        border-radius: 2px;
        text-transform: uppercase;
        letter-spacing: 0.04em;
    }

    /* Open app button */
    div[data-testid="stLinkButton"] a {
        background: #002A86 !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 3px !important;
        font-weight: 600 !important;
        font-size: 0.82rem !important;
        letter-spacing: 0.01em !important;
        transition: background 0.15s ease !important;
    }
    div[data-testid="stLinkButton"] a:hover {
        background: #1B90FF !important;
    }

    /* Expander */
    div[data-testid="stExpander"] {
        border: 1px solid #EAECEE !important;
        border-radius: 3px !important;
    }
    div[data-testid="stExpander"] summary {
        font-size: 0.82rem !important;
        color: #555 !important;
    }

    /* Segmented control */
    div[data-testid="stSegmentedControl"] {
        margin-bottom: 0.5rem !important;
    }

    /* Footer */
    .sap-footer {
        text-align: center;
        color: #aaaaaa;
        font-size: 0.74rem;
        padding: 1.5rem 0 0.5rem 0;
        border-top: 1px solid #EAECEE;
        margin-top: 1rem;
        font-family: Arial, sans-serif;
    }
</style>
""", unsafe_allow_html=True)

# ── Nav bar — simple text, zero data URIs, guaranteed to render ───────────────
st.markdown("""
<div class="sap-nav">
    <div class="sap-nav-inner">
        <div>
            <span class="sap-nav-brand">SAP</span>
            <span class="sap-nav-title" style="margin-left:12px;">
                US SMB Sales Tools
            </span>
        </div>
        <span class="sap-nav-sub">GTM Operations</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Session ID how-to (appended inside expanders for SF apps) ─────────────────
def _sid_html():
    steps = [
        "Open Salesforce in your browser and make sure you are fully logged in.",
        ("Open developer tools using <strong>either</strong> method:<br>"
         "&nbsp;&nbsp;&#8226; Press <strong>F12</strong> on your keyboard<br>"
         "&nbsp;&nbsp;&#8226; <strong>Right-click</strong> anywhere on the page "
         "&rarr; <strong>Inspect</strong> or <strong>Inspect Element</strong>"),
        "Click the <strong>Application</strong> tab (Chrome / Edge) or "
        "<strong>Storage</strong> tab (Firefox).",
        "In the left panel, expand <strong>Cookies</strong> and click the Salesforce domain.",
        "Find the cookie named <code>sid</code> and copy the full value.",
        "Paste it into the <strong>Session ID</strong> field in the app and click Connect.",
    ]
    note = ("Your session ID expires on logout or after inactivity. "
            "If the app stops working, refresh Salesforce and grab a fresh one.")
    html = ("<p style='font-size:0.72rem;font-weight:700;color:#002A86;"
            "text-transform:uppercase;letter-spacing:0.08em;"
            "border-top:1px solid #EAECEE;padding-top:0.7rem;margin-top:0.9rem;'>"
            "&#128273;&nbsp; Getting your Salesforce Session ID</p>")
    for i, s in enumerate(steps, 1):
        html += (
            f"<div style='display:flex;gap:0.55rem;margin-bottom:0.45rem;"
            f"align-items:flex-start;'>"
            f"<div style='min-width:19px;height:19px;border-radius:50%;"
            f"background:#002A86;color:#fff;font-size:0.65rem;font-weight:700;"
            f"display:flex;align-items:center;justify-content:center;"
            f"flex-shrink:0;margin-top:2px;'>{i}</div>"
            f"<div style='font-size:0.81rem;color:#333;line-height:1.45;'>{s}</div>"
            f"</div>"
        )
    html += (
        f"<div style='background:#D1EFFF;border-left:3px solid #1B90FF;"
        f"border-radius:2px;padding:0.45rem 0.7rem;"
        f"font-size:0.78rem;color:#002A86;margin-top:0.4rem;'>"
        f"&#128161; {note}</div>"
    )
    return html

# ── App registry ──────────────────────────────────────────────────────────────
APPS = [
    {
        "name": "Performance Dashboard \u2014 US SMB",
        "description": "Track your attainment against plan in real time. Breaks down your total quota credit into its individual components \u2014 Closed-Won ARR, LTC Incentive, Retention Incentive, and Complete Incentive \u2014 so you can see exactly where you stand and where to focus.",
        "url": "https://smb-client-sales-performance-dashboard-fnbeugwlcwmxwvtgwneup3.streamlit.app/",
        "tags": ["Performance", "Quota", "Salesforce"],
        "audience": "All",
        "uses_sf": True,
        "how_to": [
            "Enter your Salesforce Session ID when prompted (instructions below).",
            "Select your name from the rep dropdown, or a team/segment view if you are a leader.",
            "Your YTD attainment and component breakdown load automatically.",
            "Use the date range filter to view performance for a specific period.",
            "Hover over each bar for exact CW ARR, LTC, Retention, and Complete amounts.",
        ],
    },
    {
        "name": "Performance Dashboard \u2014 Global SMB",
        "description": "Same quota attainment and component breakdown as the US dashboard \u2014 Closed-Won ARR, LTC, Retention, and Complete Incentives \u2014 built for the UK, Australia, and Canada SMB teams.",
        "url": "https://global-smb-client-sales-performance-dashboard.streamlit.app/",
        "tags": ["Performance", "Quota", "Global"],
        "audience": "All",
        "uses_sf": True,
        "how_to": [
            "Enter your Salesforce Session ID when prompted (instructions below).",
            "Select your region (UK, Australia, or Canada) then your name from the dropdown.",
            "Your YTD attainment and component breakdown load automatically.",
            "Use the date range filter to view a specific period.",
            "Hover over each bar for exact CW ARR, LTC, Retention, and Complete amounts.",
        ],
    },
    {
        "name": "Watermark Dashboard \u2014 US SMB",
        "description": "See all accounts in your book with an active watermark deficit. Shows the deficit amount, the date it went into effect, and when it expires \u2014 so you're never caught off guard on a renewal or expansion deal.",
        "url": "https://smb-watermark-tool-usclientsales.streamlit.app/",
        "tags": ["Accounts", "Watermark", "Salesforce"],
        "audience": "All",
        "uses_sf": True,
        "how_to": [
            "Enter your Salesforce Session ID when prompted (instructions below).",
            "Your active watermark accounts load automatically \u2014 no additional filters needed.",
            "Each row shows account name, deficit amount, effective date, and expiry date.",
            "Accounts expiring within 30 days are highlighted \u2014 prioritise for renewal conversations.",
            "Export the list as CSV using the download button.",
        ],
    },
    {
        "name": "Watermark Dashboard \u2014 Global SMB",
        "description": "Same watermark visibility as the US tool \u2014 active deficits, effective dates, and expiry dates \u2014 built for the UK, Australia, and Canada SMB teams.",
        "url": "https://watermark-appglobal-smb.streamlit.app/",
        "tags": ["Accounts", "Watermark", "Global"],
        "audience": "All",
        "uses_sf": True,
        "how_to": [
            "Enter your Salesforce Session ID when prompted (instructions below).",
            "Select your region (UK, Australia, or Canada).",
            "Your active watermark accounts load \u2014 each row shows deficit, effective date, and expiry.",
            "Accounts expiring within 30 days are highlighted.",
            "Export as CSV if needed.",
        ],
    },
    {
        "name": "Split Calculator",
        "description": "Submit and calculate credit splits when two or more accounts consolidate. Paste the account and opportunity links, enter each entity's expense transactions, and the tool calculates the percentage each rep receives. Hitting submit fires an email to Field Services and logs the submission.",
        "url": "https://github.wdf.sap.corp/pages/I521094/Split-Calculator/",
        "tags": ["Splits", "Leaders"],
        "audience": "Leaders",
        "uses_sf": False,
        "how_to": [
            "Open the app \u2014 no Salesforce login required.",
            "Paste the Salesforce URL for the consolidating account and the opportunity to be split.",
            "Enter the expense transaction amounts for each entity.",
            "Review the calculated credit percentage per rep \u2014 adjust values if needed.",
            "Click Submit \u2014 this emails Field Services and logs the submission in your history.",
        ],
    },
]

AUD_BG    = {"All": "#D1EFFF", "Leaders": "#FFF3CD", "Reps": "#E6F4EA"}
AUD_COLOR = {"All": "#002A86", "Leaders": "#7A5800", "Reps": "#1B6B3A"}
AUD_LABEL = {"All": "All Users", "Leaders": "Leaders Only", "Reps": "Reps Only"}

# ── Subtitle ──────────────────────────────────────────────────────────────────
st.markdown(
    "<p style='color:#555;font-size:0.88rem;margin:0 0 1.4rem 0;'>"
    "All your Salesforce-connected tools in one place. "
    "Click <strong>Open app</strong> on any card to launch it in a new tab.</p>",
    unsafe_allow_html=True,
)

# ── Filter ────────────────────────────────────────────────────────────────────
st.markdown("<p class='sap-label'>Filter by audience</p>", unsafe_allow_html=True)

audience_filter = st.segmented_control(
    label="filter",
    label_visibility="collapsed",
    options=["All Users", "Leaders only", "Reps only"],
    default="All Users",
)
_map     = {"All Users": None, "Leaders only": "Leaders", "Reps only": "Reps"}
selected = _map[audience_filter]
filtered = [a for a in APPS if selected is None or a["audience"] in (selected, "All")]

st.markdown(
    f"<p style='color:#999;font-size:0.78rem;margin:0.4rem 0 1.4rem 0;'>"
    f"{len(filtered)} app{'s' if len(filtered) != 1 else ''}</p>",
    unsafe_allow_html=True,
)

# ── Cards ─────────────────────────────────────────────────────────────────────
for batch in [filtered[i:i+3] for i in range(0, len(filtered), 3)]:
    cols = st.columns(3, gap="medium")
    for col, app in zip(cols, batch):
        with col:
            tags   = "".join(f'<span class="sap-tag">{t}</span>' for t in app["tags"])
            ab, ac = AUD_BG[app["audience"]], AUD_COLOR[app["audience"]]
            albl   = AUD_LABEL[app["audience"]]
            st.markdown(
                f'<div class="sap-card">'
                f'<span class="sap-badge" style="background:{ab};color:{ac};">{albl}</span>'
                f'<p class="sap-card-title">{app["name"]}</p>'
                f'<p class="sap-card-desc">{app["description"]}</p>'
                f'{tags}'
                f'</div>',
                unsafe_allow_html=True,
            )
            st.link_button("Open app \u2192", app["url"], use_container_width=True)
            with st.expander("How to use this app"):
                html = ""
                for n, step in enumerate(app["how_to"], 1):
                    html += (
                        f"<div style='display:flex;gap:0.55rem;margin-bottom:0.45rem;"
                        f"align-items:flex-start;'>"
                        f"<div style='min-width:19px;height:19px;border-radius:50%;"
                        f"background:#002A86;color:#fff;font-size:0.65rem;font-weight:700;"
                        f"display:flex;align-items:center;justify-content:center;"
                        f"flex-shrink:0;margin-top:2px;'>{n}</div>"
                        f"<div style='font-size:0.81rem;color:#333;line-height:1.45;'>{step}</div>"
                        f"</div>"
                    )
                if app["uses_sf"]:
                    html += _sid_html()
                st.markdown(html, unsafe_allow_html=True)
    st.markdown("")

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown(
    "<div class='sap-footer'>"
    "SAP SE &nbsp;&middot;&nbsp; GTM Operations &nbsp;&middot;&nbsp; "
    "Questions? Contact your GTM Ops rep"
    "</div>",
    unsafe_allow_html=True,
)
