from dashboard.components.portfolio_selector import render_portfolio_selector
import streamlit as st
import streamlit_antd_components as sac

render_portfolio_selector()

if not st.session_state.get("lock_portfolios") or not st.session_state.get("selected_portfolios"):
    st.info("Select and lock portfolios on the Overview page to continue.")
    st.stop()

selected_portfolios = st.session_state["selected_portfolios"]
selection_key = tuple(sorted(p["id"] for p in selected_portfolios))
if st.session_state.get("_p3_selection") != selection_key:
    st.session_state["_p3_selection"] = selection_key
    st.session_state.unlocked = 0
    st.session_state.pop("steps", None)

st.markdown("""<style>
.block-container { padding-top: 2rem; padding-bottom: 1rem; }
</style>""", unsafe_allow_html=True)

if "unlocked" not in st.session_state:
    st.session_state.unlocked = 0

step = sac.steps([
    sac.StepsItem("Remove Asset"),
    sac.StepsItem("Add Asset", disabled=st.session_state.unlocked < 1),
    sac.StepsItem("Review & Execute", disabled=st.session_state.unlocked < 2),
], variant="navigation", return_index=True, key="steps")

def next_step(n):
    st.session_state.unlocked = max(st.session_state.unlocked, n)
    st.session_state["steps"] = n

col1, _, col2 = st.columns([2, 6, 2])

if step == 0:
    st.write("Step 1: Remove Asset")
    col2.button("Next", on_click=next_step, args=(1,), use_container_width=True)

elif step == 1:
    st.write("Step 2: Add Asset")
    col1.button("Previous", on_click=next_step, args=(0,), use_container_width=True)
    col2.button("Next", on_click=next_step, args=(2,), use_container_width=True)

elif step == 2:
    st.write("Step 3: Review & Execute")
    col1.button("Previous", on_click=next_step, args=(1,), use_container_width=True)
