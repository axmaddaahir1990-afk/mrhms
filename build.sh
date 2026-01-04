#!/usr/bin/env bash
set -e
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate --noinput
if [ "$SEED" = "1" ]; then
  python scripts/seed_demo.py || true
fi
