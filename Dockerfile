FROM python:3.11.1-slim

RUN mkdir /fastapi_app

WORKDIR /fastapi_app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x docker/*.sh