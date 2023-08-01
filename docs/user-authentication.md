# User Authentication

## Django administration

Login with the previously created superuser on [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).

### Superuser credentials:

- Username: admin
- Password: password

### Fix for Timezone Error

ZoneInfoNotFoundError: 'No time zone found with key utc'

```console
pip install tzdata
```

## Django authentication

3-steps-process:

1. Add new route
2. Add new view
3. Create new template

### Add new views

Import authenticate, login, and logout from django authentication and add the login_user- and logout_user-view
in [views.py](../dcrm/website/views.py).

```python
from django.contrib.auth import authenticate, login, logout


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    login(request, user)


def logout_user(request):
    logout(request)
```

### Add URLs

Add login- and logout-route to [urls.py](../dcrm/website/urls.py).

```python
path('login', views.login_user, name='login'),
path('logout', views.logout_user, name='logout'),
```

### Login Form

In the following the login form is added to [home.html](../dcrm/website/templates/home.html) instead of a separate
login-template. Therefore the code is
slightliy different.
The following if-statement in django syntax checks if the user is authenticated (logged in).

```html
 {% if user.is_authenticated %}
<h1>Hello User</h1>

{% else %}
<h1>Login</h1>
<form method="POST" action="{% url 'home' %}">
    {% csrf_token %}
    <form>
        <div class="mb-3 mt-3">
            <input type="text" class="form-control" name="username" placeholder="Username" required>
        </div>
        <div class="mb-3">
            <input type="password" class="form-control" name="password" placeholder="Password" required>
        </div>
        <button type="submit" class="btn btn-secondary">Login</button>
    </form>
</form>
{% endif %}
```

### Logout

For logout the [navbar template](../dcrm/website/templates/navbar.html) is extended with a logout button. The url points
to the logout view.

```
{% if user.is_authenticated %}
    <li class="nav-item">
        <a class="nav-link" href="{% url 'logout' %}">Logout</a>
    </li>
{% endif %}
```

