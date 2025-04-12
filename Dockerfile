FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential=12.9 \
    curl=7.88.1-10+deb12u12 \
    && rm -rf /var/lib/apt/lists/*

ENV OTEL_SDK_DISABLED=true
ENV MODEL=ollama/llama3.1
ENV API_BASE=http://localhost:11434

COPY . /app
WORKDIR /app

RUN uv sync --frozen

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

RUN useradd -m appuser
USER appuser

ENTRYPOINT ["/app/.venv/bin/streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
