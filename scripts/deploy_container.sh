#!/bin/bash
set -e

cd /home/ec2-user/app

docker stop ml-app 2>/dev/null || true
docker rm ml-app 2>/dev/null || true

docker build -t ml-app:latest .
docker run -d --name ml-app --restart always -p 80:5000 ml-app:latest

sleep 5
docker ps --filter name=ml-app
