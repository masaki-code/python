#!/bin/bash

echo docker ps
docker ps
echo

read -p "name? " NAME

echo $NAME
echo

echo docker stop $NAME
docker stop $NAME
echo

echo docker ps
docker ps
echo
