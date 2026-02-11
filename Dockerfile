FROM python:3.11-slim-bullseye

ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

RUN pip install pipenv --no-cache-dir

COPY Pipfile ./
RUN pipenv lock && pipenv install --system --deploy

COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]