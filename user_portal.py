"""
user_portal.py — US SMB Sales Tools Portal
SAP Classic Corporate branding.
"""
import streamlit as st

st.set_page_config(page_title="US SMB Sales Tools", page_icon="📊", layout="wide")

SAP_LOGO = "data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4KPCEtLSBHZW5lcmF0b3I6IEFkb2JlIElsbHVzdHJhdG9yIDI4LjMuMCwgU1ZHIEV4cG9ydCBQbHVnLUluIC4gU1ZHIFZlcnNpb246IDYuMDAgQnVpbGQgMCkgIC0tPgo8c3ZnIHZlcnNpb249IjEuMSIgaWQ9IkxheWVyXzEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9IjBweCIgeT0iMHB4IgoJIHZpZXdCb3g9IjAgMCA0MTIuNCAyMDQiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDQxMi40IDIwNDsiIHhtbDpzcGFjZT0icHJlc2VydmUiPgo8c3R5bGUgdHlwZT0idGV4dC9jc3MiPgoJLnN0MHtmaWxsLXJ1bGU6ZXZlbm9kZDtjbGlwLXJ1bGU6ZXZlbm9kZDtmaWxsOnVybCgjU1ZHSURfMV8pO30KCS5zdDF7ZmlsbC1ydWxlOmV2ZW5vZGQ7Y2xpcC1ydWxlOmV2ZW5vZGQ7ZmlsbDojRkZGRkZGO30KPC9zdHlsZT4KPGc+CgkKCQk8bGluZWFyR3JhZGllbnQgaWQ9IlNWR0lEXzFfIiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgeDE9IjIwNi4xOSIgeTE9IjIwNiIgeDI9IjIwNi4xOSIgeTI9IjIiIGdyYWRpZW50VHJhbnNmb3JtPSJtYXRyaXgoMSAwIDAgLTEgMCAyMDYpIj4KCQk8c3RvcCAgb2Zmc2V0PSIwIiBzdHlsZT0ic3RvcC1jb2xvcjojMDBCOEYxIi8+CgkJPHN0b3AgIG9mZnNldD0iMi4wMDAwMDBlLTAyIiBzdHlsZT0ic3RvcC1jb2xvcjojMDFCNkYwIi8+CgkJPHN0b3AgIG9mZnNldD0iMC4zMSIgc3R5bGU9InN0b3AtY29sb3I6IzBEOTBEOSIvPgoJCTxzdG9wICBvZmZzZXQ9IjAuNTgiIHN0eWxlPSJzdG9wLWNvbG9yOiMxNzc1QzgiLz4KCQk8c3RvcCAgb2Zmc2V0PSIwLjgyIiBzdHlsZT0ic3RvcC1jb2xvcjojMUM2NUJGIi8+CgkJPHN0b3AgIG9mZnNldD0iMSIgc3R5bGU9InN0b3AtY29sb3I6IzFFNUZCQiIvPgoJPC9saW5lYXJHcmFkaWVudD4KCTxwb2x5bGluZSBjbGFzcz0ic3QwIiBwb2ludHM9IjAsMjA0IDIwOC40LDIwNCA0MTIuNCwwIDAsMCAwLDIwNCAJIi8+Cgk8cGF0aCBjbGFzcz0ic3QxIiBkPSJNMjQ0LjcsMzguNGgtNDAuNnY5Ni41bC0zNS41LTk2LjZoLTM1LjJsLTMwLjMsODAuN0MxMDAsOTguNyw3OSw5MS43LDYyLjQsODYuNEM1MS41LDgyLjksMzkuOCw3Ny43LDQwLDcyCgkJYzAuMS00LjcsNi4yLTksMTguNC04LjRjOC4yLDAuNCwxNS40LDEuMSwyOS43LDhsMTQuMS0yNC41Yy0xMy4xLTYuNi0zMS4yLTEwLjktNDYtMTAuOWgtMC4xYy0xNy4zLDAtMzEuNyw1LjYtNDAuNiwxNC44CgkJYy02LjIsNi4zLTkuNywxNC44LTkuNywyMy43QzUuNSw4Ny4yLDEwLjEsOTYsMTkuNywxMDNjOC4xLDUuOSwxOC41LDkuOCwyNy42LDEyLjZjMTEuMywzLjUsMjAuNSw2LjUsMjAuNCwxMwoJCWMtMC4xLDIuNC0xLDQuNy0yLjcsNi40Yy0yLjgsMi45LTcuMSw0LTEzLjEsNC4xYy0xMS41LDAuMi0yMC0xLjYtMzMuNi05LjZMNS44LDE1NC40YzE0LDgsMjkuOSwxMi4yLDQ2LDEyLjJoMi4xCgkJYzE0LjItMC4yLDI1LjctNC4zLDM0LjktMTEuN2MwLjUtMC40LDEtMC44LDEuNS0xLjNsLTQuMSwxMC45SDEyM2w2LjItMTguOGM3LDIuMywxNC4zLDMuNSwyMS43LDMuNGM3LjIsMCwxNC4zLTEuMSwyMS4yLTMuMgoJCWw2LDE4LjZoNjAuMXYtMzloMTMuMWMzMS43LDAsNTAuNS0xNi4yLDUwLjUtNDMuMkMzMDEuNyw1Mi4yLDI4My41LDM4LjQsMjQ0LjcsMzguNHogTTE1MC45LDEyMWMtNC40LDAtOC44LTAuNy0xMy0yLjNsMTIuOS00MC42CgkJaDAuMmwxMi42LDQwLjdDMTU5LjYsMTIwLjMsMTU1LjIsMTIxLDE1MC45LDEyMXogTTI0Ny4xLDk3LjdoLTguOVY2NC45aDguOWMxMS45LDAsMjEuNCw0LDIxLjQsMTYuMQoJCUMyNjguNSw5My43LDI1OSw5Ny42LDI0Ny4xLDk3LjciLz4KPC9nPgo8L3N2Zz4K"


