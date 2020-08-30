#!/bin/bash

IMAGE=my-keras-mnist_web
CONTAINER=my-keras-mnist_web-app
echo ======================
echo build
echo ======================
docker build -t $IMAGE .

echo ======================
echo ls
echo ======================
docker image ls $IMAGE

echo ======================
echo run
echo ======================
docker run -dit --name $CONTAINER -p 80:80 $IMAGE

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
