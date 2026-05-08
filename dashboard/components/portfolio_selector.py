from dashboard.services.api import get_portfolios
import streamlit as st


def render_portfolio_selector():
    try:
        portfolios = get_portfolios()
    except Exception:
        st.sidebar.warning("Could not load portfolios.")
        return

    lookup = {f"{p['name']}@{p['source']}": p for p in portfolios}

    # Remove stale keys if portfolios changed
    valid_keys = [k for k in st.session_state.get("selected_portfolio_keys", []) if k in lookup]
    st.session_state["selected_portfolio_keys"] = valid_keys

    has_selection = bool(valid_keys)
    if not has_selection:
        st.session_state["lock_portfolios"] = False

    with st.sidebar:
        st.toggle("Lock selection", key="lock_portfolios", disabled=not has_selection)
        locked = st.session_state["lock_portfolios"]

        if locked:
            for key in valid_keys:
                p = lookup[key]
                st.caption(f"{p['name']}@{p['source']}")
        else:
            st.multiselect("Portfolios", options=sorted(lookup), key="selected_portfolio_keys")

    st.session_state["selected_portfolios"] = [
        lookup[k] for k in st.session_state.get("selected_portfolio_keys", []) if k in lookup
    ]
