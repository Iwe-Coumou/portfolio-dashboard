from dashboard.services.api import sync
import streamlit as st

def render_sync_button():
    with st.sidebar:
        if st.button("Sync"):
            try:
                with st.spinner("Syncing backend..."):
                    sync_response = sync()
                st.toast(sync_response["message"], icon="✅")
            except Exception as e:
                st.error(str(e).splitlines()[0])
            