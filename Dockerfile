FROM ubuntu:14.04

RUN apt-get update && apt-get install -y python2.7 python-dev graphviz git python-pip

RUN mkdir /code

WORKDIR /code

ADD requirements.txt /code/

RUN pip install -r requirements.txt

WORKDIR /code/app

ADD demo /code/app
