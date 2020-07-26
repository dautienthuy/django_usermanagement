from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
from users.forms import CustomUserCreationForm


def dashboard(request):
    return render(request, 'users/dashboard.html')


def register(request):
    # If the view is displayed by a browser, then it will be accessed by a GET method.
    # In that case, a template called users/register.html will be rendered. The last argument
    # of .render() is a context, which in this case contains your custom user creation form.
    if request.method == 'GET':
        return render(
            request, 'users/register.html',
            {'form': CustomUserCreationForm}
        )
    # If the form is submitted, then the view will be accessed by a POST method. In that case,
    # Django will attempt to create a user. A new CustomUserCreationForm is created using the
    # values submitted to the form, which are contained in the request.POST object.
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # If the form is valid, then a new user is created using form.save()
            user = form.save()
            # login the user using login
            login(request, user)
            # redirect the user to the dashboard
            return redirect(reverse('dashboard'))
