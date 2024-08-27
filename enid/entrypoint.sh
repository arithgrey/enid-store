#!/bin/sh

# Ejecuta las migraciones si es necesario}
echo "Microservice Store"
echo "Running makemigrations and migrate..."
echo "Running makemigrations and migrate..."
echo "Running makemigrations and migrate..."
echo "Running makemigrations and migrate..."

python manage.py makemigrations image categories product_group products product_category_search variants product_variant state address order order_oauth order_search item_order search
python manage.py makemigrations
python manage.py migrate
# Inicia el servidor con watchmedo
echo "Starting the server with watchmedo..."
watchmedo auto-restart --directory=./ --pattern=*.py --recursive -- gunicorn -b 0.0.0.0:8080 enid.wsgi:application
