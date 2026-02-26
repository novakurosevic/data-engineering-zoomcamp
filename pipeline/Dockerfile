# FROM python:3.13.11-slim

# # Copy uv binary from official uv image (multi-stage build pattern)
# COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

# WORKDIR /code
# ENV PATH="/code/.venv/bin:$PATH"

# COPY pyproject.toml .python-version uv.lock ./
# RUN uv sync --locked

# COPY pipeline.py ./
# ENTRYPOINT ["uv", "run", "python", "pipeline.py"]




FROM python:3.13.11-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

RUN apt-get update && apt-get install -y \
    libpq-dev gcc \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /code
ENV PATH="/code/.venv/bin:$PATH"

COPY pyproject.toml .python-version uv.lock ./
RUN uv sync --locked

COPY ingest_data.py .

ENTRYPOINT ["uv", "run", "python", "ingest_data.py"]