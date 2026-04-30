import streamlit as st


def kpi_card(label: str, primary: str, secondary: str | None = None, delta: float | None = None):
    if delta is None:
        color = "inherit"
    elif delta > 0:
        color = "#22c55e"
    elif delta < 0:
        color = "#ef4444"
    else:
        color = "inherit"

    secondary_html = (
        f'<div style="font-size:0.8rem;color:{color};opacity:0.85;margin-top:4px">{secondary}</div>'
        if secondary else ""
    )

    st.markdown(f"""
    <div style="border:1px solid rgba(128,128,128,0.2);border-radius:0.5rem;padding:1rem;margin-bottom:0.5rem;min-height:5.5rem">
        <div style="font-size:0.75rem;opacity:0.55;margin-bottom:6px">{label}</div>
        <div style="font-size:1.4rem;font-weight:600;color:{color}">{primary}</div>
        {secondary_html}
    </div>
    """, unsafe_allow_html=True)
