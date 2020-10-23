# Notes: URL Routing and Requests using urls.py and views.py

URL Patterns and Routing, how to create "xyz.com/home","xyz.com/about","xyz.com/social"

## Execution:

- Create the views:

  ```
  def contact_view(*args,**kwargs):
      return HttpResponse("<h1>Contact Page</h1>")

  def about_view(*args,**kwargs):
      return HttpResponse("<h1>About Page</h1>")

  def social_view(*args,**kwargs):
      return HttpResponse("<h1>Social Page</h1>")
  ```

- Add the following paths in urls.py:
  ```
  path("home/", home_view, name="home"),
  path("contact/",contact_view,name="contact"),
  path("about/",about_view,name="about"),
  path("social/",social_view,name="social")
  ```
- Now the paths should be accessible, like 127.0.0.1:8000/contact

## Note:

`def contact_view(*args,**kwargs):` in this args contain WSGI request object, request object contains the request information, this will be discussed in later modules.
