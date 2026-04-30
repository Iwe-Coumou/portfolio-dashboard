from dashboard.services.api import get_portfolios, get_kpis
import streamlit as st


def render_portfolio_selector():
    portfolios = get_portfolios()
    lookup = {f"{p['name']}@{p['source']}": p for p in portfolios}

    locked = st.session_state.get("lock_portfolios", False)

    with st.sidebar:
        locked = st.toggle("Lock selection", value=locked)
        st.session_state["lock_portfolios"] = locked

        if locked:
            for p in st.session_state.get("selected_portfolios", []):
                st.caption(f"{p['name']}@{p['source']}")
        else:
            current = [
                f"{p['name']}@{p['source']}"
                for p in st.session_state.get("selected_portfolios", [])
            ]
            selected_keys = st.multiselect("Portfolios", options=sorted(lookup), default=current)
            selected_portfolios = [lookup[k] for k in selected_keys]
            st.session_state["selected_portfolios"] = selected_portfolios
            st.session_state["kpis"] = get_kpis(
                tuple({p["name"] for p in selected_portfolios}),
                tuple({p["source"] for p in selected_portfolios}),
            )
