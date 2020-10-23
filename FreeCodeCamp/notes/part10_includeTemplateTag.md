# Notes: Including HTML templates by using template tag

We learn about adding external HTML files at specific places by using "include":

```
{% include 'navbar.html' %}
```

## Execution:

- Create a file named navbar.html in templates:

```
<!-- part10 -->
<nav>
    <ul>
        <li>Brand</li>
        <li>Contact</li>
        <li>About</li>
    </ul>
</nav>
```

- Add navbar.html to base.html by using the following code:

```
<body>
    <!-- part10 -->
    {% include 'navbar.html' %}
    <!-- /part10 -->
    <!-- <h1>Test</h1> -->
    {% block content %}
    replace me
    {% endblock %}
</body>
</html>
```
