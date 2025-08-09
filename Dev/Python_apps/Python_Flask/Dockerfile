# Dockerfile for the Flask app using uv as the package manager
# Default to Python 3.12.10 to match pyproject.toml
ARG PYTHON_VERSION=3.12.10

FROM python:${PYTHON_VERSION}-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_LINK_MODE=copy \
    # Set a non-root user later if desired
    APP_HOME=/app

# Install curl and certificates to fetch uv installer
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install uv (https://github.com/astral-sh/uv)
RUN curl -LsSf https://astral.sh/uv/install.sh | sh \
    && ln -s /root/.local/bin/uv /usr/local/bin/uv \
    && ln -s /root/.local/bin/uvx /usr/local/bin/uvx

WORKDIR ${APP_HOME}

# Copy only dependency files first for better caching
COPY pyproject.toml ./
# If you later add a uv.lock, copy it too to leverage layer caching
# COPY uv.lock ./

# Sync project dependencies (no dev deps)
RUN uv sync  
# --no-dev

# Copy application source
COPY app.py ./
COPY src ./src

# Expose Flask port
EXPOSE 5050