from dashboard.logging import get_logger
from dashboard.config import get_env_var
import httpx
from functools import wraps
import streamlit as st
from pathlib import Path

@st.cache_resource
def _get_client() -> httpx.Client:
    return httpx.Client(
        base_url=get_env_var("API_URL"),
        headers={"X-API-Key": get_env_var("API_KEY")},
        timeout=30.0,
    )

  
def _get(endpoint: str, params: dict = None) -> dict:
    response = _get_client().get(f"{endpoint}", params=params)
    response.raise_for_status()
    return response.json()

def _post(endpoint: str, body: dict = None) -> dict:
    response = _get_client().post(endpoint, json=body)
    response.raise_for_status()
    return response.json()

@st.cache_data(ttl=300)
def get_weights(portfolio_name: str) -> dict:
    return _get(f"portfolios/{portfolio_name}/weights")

@st.cache_data(ttl=300)
def get_portfolios() -> dict:
    return _get(f"v1/portfolios/")

@st.cache_data(ttl=300)
def get_kpis(names: tuple[str, ...], sources: tuple[str, ...] = ()) -> dict:
    params = {}
    if names:
        params["name"] = list(names)
    if sources:
        params["source"] = list(sources)
    return _get("v1/portfolios/KPIs", params=params)
