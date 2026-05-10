FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

RUN pip install uv

COPY pyproject.toml uv.lock README.md ./
COPY dashboard/ dashboard/

RUN uv sync --frozen --no-dev --no-install-project

EXPOSE 8501

CMD ["uv", "run", "streamlit", "run", "dashboard/main.py", \
    "--server.port=8501", "--server.address=0.0.0.0"]