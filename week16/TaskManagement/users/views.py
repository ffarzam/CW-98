from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, logout
from .authentication import MyAuthBackend

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
            user = MyAuthBackend().authenticate(
                request,
                username=form.cleaned_data["username_or_email"],
                password=form.cleaned_data["password"])
            if user is None:
                message = "user or passwords is invalid"
                return render(request, 'login.html', {'form': form, "message": message})

            login(request, user, backend='users.authentication.MyAuthBackend')
            return redirect("home")

    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form, "message": message})


def logout_view(request):
    logout(request)
    return redirect("home")
