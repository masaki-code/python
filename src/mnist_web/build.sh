#!/bin/bash

IMAGE=my-keras-mnist_web
TAG=tmp_`date +"%H%M%S"`
CONTAINER=my-keras-mnist_web-app_$TAG
echo ======================
echo build
echo ======================
docker build -t $IMAGE:$TAG .

echo ======================
echo ls
echo ======================
docker image ls $IMAGE

echo ======================
echo run
echo ======================

# docker run -dit --name $CONTAINER -p 80:80 $IMAGE:$TAG
docker run -dit --name $CONTAINER -p 80:80 -v $PWD/src/python:/home/keras/lib -v $PWD/src/php:/var/www/html/ $IMAGE:$TAG

echo ======================
echo ps
echo ======================
docker ps

echo ======================
echo exec
echo ======================
docker exec -it $CONTAINER /bin/bash

echo ======================
echo stop
echo ======================
docker stop $CONTAINER
