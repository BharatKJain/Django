# Notes: initCommands-'settings.py'

## Init-Commands

* Create virtual-environment: ```virtualenv venv```
* Installion of django : ```pip install django```
* Boilerplate for django-project: ```django-admin startproject <nameOfProject> .```
* Starting django server: ```python manage.py runserver```
---
## Advanced Init-Commands:
* Migration/Sync of setting with Django project: ```python manage.py migrate```
    * Run this command whenever a error pops up while running
    * Run this command to sync the settings.py with django project
* Create User in Django project: ```python manage.py createsuperuser```
    * To access '/admin' route in django project
    * This also activates the 'django.contib.auth'
* Create an app: ```python manage.py startapp <nameOfAppComponent>```
    * To create an app inside base directory
---

## Description of 'settings.py': 

> BASE_DIR
* path of manage.py 
* In our current case it should be: ```....\django-coursework\personal-code-repo\FreeCodeCamp```
> SECRET_KEY
* They are always unique
* Do not leak it publicaly when code goes into production
> DEBUG
* Keep it true when in development, else false when in production
> INSTALLED_APPS
* This is where we add our app
* Suppose we have "list of products", then we'll pu that in this section
* Smaller pieces of Django project
> MIDDLEWARE
* It deals with requests and how they're handled
* Also, deals with security aspect
> ROOT_URLCONF
* Deals with routing of webpage
> TEMPLATES
* Basically, HTML page that gets rendered in Django
* We mention the folder name of templates in TEMPLATES->DIRS=[], for example 
> WSGI_APPLICATION
* Server goes through and uses this setting
> DATABASES
* Django can link up with the mentioned database
* We are using SQLITE3 right now
> AUTH_PASSWORD_VALIDATORS
* Validates that passwords are strong
> STATIC_URL
* storage of images, videos etc.

