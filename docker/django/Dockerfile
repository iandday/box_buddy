FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS builder

ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy
ENV UV_PYTHON_DOWNLOADS=0


# Install the project into `/app`
WORKDIR /app

# dependency resolution and caching
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    --mount=type=bind,source=README.md,target=README.md \
    uv sync --frozen --no-install-project 
    #--no-dev

COPY ./app /app
COPY docker/django/run-*.sh /app

# installs the dependencies after the application code is copied.
RUN --mount=type=cache,target=/root/.cache/uv \
--mount=type=bind,source=uv.lock,target=uv.lock \
--mount=type=bind,source=pyproject.toml,target=pyproject.toml \
--mount=type=bind,source=README.md,target=README.md \
    uv sync --frozen 
    #--no-dev


FROM python:3.12-slim-bookworm
COPY --from=builder --chown=app:app /app /app


ENV PATH="/app/.venv/bin:$PATH"

RUN adduser django --home /home/django



# Create the static and media directories
RUN mkdir /app/static
RUN mkdir /app/media

RUN chmod a+x /app/run-*.sh
RUN chown -R django /app

WORKDIR /app/src
USER django