st.markdown("""
<style>
    .block-container { padding-top:0 !important; padding-bottom:2rem !important; max-width:100% !important; }
    div[data-testid="stLinkButton"] a {
        background:#002A86 !important; color:#fff !important; border:none !important;
        border-radius:3px !important; font-weight:600 !important; font-size:0.82rem !important;
    }
    div[data-testid="stLinkButton"] a:hover { background:#1B90FF !important; }
    div[data-testid="stExpander"] { border:1px solid #EAECEE !important; border-radius:3px !important; }
</style>
""", unsafe_allow_html=True)

st.markdown(
    f'''<div style="background:#002A86;padding:0.75rem 2.5rem;display:flex;
                    align-items:center;gap:1.1rem;margin-bottom:1.5rem;width:100%;">
        <img src="{SAP_LOGO}" style="height:26px;width:auto;" />
        <div style="width:1px;height:26px;background:rgba(255,255,255,0.35);"></div>
        <span style="color:#fff;font-size:1rem;font-weight:700;font-family:Arial,sans-serif;">
            US SMB Sales Tools</span>
        <span style="color:#89D1FF;font-size:0.8rem;margin-left:auto;font-family:Arial,sans-serif;">
            GTM Operations</span>
    </div>''',
    unsafe_allow_html=True)

def session_id_html():
    steps = [
        "Open Salesforce in your browser and make sure you are fully logged in.",
        "Open developer tools using <strong>either</strong> method:<br>"
        "&nbsp;&nbsp;&#8226; Press <strong>F12</strong> on your keyboard<br>"
        "&nbsp;&nbsp;&#8226; <strong>Right-click</strong> anywhere on the page "
        "&rarr; <strong>Inspect</strong> or <strong>Inspect Element</strong>",
        "Click the <strong>Application</strong> tab (Chrome/Edge) or "
        "<strong>Storage</strong> tab (Firefox).",
        "In the left panel expand <strong>Cookies</strong> and click the Salesforce domain.",
        "Find the cookie named <code>sid</code> and copy its full value.",
        "Paste it into the <strong>Session ID</strong> field in the app and click Connect.",
    ]
    note = ("Your session ID expires on logout or after inactivity. "
            "If the app stops working, refresh Salesforce and grab a new one.")
    out = ('<p style="font-size:0.75rem;font-weight:700;color:#002A86;text-transform:uppercase;' +
           'letter-spacing:0.08em;border-top:1px solid #EAECEE;padding-top:0.7rem;margin-top:0.8rem;">' +
           '&#128273; Getting your Salesforce Session ID</p>')
    for idx, s in enumerate(steps, 1):
        out += (f'<div style="display:flex;gap:0.6rem;margin-bottom:0.5rem;align-items:flex-start;">' +
                f'<div style="background:#002A86;color:#fff;font-size:0.68rem;font-weight:700;' +
                f'min-width:20px;height:20px;border-radius:50%;display:flex;' +
                f'align-items:center;justify-content:center;flex-shrink:0;margin-top:1px;">{idx}</div>' +
                f'<div style="font-size:0.82rem;color:#333;line-height:1.45;">{s}</div></div>')
    out += ('<div style="background:#D1EFFF;border-left:3px solid #1B90FF;border-radius:2px;' +
            f'padding:0.5rem 0.75rem;font-size:0.8rem;color:#002A86;margin-top:0.5rem;">&#128161; {note}</div>')
    return out


