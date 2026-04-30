# dashboard/main.py
import streamlit as st
import httpx
from dashboard.services.api import _get

st.set_page_config(layout="wide", page_title="Portfolio Dashboard", page_icon="📈")

st.title("API Explorer")

endpoint = st.text_input("Endpoint", value="v1/")

if st.button("Run"):
    with st.spinner("Fetching from API..."):
        try:
            result = _get(endpoint)
            st.json(result)
        except httpx.HTTPStatusError as e:
            body = e.response.json() if "application/json" in e.response.headers.get("content-type", "") else {}
            detail = body.get("detail", e.response.text)
            st.error(f"{e.response.status_code}: {detail}")
        except Exception as e:
            st.error(str(e))