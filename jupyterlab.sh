#!/bin/sh

# Starts Jupyter without the need of a password or token
jupyter lab \
    --allow-root \
    --ip=0.0.0.0 \
    --no-browser \
    --NotebookApp.password='' \
    --NotebookApp.token=''