APPS = [
    {
        "name": "Performance Dashboard — US SMB",
        "description": "Track your attainment against plan in real time. Breaks down your total quota credit into its individual components — Closed-Won ARR, LTC Incentive, Retention Incentive, and Complete Incentive — so you can see exactly where you stand and where to focus.",
        "url": "https://smb-client-sales-performance-dashboard-fnbeugwlcwmxwvtgwneup3.streamlit.app/",
        "tags": ["Performance", "Quota", "Salesforce"],
        "audience": "All",
        "uses_sf": True,
        "how_to": [
            "Enter your Salesforce Session ID when prompted (instructions below).",
            "Select your name from the rep dropdown, or a team/segment view if you are a leader.",
            "Your YTD attainment and component breakdown load automatically.",
            "Use the date range filter to view performance for a specific period.",
            "Hover over each bar in the component chart for exact CW ARR, LTC, Retention, and Complete amounts.",
        ],
    },
    {
        "name": "Performance Dashboard — Global SMB",
        "description": "Same quota attainment and component breakdown as the US dashboard — Closed-Won ARR, LTC, Retention, and Complete Incentives — built for the UK, Australia, and Canada SMB teams.",
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
        "name": "Watermark Dashboard — US SMB",
        "description": "See all accounts in your book with an active watermark deficit. Shows the deficit amount, the date it went into effect, and when it expires — so you're never caught off guard on a renewal or expansion deal.",
        "url": "https://smb-watermark-tool-usclientsales.streamlit.app/",
        "tags": ["Accounts", "Watermark", "Salesforce"],
        "audience": "All",
        "uses_sf": True,
        "how_to": [
            "Enter your Salesforce Session ID when prompted (instructions below).",
            "Your active watermark accounts load automatically — no additional filters needed.",
            "Each row shows account name, deficit amount, effective date, and expiry date.",
            "Accounts expiring within 30 days are highlighted — prioritise those for renewal conversations.",
            "Export the list as CSV using the download button at the top of the table.",
        ],
    },
    {
        "name": "Watermark Dashboard — Global SMB",
        "description": "Same watermark visibility as the US tool — active deficits, effective dates, and expiry dates — built for the UK, Australia, and Canada SMB teams.",
        "url": "https://watermark-appglobal-smb.streamlit.app/",
        "tags": ["Accounts", "Watermark", "Global"],
        "audience": "All",
        "uses_sf": True,
        "how_to": [
            "Enter your Salesforce Session ID when prompted (instructions below).",
            "Select your region (UK, Australia, or Canada).",
            "Your active watermark accounts load — each row shows deficit, effective date, and expiry.",
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
            "Open the app — no Salesforce login required.",
            "Paste the Salesforce URL for the consolidating account and the opportunity to be split.",
            "Enter the expense transaction amounts for each entity.",
            "Review the calculated credit percentage per rep — adjust values if needed.",
            "Click Submit — this sends an email to Field Services and logs the submission in your history.",
        ],
    },
]

AUD_BG    = {"All": "#D1EFFF", "Leaders": "#FFF3CD", "Reps": "#E6F4EA"}
AUD_COLOR = {"All": "#002A86", "Leaders": "#7A5800", "Reps": "#1B6B3A"}
AUD_LABEL = {"All": "All Users", "Leaders": "Leaders Only", "Reps": "Reps Only"}

