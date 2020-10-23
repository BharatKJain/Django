# Notes: Add New Field in models.py 

Change the database schema by addition of new field without deleting the database and setting default or null values.

## Execution:
* Adding a new field:

    * We add the changes to the products model by introducing new field named "featured".
    * When we add a new field in existing database, we have to make sure the old values have a default value or null value set for the new field.
    * Thus we get this error when we add ```featured=models.BooleanField() # null=True,default=True``` in models.py :
        ```
        (venv) PS C:\Users\bhara\Desktop\JavaScript_Django\django-coursework\personal-code-repo\FreeCodeCamp\src> python .\manage.py makemigrations
        Check this out: C:\Users\bhara\Desktop\JavaScript_Django\django-coursework\personal-code-repo\FreeCodeCamp\src
        You are trying to add a non-nullable field 'featured' to product without a default; we can't do that (the database needs something to populate existing rows).
        Please select a fix:
        1) Provide a one-off default now (will be set on all existing rows with a null value for this column) 2) Quit, and let me add a default in models.py
        Select an option: 1
        Please enter the default value now, as valid Python
        The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
        Type 'exit' to exit this prompt
        >>> True
        Migrations for 'products':
        products\migrations\0005_product_featured.py
            - Add field featured to product
        ```

    * We can also hardcode the process by using this code:
        ```featured=models.BooleanField(default=True)```

* Making a field mandatory:

    * Code:
        ```
        class Product(models.Model):
            title = models.CharField(max_length=120)
            description = models.TextField()
            price = models.DecimalField(decimal_places=2,max_digits=1000)
            #Before: summary=models.TextField(default='this is cool')
            summary=models.TextField(blank=True,null=True)
            # Changes made using part5_changeAModel
            featured=models.BooleanField() # null=True,default=True
        ```
    * Explanation : ```summary=models.TextField(blank=True,null=True)```
        - "blank" is used to make a field mandatory in the form.
        - "null" is used to make a field mandatory in the database.

## Points to note:
* When we run  ```makemigrations``` it creates a file in products/migrations/ which keeps a track of addition of new field in the database.
* Please check it out!
