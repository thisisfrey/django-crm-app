# Build Out The Basic App

Creating a new webpage in Django is a 3-step-process:
- Create an URL
- Create actual template file 
- Create a view

##  URL configuration for dcrm project
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

## Create home URL
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

## Create home view
- Open the existing file [views.py](../dcrm/website/views.py)
- Add the following lines
```python
def home(request):
    return render(request, 'home.html', {})
```

## Create home template
- Create a new directory named [templates](../dcrm/website/templates)
- Create the template file [home.html](../dcrm/website/templates/home.html)
- Add the following content:
```html
<h1>Hello world!</h1>
```


