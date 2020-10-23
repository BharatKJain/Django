# Notes: AppComponents-'INSTALLED_APPS' & Models.py

Basically, we deal with INSTALLED_APPS section in this part where we initially access the admin page 
and then we create our own custom model in models.py.

## Execution:
* '/admin' route access:
    * Access the 'http://127.0.0.1:8000/admin' site
    * To create super user: ```python manage.py createsuperuser```
    * Then use the super user to access the admin page and login
* Creating custom INSTALLED_APPS package(models.py/model):
    * To create a app: ```python manage.py startapp products```
    * Now in models.py file we add the follwing code:
        ```
        class Product(models.Model):
            title = models.TextField()
            description = models.TextField()
            price = models.TextField()
        ```
    * Then, we add products to INSTALLED_APPS in settings.py
    * Then, we run : ```python manage.py makemigrations```, to add the changes made in 'settings.py'
    * Then we run: ```python manage.py migrate```
    * These two commands(makemigrations and migrate) are to be run everytime we change models.py
    * Then, we add another field in models.py i.e. ```summary=models.TextField(default='this is cool')```
    * Then we import our Products model in admin.py, using relative import ```from .models import Product``` and ```admin.site.register(Product)```
    * Then run django server
    