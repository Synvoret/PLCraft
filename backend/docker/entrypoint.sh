#!/bin/sh

echo "Run migrations..."
python manage.py migrate

echo "I collect static files..."
python manage.py collectstatic --noinput

exec "$@"