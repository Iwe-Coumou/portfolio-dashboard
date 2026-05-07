from dashboard.services.api import sync
import streamlit as st

def render_sync_button():
    with st.sidebar:
        if st.button("Sync"):
            try:
                with st.spinner("Syncing backend..."):
                    sync_response = sync()
                st.session_state['sync_response'] = sync_response
            except Exception as e:
                st.error(str(e).splitlines()[0])
        elif st.session_state.get('sync_response'):
            st.write(st.session_state["sync_response"])
            