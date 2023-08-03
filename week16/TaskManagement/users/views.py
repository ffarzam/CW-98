from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout

# Create your views here.


def register(request):
    message = None
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["password"] == form.cleaned_data["confirm_password"]:
                form.save()
                return redirect('home')
            else:
                message = "passwords don't match"

    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form, "message": message})


def login_view(request):
    message = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print("1"*100)
            user = authenticate(
                username=form.cleaned_data["username_or_email"],
                password=form.cleaned_data["password"])
            if user is None:
                print("2" * 100)
                user = authenticate(
                    email=form.cleaned_data["username_or_email"],
                    password=form.cleaned_data["password"])
                if user is None:
                    print("3" * 100)
                    message = "user or passwords is invalid"
                    return render(request, 'register.html', {'form': form, "message": message})
            login(request, user)
            return redirect("home")

    else:
        form = LoginForm()
        return render(request, 'register.html', {'form': form, "message": message})

