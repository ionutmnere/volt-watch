#!/usr/bin/env bash

# load environment
set -a
source .env
set +a

# prepare folders
[[ ! -d "./static" ]] && mkdir -p ./static
[[ ! -d "./www/data" ]] && mkdir -p ./www/data

# run django command
cd www
./manage.py $@
cd ..
