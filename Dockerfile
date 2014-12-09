FROM ubuntu:precise
MAINTAINER Miguel Angel Gordian <miguel.angel@codeandomexico.org>

ENV DEBIAN_FRONTEND noninteractive
ENV TUTUM_USER miguel
ENV TUTUM_APIKEY ""


RUN apt-get update && \
    apt-get install -y python2.7 python-pip python-dev

ADD . /broker
WORKDIR /broker

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT python broker.py
