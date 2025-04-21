FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=never \
    UV_PYTHON=python3.12


RUN apt-get update && \
    apt-get install -y curl git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# dependency resolution and caching
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    --mount=type=bind,source=README.md,target=README.md \
    uv sync --locked --no-install-project
    #--no-dev

COPY . /app

# installs the dependencies after the application code is copied.
RUN --mount=type=cache,target=/root/.cache/uv \
--mount=type=bind,source=uv.lock,target=uv.lock \
--mount=type=bind,source=pyproject.toml,target=pyproject.toml \
--mount=type=bind,source=README.md,target=README.md \
    uv sync --locked
    #--no-dev

ENV PATH="/app/.venv/bin:$PATH"

RUN adduser django --home /home/django

# Create the static and media directories
RUN mkdir /app_static
RUN mkdir /app_media

RUN chmod a+x /app/docker/django/entrypoint.sh
RUN chown django -R /app*

WORKDIR /app
USER django

ENTRYPOINT ["/bin/bash", "/app/docker/django/entrypoint.sh"]
