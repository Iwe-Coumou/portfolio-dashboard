from dashboard.components.portfolio_selector import render_portfolio_selector
import streamlit as st

render_portfolio_selector()

if not st.session_state.get("lock_portfolios") or not st.session_state.get("selected_portfolios"):
    st.info("Select and lock portfolios on the Overview page to continue.")
    st.stop()
