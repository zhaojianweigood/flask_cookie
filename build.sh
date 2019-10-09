#!/usr/bin/env bash
set -e

ENV=$1

ALIYUN_REGISTRY="***.aliyuncs.com"
IMAGE_NAME=${ALIYUN_REGISTRY}"/***/flask_cookie"

function build_push(){
    docker login --username=*** -p *** ${ALIYUN_REGISTRY}
    docker build . -t ${IMAGE_NAME}:${ENV}
    docker push ${IMAGE_NAME}:${ENV}
    echo "Deploy finished at $(date '+%Y-%m-%d %H:%M:%S')"
}

case "$ENV" in
   "prod"|"dev")
       build_push
       ;;
   *)
       echo "Invalid env: ${ENV}"
       ;;
esac


