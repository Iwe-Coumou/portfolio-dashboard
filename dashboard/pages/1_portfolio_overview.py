from dashboard.components.portfolio_selector import render_portfolio_selector
from dashboard.components.kpi_cards import kpi_card
import streamlit as st

render_portfolio_selector()

kpis = st.session_state.get("kpis", {})
if not kpis:
    st.stop()

c1, c2, c3, c4 = st.columns(4)

with c1:
    kpi_card("Portfolio Value", f"€{kpis['portfolio_value']:,.2f}")
with c2:
    kpi_card("Holdings", str(kpis["num_holdings"]))
with c3:
    kpi_card("Return", f"{kpis['pct_return']:.2%}", secondary=f"€{kpis['raw_return']:+,.2f}", delta=kpis['raw_return'])
with c4:
    kpi_card("YTD Return", f"{kpis['ytd_pct']:.2%}", secondary=f"€{kpis['ytd_raw']:+,.2f}", delta=kpis['ytd_raw'])

c5, c6, c7, c8 = st.columns(4)

with c5:
    kpi_card("Annualised Return", f"{kpis['annualized_return']:.2%}", delta=kpis['annualized_return'])
with c6:
    kpi_card("Volatility", f"{kpis['volatility']:.2%}")
with c7:
    kpi_card("Sharpe", f"{kpis['sharpe']:.2f}")
with c8:
    kpi_card("Sortino", f"{kpis['sortino']:.2f}")

c9, c10, c11 = st.columns(3)

with c9:
    kpi_card("Max Drawdown", f"{kpis['max_drawdown']:.2%}",
             secondary=f"{kpis['max_drawdown_start']} → {kpis['max_drawdown_end']}")
with c10:
    kpi_card("Beta", f"{kpis['beta']:.2f}")
with c11:
    kpi_card("vs Benchmark", f"{kpis['vs_benchmark']:+.2%}", delta=kpis['vs_benchmark'])
