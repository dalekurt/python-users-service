FROM python:3.10-alpine3.13

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml ./
COPY poetry.toml ./
COPY poetry.lock ./

RUN poetry install --no-dev

COPY . .

EXPOSE 8080
ENTRYPOINT ["poetry", "run"]
CMD ["gunicorn", "-b0.0.0.0:8080", "app:api"]
