FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /var/www/marathon

WORKDIR /var/www/marathon

COPY requirements.txt /var/www/marathon

RUN pip install -r requirements.txt