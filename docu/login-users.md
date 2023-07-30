# Login Users

## Django authentication

Import the django authentication and messages into the [views](../dcrm/website/views.py)

```python
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
```

### Login as superuser

Login [here](http://127.0.0.1:8000/admin)

## Add login and logout

3-steps-process:

1. Add new route
2. Add new view
3. Create new template

### Add new views

Add login_user- and logout_user-view in [views.py](../dcrm/website/views.py).

```python
def login_user(request):
    pass


def logout_user(request):
    pass
```

### Add URLs

Add login- and logout-route to [urls.py](../dcrm/website/urls.py).

```python
urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login_user(), name='login'),
    path('logout', views.logout_user(), name='logout'),
]
```

### Login Form

In the following the login form is added to the home-page instead of a separate form-template. Therefore the code is
slightliy different.
You can find the login form in [home.html](../dcrm/website/templates/home.html)

### Change templates

## Timezone Error

ZoneInfoNotFoundError: 'No time zone found with key utc'

```console
pip install tzdata
```
