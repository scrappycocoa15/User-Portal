"""
user_portal.py — US SMB Sales Tools Portal
"""
import base64, cairosvg, io
import streamlit as st
from PIL import Image

# ── SAP logo as proper PNG favicon ──────────────────────────────────────────
_SVG = base64.b64decode("PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4KPCEtLSBHZW5lcmF0b3I6IEFkb2JlIElsbHVzdHJhdG9yIDI4LjMuMCwgU1ZHIEV4cG9ydCBQbHVnLUluIC4gU1ZHIFZlcnNpb246IDYuMDAgQnVpbGQgMCkgIC0tPgo8c3ZnIHZlcnNpb249IjEuMSIgaWQ9IkxheWVyXzEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9IjBweCIgeT0iMHB4IgoJIHZpZXdCb3g9IjAgMCA0MTIuNCAyMDQiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDQxMi40IDIwNDsiIHhtbDpzcGFjZT0icHJlc2VydmUiPgo8c3R5bGUgdHlwZT0idGV4dC9jc3MiPgoJLnN0MHtmaWxsLXJ1bGU6ZXZlbm9kZDtjbGlwLXJ1bGU6ZXZlbm9kZDtmaWxsOnVybCgjU1ZHSURfMV8pO30KCS5zdDF7ZmlsbC1ydWxlOmV2ZW5vZGQ7Y2xpcC1ydWxlOmV2ZW5vZGQ7ZmlsbDojRkZGRkZGO30KPC9zdHlsZT4KPGc+CgkKCQk8bGluZWFyR3JhZGllbnQgaWQ9IlNWR0lEXzFfIiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgeDE9IjIwNi4xOSIgeTE9IjIwNiIgeDI9IjIwNi4xOSIgeTI9IjIiIGdyYWRpZW50VHJhbnNmb3JtPSJtYXRyaXgoMSAwIDAgLTEgMCAyMDYpIj4KCQk8c3RvcCAgb2Zmc2V0PSIwIiBzdHlsZT0ic3RvcC1jb2xvcjojMDBCOEYxIi8+CgkJPHN0b3AgIG9mZnNldD0iMi4wMDAwMDBlLTAyIiBzdHlsZT0ic3RvcC1jb2xvcjojMDFCNkYwIi8+CgkJPHN0b3AgIG9mZnNldD0iMC4zMSIgc3R5bGU9InN0b3AtY29sb3I6IzBEOTBEOSIvPgoJCTxzdG9wICBvZmZzZXQ9IjAuNTgiIHN0eWxlPSJzdG9wLWNvbG9yOiMxNzc1QzgiLz4KCQk8c3RvcCAgb2Zmc2V0PSIwLjgyIiBzdHlsZT0ic3RvcC1jb2xvcjojMUM2NUJGIi8+CgkJPHN0b3AgIG9mZnNldD0iMSIgc3R5bGU9InN0b3AtY29sb3I6IzFFNUZCQiIvPgoJPC9saW5lYXJHcmFkaWVudD4KCTxwb2x5bGluZSBjbGFzcz0ic3QwIiBwb2ludHM9IjAsMjA0IDIwOC40LDIwNCA0MTIuNCwwIDAsMCAwLDIwNCAJIi8+Cgk8cGF0aCBjbGFzcz0ic3QxIiBkPSJNMjQ0LjcsMzguNGgtNDAuNnY5Ni41bC0zNS41LTk2LjZoLTM1LjJsLTMwLjMsODAuN0MxMDAsOTguNyw3OSw5MS43LDYyLjQsODYuNEM1MS41LDgyLjksMzkuOCw3Ny43LDQwLDcyCgkJYzAuMS00LjcsNi4yLTksMTguNC04LjRjOC4yLDAuNCwxNS40LDEuMSwyOS43LDhsMTQuMS0yNC41Yy0xMy4xLTYuNi0zMS4yLTEwLjktNDYtMTAuOWgtMC4xYy0xNy4zLDAtMzEuNyw1LjYtNDAuNiwxNC44CgkJYy02LjIsNi4zLTkuNywxNC44LTkuNywyMy43QzUuNSw4Ny4yLDEwLjEsOTYsMTkuNywxMDNjOC4xLDUuOSwxOC41LDkuOCwyNy42LDEyLjZjMTEuMywzLjUsMjAuNSw2LjUsMjAuNCwxMwoJCWMtMC4xLDIuNC0xLDQuNy0yLjcsNi40Yy0yLjgsMi45LTcuMSw0LTEzLjEsNC4xYy0xMS41LDAuMi0yMC0xLjYtMzMuNi05LjZMNS44LDE1NC40YzE0LDgsMjkuOSwxMi4yLDQ2LDEyLjJoMi4xCgkJYzE0LjItMC4yLDI1LjctNC4zLDM0LjktMTEuN2MwLjUtMC40LDEtMC44LDEuNS0xLjNsLTQuMSwxMC45SDEyM2w2LjItMTguOGM3LDIuMywxNC4zLDMuNSwyMS43LDMuNGM3LjIsMCwxNC4zLTEuMSwyMS4yLTMuMgoJCWw2LDE4LjZoNjAuMXYtMzloMTMuMWMzMS43LDAsNTAuNS0xNi4yLDUwLjUtNDMuMkMzMDEuNyw1Mi4yLDI4My41LDM4LjQsMjQ0LjcsMzguNHogTTE1MC45LDEyMWMtNC40LDAtOC44LTAuNy0xMy0yLjNsMTIuOS00MC42CgkJaDAuMmwxMi42LDQwLjdDMTU5LjYsMTIwLjMsMTU1LjIsMTIxLDE1MC45LDEyMXogTTI0Ny4xLDk3LjdoLTguOVY2NC45aDguOWMxMS45LDAsMjEuNCw0LDIxLjQsMTYuMQoJCUMyNjguNSw5My43LDI1OSw5Ny42LDI0Ny4xLDk3LjciLz4KPC9nPgo8L3N2Zz4K")
_png = cairosvg.svg2png(bytestring=_SVG, output_width=128, output_height=64)
_favicon = Image.open(io.BytesIO(_png))

