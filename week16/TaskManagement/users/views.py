from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, logout
from .authentication import MyAuthBackend
from django.contrib.auth.hashers import make_password

# Create your views here.


def register(request):
    message = None
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["password"] == form.cleaned_data["confirm_password"]:

                user = form.save(commit=False)
                user.password = make_password(form.cleaned_data["password"])
                user = form.save()
                request.session["register_session"] = user.username
                return redirect('home')
            else:
                message = "passwords don't match"
                form = RegisterForm()

    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form, "message": message})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    message = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        user = MyAuthBackend().authenticate(
            request,
            username=form["username_email"].value(),
            password=form["password"].value())
        if user is None:
            message = "username or password is invalid"
            form = LoginForm()
            return render(request, 'login.html', {'form': form, "message": message})

        login(request, user, backend='users.authentication.MyAuthBackend')
        request.session["login_session"] = user.username
        return redirect("home")

    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form, "message": message})


def logout_view(request):
    logout(request)
    return redirect("home")
