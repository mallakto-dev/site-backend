FROM python:3.12-alpine AS builder

WORKDIR /app

COPY . .

RUN python -m pip install --no-cache-dir poetry==1.4.2 \
  && poetry config virtualenvs.in-project true \
  && poetry install --without dev --no-interaction --no-ansi \
  && poetry run python manage.py migrate

CMD [".venv/bin/gunicorn", "-w", "5", "-b", "0.0.0.0:8000", "app.wsgi"]