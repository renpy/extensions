#!/bin/bash

set -e

cd $(dirname $(realpath $0))

./sign.py

rsync --delete --delete-excluded --progress -a \
    /home/tom/ab/extensions/ \
    tom@abagail.onegeek.org:/home/tom/WWW.extensions \
    --exclude .\* \
    --exclude typings \
    --exclude deploy.sh \
    --exclude pyproject.toml \
    --exclude sign.py
