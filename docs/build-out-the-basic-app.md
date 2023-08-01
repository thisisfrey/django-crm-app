# Build Out The Basic App

## Home Page

Creating a new webpage in Django is a 3-step-process:

- Create an URL
- Create actual template file
- Create a view

### URL configuration for dcrm project

Change the existing [URL configuration](../dcrm/dcrm/urls.py):

- Import include from django.urls
- Include the url [website.urls](../dcrm/website/urls.py)

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls'))
]
```

### Create home URL

- Open the project directory [website](../dcrm/website)
- Create a new file with the name [urls.py](../dcrm/website/urls.py)
- Add home view to the root url

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

### Create home view

- Open the existing file [views.py](../dcrm/website/views.py)
- Add the following lines

```python
def home(request):
    return render(request, 'home.html', {})
```

### Create home template

- Create a new directory named [templates](../dcrm/website/templates)
- Create the template file [home.html](../dcrm/website/templates/home.html)
- Add the following content:

```html
<h1>Hello world!</h1>
```

<!--- Hello world is working now! -->

## Add base.html

- Create [base.html](../dcrm/website/templates/base.html) file with bootstrap and entry points for the Django app.
- Copy content from [Bootstrap Docs](https://getbootstrap.com/docs/5.3/getting-started/introduction/) and include
  Bootstrap’s CSS and JS.

**base.html**

```hml
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Django CRM App</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
  </head>
  <body>

    {% block content %}
    {% endblock %}
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
  </body>
</html>
```

Make the following changes in the home.html-file.

**home.html**

```hml
{% extends 'base.html' %}

 {% block content %}
 <h1>Hello world!</h1>
 {% endblock %}
```

## Add bootstrap components

### Navbar

- Copy navbar from [Bootstrap](https://getbootstrap.com/docs/5.3/components/navbar/#how-it-works)
- Include the navbar in the base.html body-tag:

```hml
 <body>
      {% include 'navbar.html'%}
      <!-- More code goes here-->
 </body>  
```

### Preview

The Django CRM app running on [127.0.0.1:8000](http://127.0.0.1:8000/) now looks like this:
<img src="./images/hello-world-with-navbar.JPG">





