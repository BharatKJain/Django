# Notes: Including HTML templates by using template tag

How to add data from views.py to the generated HTML.

We use Context i.e. shown below:

```
def about_view(request,*args, **kwargs):
    website_context={
        "my_text":"This is about coding",
        "my_number":123
    }
    return render(request,"about.html",website_context)
```

## Execution:

- Go to pages/views.py and update the code as following:

```
def about_view(request,*args, **kwargs):
    #return render(request,"about.html",{})

    #--------------------part11
    website_context={
        "my_text":"This is about coding",
        "my_number":123
    }
    return render(request,"about.html",website_context)
    #part11-----------------
```

- Go to templates/about.html and update the code as following:

```
<!-- part9 -->
{% extends 'base.html'%}
{% block content%}
<h1>About</h1>
<p>This is a template</p>
<!-- part11 -->
{{my_text}}, {{my_number}}
<!-- part11 -->
{%endblock%}
```

## Note:

- We use {{}} in HTML to mention the context variables
- Context is passed during render in views.py
