# Notes: adding values in model using interactive-shell

We deal with django shell, running django in interactive shell.

## Execution:
* Command: ```python manage.py shell```
    * When we run the above command then we gain access to an interactive shell
    * Then we can run commmands like:
        * ```from products.models import Product```, like in admin.py
        * To create a object in products(database): ```Product.objects.create(title="new prdct",description="another one",price="19132",summary="sweet")```
        * To list all products in database: ```Product.objects.all()```