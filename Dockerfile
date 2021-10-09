FROM python:3.9.4-slim

LABEL Maintainer="CosmicOppai"
LABEL Description="Anime Pic and Quote API"

COPY requirements.txt requirements.txt
COPY ./scripts /scripts

RUN pip install -r requirements.txt && python -m pip install --upgrade pip

ENV DB_USER=${DB_USER}
ENV DB_PASSWORD=${DB_PASSWORD}
ENV DB_NAME=${DB_NAME}
ENV DEBUG=${DEBUG}
ENV HOST=${HOST}
ENV DB_HOST=${DB_HOST}
ENV SECRET=${SECRET}

COPY ./anipic /anipic

WORKDIR /anipic
EXPOSE 9000

RUN mkdir -p vol/web/static && \
    mkdir -p vol/web/pics && \
    chmod -R +x /scripts

ENV PATH="/scripts:/py/bin:$PATH"

CMD ["run.sh"]