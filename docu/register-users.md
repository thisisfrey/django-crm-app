# Register Users

## Add registration url

Add the register-path to [urls.py](../dcrm/website/urls.py):

```python
urlpatterns = [
    path('register', views.register_user, name='register')
]
```

## Add registration view

Add the register-user-view to [views.py](../dcrm/website/views.py):

```python
def register_user(request):
    return render(request, 'register.html', {})
```

## Create registration form

Create a sign-up form for the user registration [forms.py](../dcrm/website/forms.py) with the following content:

- username
- email
- first name
- last name
- password (x2)

## Create registration template

Create template [register.html](../dcrm/website/templates/register.html) which renders the form with ` {{ form.as_p }}`.

In the views the form is imported and passed to the template:

```python
from .forms import SignUpForm


def register_user(request):
    if request.method == 'POST':
        # when user sent form
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
    else:
        # show registration form
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})
```