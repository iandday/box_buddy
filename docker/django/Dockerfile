FROM python:3.12 AS base

ARG DEV
ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

# RUN apt update && \
#     apt install libpq-dev


FROM base AS builder

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

# RUN apt update && \
#     apt install musl-dev build-base gcc gfortran openblas-dev

WORKDIR /app

# Install Poetry
RUN pip install poetry==2.1.1

# Install the app
COPY pyproject.toml ./ 

RUN if [ "${DEV}" = "true" ] ; \
     then poetry install --with dev --no-root ; \
     else poetry install --without dev --no-root ; \
    fi

RUN rm -rf $POETRY_CACHE_DIR;



FROM base AS runtime

RUN adduser django --home /home/django

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY app /app/src
COPY docker/django/run-*.sh /app

RUN mkdir /app/static
RUN mkdir /app/media

RUN chmod a+x /app/run-*.sh
RUN chown -R django /app

WORKDIR /app/src
USER django

