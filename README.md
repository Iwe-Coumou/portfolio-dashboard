# Finance Dashboard

A portfolio analytics dashboard built with Streamlit, powered by the [Finance API](https://github.com/Iwe-Coumou/finance-backend).

## Overview

Three page dashboard for portfolio monitoring, factor analysis, and portfolio optimization.

---

## Pages

### Page 1 — Portfolio Overview
A fixed single-page dashboard for daily monitoring.

- KPIs: total return, volatility, Sharpe ratio, Sortino ratio, expected return
- Portfolio return chart vs benchmark
- Max drawdown and max drawdown period
- Asset weights and allocation overview
- Factor exposure summary
- Monte Carlo simulation results

### Page 2 — Drift & Rebalancing
Scrollable analytical view for periodic portfolio review.

- Factor drift visualization — current exposure vs target
- Per-asset factor contribution to drift
- Traffic light indicator per factor (green/yellow/red)
- Historical drift over time
- Rebalancing check — can current assets fix the drift?
- Estimated rebalancing cost

### Page 3 — Portfolio Builder
Scrollable workflow page for simulating portfolio changes. Uses session state to persist a working portfolio across steps.

**Step 1 — Remove**
- Select assets to remove from current portfolio
- See portfolio metrics without removed assets
- Confirm to update working portfolio

**Step 2 — Screen & Add**
- Factor gap of working portfolio drives screening criteria
- Run screener to find candidates that fill the gap
- See full factor profile per candidate
- Select candidate and set target weight
- See portfolio metrics with candidate added
- Confirm to update working portfolio

**Step 3 — Review & Execute**
- Side by side comparison: original vs proposed portfolio
- Factor exposure before vs after
- KPI comparison: Sharpe, Sortino, volatility, expected return
- Exact trades needed to reach proposed portfolio
- Reset session state when done

---

## Setup

### Requirements
- Python 3.12+
- Finance API running (see [finance-api](https://github.com/Iwe-Coumou/finance-backend))

### Installation
```bash
git clone https://github.com/username/finance-dashboard
cd finance-dashboard
uv sync
```

### Configuration
Create a `.env` file:
```
API_URL=http://localhost:8000
API_KEY=your-api-key-here
```

### Running
```bash
uv run streamlit run dashboard/main.py
```

---

## Architecture
```
Streamlit (dashboard) → FastAPI (finance-api) → TimescaleDB / Redis
```

The dashboard is a pure frontend — all data fetching and computation happens in the API. Streamlit only handles display and user interaction.
