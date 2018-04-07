FROM python:3.7.0b3

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH $PYTHONPATH:src
ARG DJANGO_ENV

RUN apt update

WORKDIR /code

COPY requirements/ requirements/

RUN pip install --upgrade pip \
	&& pip install -r requirements/$DJANGO_ENV.txt

COPY . /code/

RUN rm requirements/ -rf \
    && mv docker/django/uwsgi.ini uwsgi.ini \
    && rm docker/ -rf

CMD uwsgi --ini=./uwsgi.ini
