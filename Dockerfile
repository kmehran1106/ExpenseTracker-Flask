FROM python:3.8.5-slim-buster

RUN mkdir -p /code
WORKDIR /code

RUN pip install --upgrade pip && pip install pipenv

COPY ./Pipfile /code/Pipfile
COPY ./Pipfile.lock /code/Pipfile.lock
RUN pipenv install --system --deploy --ignore-pipfile

