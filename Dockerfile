FROM python:3.11-alpine

LABEL maintainer="Hasnain our.hasnain22@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D angle
USER angle
