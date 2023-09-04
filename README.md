# Django-Random-Project-1
django-admin startproject auction1
mkdir templates
mkdir assets
cd assets
mkdir css
mkdir js
mkdir media
cd..
python manage.py collectstatic
django-admin startapp authentication
django-admin startapp home
django-admin startapp transactionControl
python manage.py makemigrations (After you've setup the database, it's details and listed newly created apps in apps list in the settings.py file)
python manage.py migrate
