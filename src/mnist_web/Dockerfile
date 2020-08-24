FROM ubuntu:latest

RUN apt-get update && apt-get -y install vim less
RUN apt-get update && apt-get -y install python3-dev python3-pip
RUN pip3 install --user --upgrade tensorflow-cpu
RUN pip3 install --user --upgrade keras
RUN pip3 install --user --upgrade opencv-python Pillow

RUN mkdir /home/keras
