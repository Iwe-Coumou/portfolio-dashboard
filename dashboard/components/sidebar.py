from dashboard.components.portfolio_selector import render_portfolio_selector
from dashboard.components.sync_button import render_sync_button
from dashboard.components.health_indicator import render_health_indicator
import streamlit as st


def render_sidebar():
    with st.sidebar:
        render_health_indicator()
        render_portfolio_selector()
        render_sync_button()