#!/bin/sh
set -e

flask db stamp head
flask db migrate
flask db upgrade


FLASK_APP=app/app.py DB_HOST="${DB_HOST}" DB_USERNAME="${DB_USERNAME}" DB_PASSWORD="${DB_PASSWORD}" flask run