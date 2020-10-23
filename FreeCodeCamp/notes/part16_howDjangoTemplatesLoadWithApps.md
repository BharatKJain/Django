# Notes: Including conditional statements in HTML Templates using templates/about.html

How to load content from sqlite as well as creating HTML templaet for the same.

## References:
- (Built in templates)[https://docs.djangoproject.com/en/3.1/ref/templates/builtins/]
- (Built in filters)[https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#built-in-filter-reference]

## Execution:
- Create a folder named templates inside "src/products", then add "src/products/templates/products_details.html":
```
{% extends 'base.html'%}
{%block content%}
<h1>{{object.title}}</h1>
<p>
    {% if object.description != None and object.description != '' %}
        {{object.description}}
    {% else %}
        Description Coming Soon!
    {%endif%}
</p>
{%endblock%}
```
- Update the products/views.py with:
```
```

## NOTES:
- When we create template folder inside an app, and another template folder is already present in root like ```src/products/templates/products``` and ```src/templates/products```, then the root directory will override the HTML template file present in app directory.
