# Notes: Including conditional statements in HTML Templates using templates/about.html and pages/views.py

We learn about adding conditional statements i.e. 'if' by using:
```
{% if item == 312 %}
    <li>Item{{forloop.counter}}-{{item}}-{{item|add:100}}</li>
{% elif item == "Abc" %}
    <li> Invalid Item </li>
{% else %}
    <li>Item{{forloop.counter}}-{{item}}</li>
{%endif%}
```

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
    # #--------------------part12
    # website_context={
    #     "my_text":"This is about coding",
    #     "my_number":123,
    #     "my_list":['this','is','my','list']
    # }
    # return render(request,"about.html",website_context)
    # #part12-----------------
    #-------------------------part13
    website_context={
        "my_text":"This is about coding",
        "my_number":123,
        "my_list":[1313,4231,312,"Abc"]
    }
    return render(request,"about.html",website_context)
    #part13-------------------------
```
- Go to template/about.html:
```
<!-- part13 -->
<ul>
{% for item in my_list%}
    {% if item == 312 %}
        <li>Item{{forloop.counter}}-{{item}}-{{item|add:100}}</li>
    {% elif item == "Abc" %}
        <li> Invalid Item </li>
    {% else %}
        <li>Item{{forloop.counter}}-{{item}}</li>
    {%endif%}
{% endfor %}
</ul>
<!-- part13 -->
```

## NOTE:
- {{forloop.counter}}, {{item|add:100}} is known as template tag and filters in Django templates.