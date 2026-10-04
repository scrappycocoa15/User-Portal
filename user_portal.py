"""
user_portal.py — US SMB Sales Tools Portal
SAP Classic Corporate branding.
"""
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="US SMB Sales Tools", page_icon="📊", layout="wide")

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

SAP_SVG = """<svg style="height:28px;width:auto;vertical-align:middle;" version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
	 viewBox="0 0 412.4 204" style="enable-background:new 0 0 412.4 204;" xml:space="preserve">
<style type="text/css">
	.st0{fill-rule:evenodd;clip-rule:evenodd;fill:url(#SVGID_1_);}
	.st1{fill-rule:evenodd;clip-rule:evenodd;fill:#FFFFFF;}
</style>
<g>
	
		<linearGradient id="SVGID_1_" gradientUnits="userSpaceOnUse" x1="206.19" y1="206" x2="206.19" y2="2" gradientTransform="matrix(1 0 0 -1 0 206)">
		<stop  offset="0" style="stop-color:#00B8F1"/>
		<stop  offset="2.000000e-02" style="stop-color:#01B6F0"/>
		<stop  offset="0.31" style="stop-color:#0D90D9"/>
		<stop  offset="0.58" style="stop-color:#1775C8"/>
		<stop  offset="0.82" style="stop-color:#1C65BF"/>
		<stop  offset="1" style="stop-color:#1E5FBB"/>
	</linearGradient>
	<polyline class="st0" points="0,204 208.4,204 412.4,0 0,0 0,204 	"/>
	<path class="st1" d="M244.7,38.4h-40.6v96.5l-35.5-96.6h-35.2l-30.3,80.7C100,98.7,79,91.7,62.4,86.4C51.5,82.9,39.8,77.7,40,72
		c0.1-4.7,6.2-9,18.4-8.4c8.2,0.4,15.4,1.1,29.7,8l14.1-24.5c-13.1-6.6-31.2-10.9-46-10.9h-0.1c-17.3,0-31.7,5.6-40.6,14.8
		c-6.2,6.3-9.7,14.8-9.7,23.7C5.5,87.2,10.1,96,19.7,103c8.1,5.9,18.5,9.8,27.6,12.6c11.3,3.5,20.5,6.5,20.4,13
		c-0.1,2.4-1,4.7-2.7,6.4c-2.8,2.9-7.1,4-13.1,4.1c-11.5,0.2-20-1.6-33.6-9.6L5.8,154.4c14,8,29.9,12.2,46,12.2h2.1
		c14.2-0.2,25.7-4.3,34.9-11.7c0.5-0.4,1-0.8,1.5-1.3l-4.1,10.9H123l6.2-18.8c7,2.3,14.3,3.5,21.7,3.4c7.2,0,14.3-1.1,21.2-3.2
		l6,18.6h60.1v-39h13.1c31.7,0,50.5-16.2,50.5-43.2C301.7,52.2,283.5,38.4,244.7,38.4z M150.9,121c-4.4,0-8.8-0.7-13-2.3l12.9-40.6
		h0.2l12.6,40.7C159.6,120.3,155.2,121,150.9,121z M247.1,97.7h-8.9V64.9h8.9c11.9,0,21.4,4,21.4,16.1
		C268.5,93.7,259,97.6,247.1,97.7"/>
</g>
</svg>"""

components.html(f"""
<!DOCTYPE html>
<html>
<body style="margin:0;padding:0;overflow:hidden;">
<div style="background:#002A86;padding:0.65rem 2rem;display:flex;
            align-items:center;gap:1rem;font-family:Arial,sans-serif;">
    {SAP_SVG}
    <div style="width:1px;height:26px;background:rgba(255,255,255,0.35);margin:0 0.2rem;"></div>
    <span style="color:#ffffff;font-size:1rem;font-weight:700;letter-spacing:0.01em;">
        US SMB Sales Tools
    </span>
    <span style="color:#89D1FF;font-size:0.8rem;margin-left:auto;">
        GTM Operations
    </span>
</div>
</body></html>
""", height=52, scrolling=False)

def session_id_html():
    steps = [
        "Open Salesforce in your browser and make sure you are fully logged in.",
        ("Open developer tools using <strong>either</strong> method:<br>"
         "&nbsp;&nbsp;&#8226; Press <strong>F12</strong> on your keyboard<br>"
         "&nbsp;&nbsp;&#8226; <strong>Right-click</strong> anywhere on the page "
         "&rarr; <strong>Inspect</strong> or <strong>Inspect Element</strong>"),
        "Click the <strong>Application</strong> tab (Chrome / Edge) or <strong>Storage</strong> tab (Firefox).",
        "In the left panel expand <strong>Cookies</strong> and click the Salesforce domain.",
        "Find the cookie named <code>sid</code> and copy the full value.",
        "Paste it into the <strong>Session ID</strong> field in the app and click Connect.",
    ]
    note = ("Your session ID expires on logout or after inactivity. "
            "If the app stops working, refresh Salesforce and grab a fresh one.")
    out = ('<p style="font-size:0.75rem;font-weight:700;color:#002A86;text-transform:uppercase;' +
           'letter-spacing:0.08em;border-top:1px solid #EAECEE;padding-top:0.7rem;margin-top:0.8rem;">' +
           '&#128273; Getting your Salesforce Session ID</p>')
    for idx, s in enumerate(steps, 1):
        out += ('<div style="display:flex;gap:0.6rem;margin-bottom:0.5rem;align-items:flex-start;">' +
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
                '<span style="display:inline-block;background:#D1EFFF;color:#002A86;' +
                'border-radius:2px;font-size:0.68rem;font-weight:700;padding:2px 7px;' +
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
                f'<p style="color:#002A86;font-size:0.95rem;font-weight:700;margin:0 0 0.45rem;">{app["name"]}</p>' +
                f'<p style="color:#444;font-size:0.83rem;line-height:1.5;margin:0 0 0.7rem;">{app["description"]}</p>' +
                f'{tags_html}</div>',
                unsafe_allow_html=True)

            st.link_button("Open app →", app["url"], use_container_width=True)

            with st.expander("How to use this app"):
                html = ""
                for step_num, step in enumerate(app["how_to"], 1):
                    html += (
                        '<div style="display:flex;gap:0.6rem;margin-bottom:0.5rem;align-items:flex-start;">' +
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
