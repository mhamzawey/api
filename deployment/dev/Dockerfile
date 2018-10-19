FROM ubuntu:16.04


RUN apt-get update
RUN apt-get -y install locales mysql-client vim python3 python3-pip  libmysqlclient-dev libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev
RUN locale-gen en_US.UTF-8

RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

COPY ./dev_req.txt /dev_req.txt
RUN pip3 install -r /dev_req.txt

RUN mkdir -p /app

COPY ./start /start
RUN chmod a+x /start
WORKDIR /app