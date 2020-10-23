# Notes: Django Templating Engine and Creating HTML Templates using views.py and settings.py

Instead of using :

```
def contact_view(*args,**kwargs):
    return HttpResponse("<h1>Contact Page</h1>")
```

we use the following code:

```
def home_view(request,*args, **kwargs):
    return render(request,"home.html",{})
```

Basically, we use html templates instead of small html snippets.

## Execution:

- Go to settings.py and edit this portion like:

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
```

**'DIRS': [BASE_DIR/"templates"],**

```
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

we replace the DIRS section by adding the BASE_DIR/"templates" because we want to add templates folder to our path, such that we can add html.

- Next, we need to add this code in our pages/views.py:

```
def home_view(request,*args, **kwargs):
    return render(request,"home.html",{})
```

### NOTE:

- We have added home.html in templates folder.
- We have used pathlib format instead of os format because new version of django uses pathlib.