st.set_page_config(
    page_title="US SMB Sales Tools",
    page_icon=_favicon,
    layout="wide",
)

# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    /* Remove default top padding so header sits flush */
    .block-container {
        padding-top: 0 !important;
        padding-bottom: 2rem !important;
        max-width: 100% !important;
    }
    /* Open app button */
    div[data-testid="stLinkButton"] a {
        background: #002A86 !important;
        color: #fff !important;
        border: none !important;
        border-radius: 3px !important;
        font-weight: 600 !important;
        font-size: 0.82rem !important;
        letter-spacing: 0.01em !important;
    }
    div[data-testid="stLinkButton"] a:hover {
        background: #1B90FF !important;
    }
    div[data-testid="stExpander"] {
        border: 1px solid #EAECEE !important;
        border-radius: 3px !important;
        background: #fff !important;
    }
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
# Uses CSS background-image (not an <img> tag) so it survives Streamlit's sanitiser
_LOGO_URI = "data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4KPCEtLSBHZW5lcmF0b3I6IEFkb2JlIElsbHVzdHJhdG9yIDI4LjMuMCwgU1ZHIEV4cG9ydCBQbHVnLUluIC4gU1ZHIFZlcnNpb246IDYuMDAgQnVpbGQgMCkgIC0tPgo8c3ZnIHZlcnNpb249IjEuMSIgaWQ9IkxheWVyXzEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9IjBweCIgeT0iMHB4IgoJIHZpZXdCb3g9IjAgMCA0MTIuNCAyMDQiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDQxMi40IDIwNDsiIHhtbDpzcGFjZT0icHJlc2VydmUiPgo8c3R5bGUgdHlwZT0idGV4dC9jc3MiPgoJLnN0MHtmaWxsLXJ1bGU6ZXZlbm9kZDtjbGlwLXJ1bGU6ZXZlbm9kZDtmaWxsOnVybCgjU1ZHSURfMV8pO30KCS5zdDF7ZmlsbC1ydWxlOmV2ZW5vZGQ7Y2xpcC1ydWxlOmV2ZW5vZGQ7ZmlsbDojRkZGRkZGO30KPC9zdHlsZT4KPGc+CgkKCQk8bGluZWFyR3JhZGllbnQgaWQ9IlNWR0lEXzFfIiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgeDE9IjIwNi4xOSIgeTE9IjIwNiIgeDI9IjIwNi4xOSIgeTI9IjIiIGdyYWRpZW50VHJhbnNmb3JtPSJtYXRyaXgoMSAwIDAgLTEgMCAyMDYpIj4KCQk8c3RvcCAgb2Zmc2V0PSIwIiBzdHlsZT0ic3RvcC1jb2xvcjojMDBCOEYxIi8+CgkJPHN0b3AgIG9mZnNldD0iMi4wMDAwMDBlLTAyIiBzdHlsZT0ic3RvcC1jb2xvcjojMDFCNkYwIi8+CgkJPHN0b3AgIG9mZnNldD0iMC4zMSIgc3R5bGU9InN0b3AtY29sb3I6IzBEOTBEOSIvPgoJCTxzdG9wICBvZmZzZXQ9IjAuNTgiIHN0eWxlPSJzdG9wLWNvbG9yOiMxNzc1QzgiLz4KCQk8c3RvcCAgb2Zmc2V0PSIwLjgyIiBzdHlsZT0ic3RvcC1jb2xvcjojMUM2NUJGIi8+CgkJPHN0b3AgIG9mZnNldD0iMSIgc3R5bGU9InN0b3AtY29sb3I6IzFFNUZCQiIvPgoJPC9saW5lYXJHcmFkaWVudD4KCTxwb2x5bGluZSBjbGFzcz0ic3QwIiBwb2ludHM9IjAsMjA0IDIwOC40LDIwNCA0MTIuNCwwIDAsMCAwLDIwNCAJIi8+Cgk8cGF0aCBjbGFzcz0ic3QxIiBkPSJNMjQ0LjcsMzguNGgtNDAuNnY5Ni41bC0zNS41LTk2LjZoLTM1LjJsLTMwLjMsODAuN0MxMDAsOTguNyw3OSw5MS43LDYyLjQsODYuNEM1MS41LDgyLjksMzkuOCw3Ny43LDQwLDcyCgkJYzAuMS00LjcsNi4yLTksMTguNC04LjRjOC4yLDAuNCwxNS40LDEuMSwyOS43LDhsMTQuMS0yNC41Yy0xMy4xLTYuNi0zMS4yLTEwLjktNDYtMTAuOWgtMC4xYy0xNy4zLDAtMzEuNyw1LjYtNDAuNiwxNC44CgkJYy02LjIsNi4zLTkuNywxNC44LTkuNywyMy43QzUuNSw4Ny4yLDEwLjEsOTYsMTkuNywxMDNjOC4xLDUuOSwxOC41LDkuOCwyNy42LDEyLjZjMTEuMywzLjUsMjAuNSw2LjUsMjAuNCwxMwoJCWMtMC4xLDIuNC0xLDQuNy0yLjcsNi40Yy0yLjgsMi45LTcuMSw0LTEzLjEsNC4xYy0xMS41LDAuMi0yMC0xLjYtMzMuNi05LjZMNS44LDE1NC40YzE0LDgsMjkuOSwxMi4yLDQ2LDEyLjJoMi4xCgkJYzE0LjItMC4yLDI1LjctNC4zLDM0LjktMTEuN2MwLjUtMC40LDEtMC44LDEuNS0xLjNsLTQuMSwxMC45SDEyM2w2LjItMTguOGM3LDIuMywxNC4zLDMuNSwyMS43LDMuNGM3LjIsMCwxNC4zLTEuMSwyMS4yLTMuMgoJCWw2LDE4LjZoNjAuMXYtMzloMTMuMWMzMS43LDAsNTAuNS0xNi4yLDUwLjUtNDMuMkMzMDEuNyw1Mi4yLDI4My41LDM4LjQsMjQ0LjcsMzguNHogTTE1MC45LDEyMWMtNC40LDAtOC44LTAuNy0xMy0yLjNsMTIuOS00MC42CgkJaDAuMmwxMi42LDQwLjdDMTU5LjYsMTIwLjMsMTU1LjIsMTIxLDE1MC45LDEyMXogTTI0Ny4xLDk3LjdoLTguOVY2NC45aDguOWMxMS45LDAsMjEuNCw0LDIxLjQsMTYuMQoJCUMyNjguNSw5My43LDI1OSw5Ny42LDI0Ny4xLDk3LjciLz4KPC9nPgo8L3N2Zz4K"

