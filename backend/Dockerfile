FROM python:3.10-slim-bullseye

ENV PYTHONUNBUFFERED=1  \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_VERSION=1.2.2 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

RUN pip3 install "poetry==${POETRY_VERSION}"

WORKDIR /code

COPY pyproject.toml poetry.lock /code/

RUN poetry config virtualenvs.create false 
RUN poetry install --no-dev --no-interaction --no-ansi

COPY . .