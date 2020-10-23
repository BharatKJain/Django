from django.db import models

# Create your models here.

'''
## Old model:
class Product(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.TextField()
    summary=models.TextField(default='this is cool')
'''
##New Model:
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=1000)
    # Changes made using part5_changeAModel
    featured=models.BooleanField() # null=True,default=True
    #Before: summary=models.TextField(default='this is cool')
    summary=models.TextField(blank=True,null=True)
