# Notes: Including for loops in HTML Templates

We learn about looping in HTML when a list object is passed in the context, such that it can iterate to form a HTML list.

## Execution:
- Go to pages/views.py:
```
def about_view(request,*args, **kwargs):
    #return render(request,"about.html",{})
    
    #--------------------part11
    # website_context={
    #     "my_text":"This is about coding",
    #     "my_number":123
    # }
    # return render(request,"about.html",website_context)
    #part11-----------------
    #--------------------part12
    website_context={
        "my_text":"This is about coding",
        "my_number":123,
        "my_list":['this','is','my','list']
    }
    return render(request,"about.html",website_context)
    #part12-----------------
```
- Go to template/about.html:
```
<!-- part9 -->
{% extends 'base.html'%}
{% block content%}
<h1>About</h1>
<p>This is a template</p>
<!-- part11 -->
{{my_text}}, {{my_number}}
<!-- part11 -->
<!-- part12 -->
<ul>
{% for item in my_list%}
<li>{{item}}</li>
{% endfor %}
</ul>
<!-- part12 -->
{%endblock%}
```