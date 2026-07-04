#!/usr/bin/env bash
set -e
pip install -r requirements.txt
pip install -r requirements_remote.txt
python manage.py collectstatic --noinput
python manage.py migrate
