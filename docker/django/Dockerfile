FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY requirements/ requirements/
RUN pip install --upgrade pip && pip install requirements/$DJANGO_ENV.txt
COPY . /code/


RUN rm requirements/ -rf \
    && mv docker/django/uwsgi.ini uwsgi.ini \
    && rm docker/ -rf

ENV PYTHONPATH $PYTHONPATH:src
CMD uwsgi --ini=./uwsgi.ini
