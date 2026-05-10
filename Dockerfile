FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml uv.lock ./
COPY dashboard/ dashboard/

RUN uv sync --frozen --no-dev

EXPOSE 8501

CMD ["uv", "run", "streamlit", "run", "dashboard/main.py", \
    "--server.port=8501", "--server.address=0.0.0.0"]