st.markdown(
    f'<div style="background:#002A86;padding:14px 28px;margin-bottom:20px;">' +
    f'<span style="background-image:url({_LOGO_URI});' +
    'background-repeat:no-repeat;background-size:contain;' +
    'display:inline-block;width:68px;height:28px;vertical-align:middle;"></span>' +
    '<span style="width:1px;height:24px;background:rgba(255,255,255,0.3);' +
    'display:inline-block;vertical-align:middle;margin:0 12px;"></span>' +
    '<span style="color:#ffffff;font-size:1rem;font-weight:700;' +
    'font-family:Arial,sans-serif;vertical-align:middle;">US SMB Sales Tools</span>' +
    '<span style="color:#89D1FF;font-size:0.78rem;float:right;' +
    'font-family:Arial,sans-serif;line-height:28px;">GTM Operations</span>' +
    '</div>',
    unsafe_allow_html=True)

# ── Session ID how-to ─────────────────────────────────────────────────────────
def _sid():
    steps = [
        "Open Salesforce in your browser and make sure you are fully logged in.",
        ("Open developer tools using <strong>either</strong> method:<br>"
         "&nbsp;&nbsp;&#8226; Press <strong>F12</strong> on your keyboard<br>"
         "&nbsp;&nbsp;&#8226; <strong>Right-click</strong> anywhere on the page "
         "&rarr; <strong>Inspect</strong> or <strong>Inspect Element</strong>"),
        "Click the <strong>Application</strong> tab (Chrome / Edge) or "
        "<strong>Storage</strong> tab (Firefox).",
        "In the left panel expand <strong>Cookies</strong> and click the Salesforce domain.",
        "Find the cookie named <code>sid</code> and copy the full value.",
        "Paste it into the <strong>Session ID</strong> field in the app and click Connect.",
    ]
    note = ("Your session ID expires on logout or after inactivity. "
            "If the app stops working, refresh Salesforce and grab a fresh one.")
    out = ('<p style="font-size:0.72rem;font-weight:700;color:#002A86;' +
           'text-transform:uppercase;letter-spacing:0.08em;' +
           'border-top:1px solid #EAECEE;padding-top:0.7rem;margin-top:0.9rem;">' +
           '&#128273;&nbsp; Getting your Salesforce Session ID</p>')
    for i, s in enumerate(steps, 1):
        out += (f'<div style="display:flex;gap:0.55rem;margin-bottom:0.45rem;align-items:flex-start;">' +
                f'<div style="min-width:19px;height:19px;border-radius:50%;' +
                f'background:#002A86;color:#fff;font-size:0.65rem;font-weight:700;' +
                f'display:flex;align-items:center;justify-content:center;flex-shrink:0;' +
                f'margin-top:1px;">{i}</div>' +
                f'<div style="font-size:0.81rem;color:#333;line-height:1.45;">{s}</div></div>')
    out += ('<div style="background:#D1EFFF;border-left:3px solid #1B90FF;' +
            f'border-radius:2px;padding:0.45rem 0.7rem;' +
            f'font-size:0.78rem;color:#002A86;margin-top:0.4rem;">&#128161; {note}</div>')
    return out

