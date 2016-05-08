#!/usr/bin/env bash
source activate vdict_service

cd /app

python manage.py makemigrations vdict_service

python manage.py migrate

python manage.py runserver 0.0.0.0:8000