st.markdown(
    "<p style='color:#555;font-size:0.88rem;margin:0 0 1rem 0'>"
    "All your Salesforce-connected tools in one place. "
    "Click <strong>Open app</strong> on any card to launch it in a new tab.</p>",
    unsafe_allow_html=True)

st.markdown(
    "<p style='font-size:0.7rem;font-weight:700;color:#002A86;text-transform:uppercase;"
    "letter-spacing:0.1em;margin:0 0 0.4rem 0'>Filter by audience</p>",
    unsafe_allow_html=True)

audience_filter = st.segmented_control(
    label="filter", label_visibility="collapsed",
    options=["All Users", "Leaders only", "Reps only"], default="All Users",
)
filter_map = {"All Users": None, "Leaders only": "Leaders", "Reps only": "Reps"}
selected   = filter_map[audience_filter]
filtered   = [a for a in APPS if selected is None or a["audience"] in (selected, "All")]

st.markdown(
    f"<p style='color:#999;font-size:0.78rem;margin:0.4rem 0 1rem 0'>"
    f"{len(filtered)} app{'s' if len(filtered) != 1 else ''}</p>",
    unsafe_allow_html=True)

COLS = 3
for row_apps in [filtered[i:i+COLS] for i in range(0, len(filtered), COLS)]:
    columns = st.columns(COLS, gap="medium")
    for col, app in zip(columns, row_apps):
        with col:
            tags_html = "".join(
                f'<span style="display:inline-block;background:#D1EFFF;color:#002A86;' +
                f'border-radius:2px;font-size:0.68rem;font-weight:700;padding:2px 7px;' +
                f'margin-right:4px;text-transform:uppercase;letter-spacing:0.04em;">{t}</span>'
                for t in app["tags"]
            )
            ab   = AUD_BG.get(app["audience"], "#eee")
            ac   = AUD_COLOR.get(app["audience"], "#333")
            albl = AUD_LABEL.get(app["audience"], app["audience"])
            st.markdown(
                f'<div style="background:#fff;border:1px solid #EAECEE;border-top:3px solid #1B90FF;' +
                f'border-radius:4px;padding:1.1rem 1.3rem 0.9rem;' +
                f'box-shadow:0 1px 3px rgba(0,42,134,0.07);margin-bottom:0.3rem;">' +
                f'<span style="float:right;font-size:0.68rem;font-weight:700;padding:2px 8px;' +
                f'border-radius:2px;background:{ab};color:{ac};' +
                f'text-transform:uppercase;letter-spacing:0.04em;">{albl}</span>' +
                f'<p style="color:#002A86;font-size:0.95rem;font-weight:700;margin:0 0 0.45rem;">' +
                f'{app["name"]}</p>' +
                f'<p style="color:#444;font-size:0.83rem;line-height:1.5;margin:0 0 0.7rem;">' +
                f'{app["description"]}</p>{tags_html}</div>',
                unsafe_allow_html=True)

            st.link_button("Open app →", app["url"], use_container_width=True)

            with st.expander("How to use this app"):
                html = ""
                for step_num, step in enumerate(app["how_to"], 1):
                    html += (
                        f'<div style="display:flex;gap:0.6rem;margin-bottom:0.5rem;align-items:flex-start;">' +
                        f'<div style="background:#002A86;color:#fff;font-size:0.68rem;font-weight:700;' +
                        f'min-width:20px;height:20px;border-radius:50%;display:flex;' +
                        f'align-items:center;justify-content:center;flex-shrink:0;margin-top:1px;">{step_num}</div>' +
                        f'<div style="font-size:0.82rem;color:#333;line-height:1.45;">{step}</div></div>'
                    )
                if app["uses_sf"]:
                    html += session_id_html()
                st.markdown(html, unsafe_allow_html=True)
    st.markdown("")

st.markdown(
    '<div style="text-align:center;color:#999;font-size:0.75rem;' +
    'padding:1.5rem 0 1rem;border-top:1px solid #EAECEE;margin-top:1rem;">' +
    'SAP SE &nbsp;&middot;&nbsp; GTM Operations &nbsp;&middot;&nbsp; ' +
    'Questions? Contact your GTM Ops rep</div>',
    unsafe_allow_html=True)
