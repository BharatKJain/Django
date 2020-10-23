# Notes:  Adding different types of fields in models.py

How to create models in django which has different field-types such as integer, strings and others.

## Reference:
    (https://docs.djangoproject.com/en/3.1/topics/db/models/#field-types)[Django Field Types]

## Execution:
* We edit our old model from :
    ```
    class Product(models.Model):
        title = models.TextField()
        description = models.TextField()
        price = models.TextField()
        summary=models.TextField(default='this is cool')
    ```
    
    To

    ```
    class Product(models.Model):
        title = models.CharField(max_length=120)
        description = models.TextField()
        price = models.DecimalField(decimal_places=2,max_digits=1000)
        summary=models.TextField(default='this is cool')
    ```

* Then we can test the same, using either django-shell or by using UI( 127.0.0.1:8000 )