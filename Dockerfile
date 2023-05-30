FROM python:3.10.9-slim

WORKDIR /events

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY /events .


# CMD ["gunicorn", "config.wsgi", "--bind", "0.0.0.0:8202"]