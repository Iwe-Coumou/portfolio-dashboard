from collections import defaultdict
from dashboard.services.api import get_portfolios
import streamlit as st
import streamlit_antd_components as sac

portfolios = get_portfolios()  # [{"id": ..., "name": ..., "source": ...}]

by_source = defaultdict(list)
for p in portfolios:
    by_source[p["source"]].append(p)

items = [
    sac.CasItem(source, children=[sac.CasItem(p["name"]) for p in ps])
    for source, ps in by_source.items()
]

with st.sidebar:
    selected = sac.cascader(items, multiple=True, label="Portfolios", search=True, clear=True)

sources = set(by_source)
lookup = {(p["source"], p["name"]): p["id"] for p in portfolios}

selected_ids, src = [], None
for label in (selected or []):
    if label in sources:
        src = label
    elif src and (pid := lookup.get((src, label))):
        selected_ids.append(pid)

st.write(selected_ids)