FROM php:7.2-apache

RUN apt-get update && apt-get -y install vim less
RUN apt-get update && apt-get -y install python3-dev python3-pip
RUN apt-get update && apt-get -y install curl

RUN mkdir -p /home/keras
RUN pip3 install -U virtualenv && virtualenv --system-site-packages -p python3 /home/keras/venv
RUN . /home/keras/venv/bin/activate && \
      /home/keras/venv/bin/pip install --upgrade pip && \
      /home/keras/venv/bin/pip install --upgrade tensorflow-cpu && \
      /home/keras/venv/bin/pip install --upgrade keras && \
      /home/keras/venv/bin/pip install --upgrade opencv-python  && \
      /home/keras/venv/bin/pip install --upgrade Pillow

RUN mkdir -p /home/keras/lib && \
    mkdir -p /home/keras/images &&  \
   chmod 757 /home/keras/images

COPY ./src/python /home/keras/lib
COPY ./src/images /home/keras/images
COPY ./src/php    /var/www/html/
