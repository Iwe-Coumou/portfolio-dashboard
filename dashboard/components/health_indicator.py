from dashboard.services.api import get_health
import streamlit as st
import time

_HEALTH_COOLDOWN = 20

@st.fragment(run_every=_HEALTH_COOLDOWN)
def render_health_indicator():
    last = st.session_state.get("last_health_check", 0)
    if time.time() - last < _HEALTH_COOLDOWN:
        return
    st.session_state["last_health_check"] = time.time()
    health = get_health()

    if not health["reachable"] or health["status_code"] == 503:
        st.session_state["api_down"] = True
        st.error("API unavailable")
    elif health["data"].get("status") == "degraded":
        st.session_state["api_down"] = False
        failed = [s for s, state in health["data"].get("services", {}).items() if state != "ok"]
        st.warning(f"Degraded: {', '.join(failed)}")
    else:
        st.session_state["api_down"] = False
        st.caption("API: operational")


def check_api_or_stop():
    if "api_down" not in st.session_state:
        health = get_health()
        st.session_state["api_down"] = not health["reachable"] or health["status_code"] == 503

    if st.session_state["api_down"]:
        st.error("API is unavailable. Start the backend and refresh.")
        st.stop()
