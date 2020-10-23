# Notes: Including conditional statements in HTML Templates using templates/about.html

* Template Tags are :
- {% extends %}
- {% blocks %}

* Filters are:
- {{item|add:100}}

* We use '|'(pipe) sign with the filter name to add the filter.
* We can also use multiple filters:
```
{{item|upper|firstcap}}
```
This will uppecase all letters and capitalize the first letter.

## References:
- (Built in templates)[https://docs.djangoproject.com/en/3.1/ref/templates/builtins/]
- (Built in filters)[https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#built-in-filter-reference]

## Execution:
- Go to templates/about.html and add:
```
<!-- part14 -->
<p>capfirst Filter--{{my_text|capfirst}}</p>
<p>capfirst Filter with upper Filter-- {{my_text|capfirst|upper}}</p>
<p>capfirst Filter with title Filter-- {{my_text|capfirst|title}}</p>
<p>capfirst Filter with lower Filter-- {{my_text|lower}}</p>
<p>capfirst Filter with direct string-- {{"test string"|capfirst}}</p>
<p>Raw my_html-- {{my_html}}</p>
<p>safe filter on my_html-- {{my_html|safe}}</p>
<p>slugify filter on my_html-- {{my_html|slugify}}</p>
<p>striptags filter on my_html-- {{my_html|striptags}}</p>
<!-- part14 -->
```

## NOTE:
- safe filter should be used replaced with mark_safe