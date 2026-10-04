"""
user_portal.py — US SMB Sales Tools Portal
SAP-styled using color system only. No embedded images that fight Streamlit's renderer.
"""
import streamlit as st
from PIL import Image, ImageDraw

# ── Favicon: SAP Dark Navy square (PIL only, no cairosvg needed) ─────────────
def _favicon():
    img = Image.new("RGBA", (64, 64), (0, 42, 134, 255))
    d = ImageDraw.Draw(img)
    d.polygon([(36, 0), (64, 0), (64, 28)], fill=(27, 144, 255, 80))
    return img

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
