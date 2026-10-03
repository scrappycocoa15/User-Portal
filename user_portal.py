
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
