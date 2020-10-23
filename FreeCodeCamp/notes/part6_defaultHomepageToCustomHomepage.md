# Notes: Create views and add custom homepage in views.py

Start working with views and create homepage.

## Execution:
* Create an app named pages: ```python manage.py startapp pages```
* Add the following code in pages.views:
    ```
    from django.http import HttpResponse
    def home_view(*args, **kwargs):
        return HttpResponse("<h1>Hello World</h1>")
    ```
* Then modify the urls.py to :

    ```
    from django.contrib import admin
    from django.urls import path

    from pages.views import home_view
    # from products.views import 

    urlpatterns = [
        path("admin/", admin.site.urls),
        # adding custom path
        path("", home_view, name="home"),
    ]
    ```

* Now the homepage will be Hello World! because of empty path being set to home_view
