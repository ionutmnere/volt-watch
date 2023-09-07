#!/usr/bin/env bash

set -a
source .env
set +a
cd www
./manage.py $@
cd ..
