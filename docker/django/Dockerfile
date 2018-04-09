FROM python:3.6

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH $PYTHONPATH:src
ARG DJANGO_ENV

RUN apt update
RUN apt install -y \
    libmemcached-dev \
    zlib1g-dev \
    libssl-dev \
    python-dev \
    build-essential 

WORKDIR /code

COPY requirements/ requirements/

RUN pip install --upgrade pip \
	&& pip install -r requirements/$DJANGO_ENV.txt

COPY . /code/

RUN rm requirements/ -rf \
    && mv docker/django/uwsgi.ini uwsgi.ini \
    && rm docker/ -rf

CMD uwsgi --ini=./uwsgi.ini
