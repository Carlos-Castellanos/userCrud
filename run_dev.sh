#!/usr/bin/env sh
#   sh run_dev.sh

export FLASK_APP=app/routes.py
export FLASK_ENV=development

flask run