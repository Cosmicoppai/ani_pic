FROM python:3.9.4-slim

LABEL Maintainer="CosmicOppai"
LABEL Description="Anime Pic and Quote API"

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt && python -m pip install --upgrade pip

ENV DB_USER=${DB_USER}
ENV DB_PASSWORD=${DB_PASSWORD}
ENV DB_PASSWORD=${DB_PASSWORD}
ENV DEBUG=${DEBUG}
ENV HOST=${HOST}

COPY anipic ./anipic

WORKDIR ./anipic

RUN mkdir wallpapers

EXPOSE 8000

CMD gunicorn anipic.wsgi:application --bind 0.0.0.0:8000