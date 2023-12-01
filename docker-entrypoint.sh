#!/bin/bash

if [ "$DATABASE" = "postgres" ]; then
    echo "Waiting for postgres..."

    while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py makemigrations --noinput

if [[ "$@" != *"manage.py test"* ]]; then
    echo "Making migrations and migrating the database"
    python manage.py migrate --noinput
fi

exec "$@"
