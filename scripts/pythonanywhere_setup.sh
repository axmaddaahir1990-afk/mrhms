#!/usr/bin/env bash
set -e
python3.12 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate --noinput
if [ "$LOAD_FIXTURE" = "1" ]; then
  python manage.py loaddata data.json || true
fi

