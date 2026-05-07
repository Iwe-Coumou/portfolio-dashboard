from dashboard.components.sidebar import render_sidebar
from dashboard.components.health_indicator import check_api_or_stop
import streamlit as st

check_api_or_stop()
render_sidebar()

if not st.session_state.get("lock_portfolios") or not st.session_state.get("selected_portfolios"):
    st.info("Select and lock portfolios on the Overview page to continue.")
    st.stop()
