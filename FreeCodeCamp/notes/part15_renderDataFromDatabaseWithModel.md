# Notes: Including conditional statements in HTML Templates using templates/about.html

How to load content from sqlite as well as creating HTML templaet for the same.

## References:
- (Built in templates)[https://docs.djangoproject.com/en/3.1/ref/templates/builtins/]
- (Built in filters)[https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#built-in-filter-reference]

## Execution:
- Go to terminal, run interactive shell by using ```python manage.py shell``` and fetch data-points:
```
from products.models import Product
Product.objects.get(id=1)
obj=Product.objects.get(id=1)
dir(obj)
obj.title
```
- Go to products/views and replace with the following code:
```
from django.shortcuts import render
from .models import Product


def product_detail_view(request):
    obj = Product.objects.get(id=3)
    object_context = {"object": obj}
    return render(request, "product/detail.html ", object_context)
```

- Create a folder "product" in templates, then add product/detail.html:
```
{% extends 'base.html'%}
{%block content%}
<h1>{{object.title}}</h1>
<p>
    {% if object.description != None and object.description != '' %}
        {{object.description}}
    {% else %}`
        Description Coming Soon!
    {%endif%}
</p>
{%endblock%}
```

## Limitations:
- When we're working with products specific apps, we need to store the template for the products page in products folder.
