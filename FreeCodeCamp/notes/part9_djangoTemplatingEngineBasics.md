# Notes: Django Templating Engine Basics and Creating HTML Templates using views.py

When we're dealing with HTML templates, we need to be able to modify them dynamically, thus we use the following syntax:

```
<body>
    <!-- <h1>Test</h1> -->
    {% block content %}
    replace me
    {% endblock %}
</body>
```

we can access "content" by inheriting the base.html file and then replacing the HTML inside content block like:

```
{% extends 'base.html'%}
{% block content%}
<h1>Social</h1>
<p>This is a template</p>
{%endblock%}
```

in social.html

So, we can dynamically add information to the webpage

## Execution:

- Create a file named base.html:

```
<!-- part9 -->
<!DOCTYPE html>
<html>
    <head>
        <title>
            Just doing my thing.
        </title>
    </head>
<body>
    <!-- <h1>Test</h1> -->
    {% block content %}
    replace me
    {% endblock %}
</body>
</html>
```

- Modify all the inheriting HTML files i.e. home.html, social.html, contact.html, about.html by using the following syntax:

```
{% extends 'base.html'%}
{% block content%}
<h1>Social</h1>
<p>This is a template</p>
{%endblock%}
```
