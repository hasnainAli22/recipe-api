FROM python:3.11-alpine

LABEL maintainer="Hasnain our.hasnain22@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./requirements.dev.txt /requirements.dev.txt

ARG DEV=false

RUN apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .temp-build-deps \
        build-base postgresql-dev musl-dev && \
    pip install -r requirements.txt && \
    if [ "${DEV}" = "true" ]; \
        then pip install -r requirements.dev.txt ; \
    fi && \ 
    apk del .temp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D angle
USER angle