# ── App registry ──────────────────────────────────────────────────────────────
APPS = [
    {
        "name": "Performance Dashboard \u2014 US SMB",
        "description": "Track your attainment against plan in real time. Breaks down your total quota credit into its individual components \u2014 Closed-Won ARR, LTC Incentive, Retention Incentive, and Complete Incentive \u2014 so you can see exactly where you stand and where to focus.",
        "url": "https://smb-client-sales-performance-dashboard-fnbeugwlcwmxwvtgwneup3.streamlit.app/",
        "tags": ["Performance", "Quota", "Salesforce"],
        "audience": "All", "uses_sf": True,
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
        "audience": "All", "uses_sf": True,
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
        "audience": "All", "uses_sf": True,
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
        "audience": "All", "uses_sf": True,
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
        "audience": "Leaders", "uses_sf": False,
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

# ── Subtitle + filter ─────────────────────────────────────────────────────────
st.markdown(
    "<p style='color:#555;font-size:0.88rem;margin:0 0 1.2rem 0'>"
    "All your Salesforce-connected tools in one place. "
    "Click <strong>Open app</strong> on any card to launch it in a new tab.</p>",
    unsafe_allow_html=True)

st.markdown(
    "<p style='font-size:0.7rem;font-weight:700;color:#002A86;' +"
    "'text-transform:uppercase;letter-spacing:0.1em;margin:0 0 0.4rem 0'>"
    "Filter by audience</p>",
    unsafe_allow_html=True)

audience_filter = st.segmented_control(
    label="filter", label_visibility="collapsed",
    options=["All Users", "Leaders only", "Reps only"],
    default="All Users",
)
_map     = {"All Users": None, "Leaders only": "Leaders", "Reps only": "Reps"}
selected = _map[audience_filter]
filtered = [a for a in APPS if selected is None or a["audience"] in (selected, "All")]

st.markdown(
    f"<p style='color:#999;font-size:0.78rem;margin:0.4rem 0 1.2rem 0'>"
    f"{len(filtered)} app{'s' if len(filtered) != 1 else ''}</p>",
    unsafe_allow_html=True)

# ── Cards ─────────────────────────────────────────────────────────────────────
for batch in [filtered[i:i+3] for i in range(0, len(filtered), 3)]:
    cols = st.columns(3, gap="medium")
    for col, app in zip(cols, batch):
        with col:
            tags = "".join(
                f'<span style="display:inline-block;background:#D1EFFF;color:#002A86;' +
                f'border-radius:2px;font-size:0.67rem;font-weight:700;' +
                f'padding:2px 7px;margin-right:4px;' +
                f'text-transform:uppercase;letter-spacing:0.04em;">{t}</span>'
                for t in app["tags"]
            )
            ab, ac, al = (AUD_BG[app["audience"]], AUD_COLOR[app["audience"]],
                          AUD_LABEL[app["audience"]])
            st.markdown(
                f'<div style="background:#fff;border:1px solid #EAECEE;' +
                f'border-top:3px solid #1B90FF;border-radius:4px;' +
                f'padding:1.1rem 1.3rem 0.9rem;' +
                f'box-shadow:0 1px 4px rgba(0,42,134,0.06);margin-bottom:0.3rem;">' +
                f'<span style="float:right;font-size:0.67rem;font-weight:700;' +
                f'padding:2px 8px;border-radius:2px;background:{ab};' +
                f'color:{ac};text-transform:uppercase;letter-spacing:0.04em;">{al}</span>' +
                f'<p style="color:#002A86;font-size:0.95rem;font-weight:700;' +
                f'margin:0 0 0.45rem;font-family:Arial,sans-serif;">{app["name"]}</p>' +
                f'<p style="color:#444;font-size:0.83rem;line-height:1.5;' +
                f'margin:0 0 0.75rem;">{app["description"]}</p>{tags}</div>',
                unsafe_allow_html=True)

            st.link_button("Open app \u2192", app["url"], use_container_width=True)

            with st.expander("How to use this app"):
                html = ""
                for n, step in enumerate(app["how_to"], 1):
                    html += (
                        f'<div style="display:flex;gap:0.55rem;margin-bottom:0.45rem;' +
                        f'align-items:flex-start;">' +
                        f'<div style="min-width:19px;height:19px;border-radius:50%;' +
                        f'background:#002A86;color:#fff;font-size:0.65rem;font-weight:700;' +
                        f'display:flex;align-items:center;justify-content:center;' +
                        f'flex-shrink:0;margin-top:1px;">{n}</div>' +
                        f'<div style="font-size:0.81rem;color:#333;line-height:1.45;">{step}</div></div>'
                    )
                if app["uses_sf"]:
                    html += _sid()
                st.markdown(html, unsafe_allow_html=True)
    st.markdown("")

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown(
    '<div style="text-align:center;color:#aaa;font-size:0.75rem;' +
    'padding:1.5rem 0 0.5rem;border-top:1px solid #EAECEE;margin-top:0.5rem;">' +
    'SAP SE &nbsp;&middot;&nbsp; GTM Operations &nbsp;&middot;&nbsp;' +
    ' Questions? Contact your GTM Ops rep</div>',
    unsafe_allow_html=True)
