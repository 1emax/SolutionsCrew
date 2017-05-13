FROM python:3.4
ENV PYTHONUNBUFFERED 1

MAINTAINER Artem Bernatskyi <artem.bernatskyy@gmail.com>

ENV INSTALL_PATH /webapps/code

RUN mkdir -p $INSTALL_PATH
WORKDIR ${INSTALL_PATH}

RUN mkdir /webapps/config  
ADD requirements.txt /webapps/config/
RUN pip install -r /webapps/config/requirements.txt


ADD . ${INSTALL_PATH}

RUN python manage.py collectstatic --noinput