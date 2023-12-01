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
    # Make migrations and migrate the database.
    echo "Making migrations and migrating the database"
    # TODO: Remove before uploading
    python manage.py migrate blog zero
    python manage.py migrate --noinput
    # TODO: Maybe we should move to migration
    python manage.py loaddata initial_data.yaml
fi

exec "$@"
