#!/bin/sh

cd django_shop

# Collect static files
#echo "Collect static files"
#python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Loading data into the db
echo "\nLoading data into the db"
python manage.py loaddata db.json

# Start server
echo "\nStarting server"
python manage.py runserver 0.0.0.0:8000