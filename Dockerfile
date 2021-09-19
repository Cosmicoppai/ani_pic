FROM PYTHON:3.9.4-slim

LABEL Maintainer="CosmicOppai"
LABEL Description="Anime Pic and Quote API"

COPY requirements.txt requirements.txt

ENV DB_USER=${DB_USER}
ENV DB_PASSWORD=${DB_PASSWORD}
ENV DB_PASSWORD=${DB_PASSWORD}
ENV DEBUG=${DEBUG}
ENV HOST=${HOST}

COPY anipic ./anipic

WORKDIR ./anipic

RUN py manage.py makemigrations
RUN py manage.py migrate

EXPOSE 8000

CMD ["py", "manage.py", "runserver", "8000"]