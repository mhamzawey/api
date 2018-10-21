FROM ubuntu:16.04


RUN apt-get update
RUN apt-get -y install locales mysql-client vim python3 python3-pip libmysqlclient-dev python3-dev libffi-dev libssl-dev git cron
RUN locale-gen en_US.UTF-8

RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

COPY ./dev_req.txt /dev_req.txt
RUN pip3 install -r /dev_req.txt

RUN mkdir -p /app

ADD ./cron /cron
RUN chmod 0600 /cron
RUN touch /var/log/scrapy.log
RUN crontab /cron
WORKDIR /app



