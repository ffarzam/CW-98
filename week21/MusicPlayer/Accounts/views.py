from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, logout
from .authentication import AuthBackend
from django.contrib.auth.hashers import make_password
from .models import User, Artist
from django.views.generic import View
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.


def register(request):
    message = None
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            _type = cd["_type"]
            if _type == "user":
                obj = User.objects.create(username=cd["username"],
                                          email=cd["email"],
                                          password=make_password(cd["password"])
                                          )
            else:
                obj = Artist.objects.create(username=cd["username"],
                                            email=cd["email"],
                                            password=make_password(cd["password"])
                                            )
            subject = "Welcome Message"
            content = "Welcome to Our Website"
            send_mail(subject, content,
                      settings.DEFAULT_FROM_EMAIL, [obj.email])
            return redirect('home')

    if request.method == 'GET':
        form = RegisterForm()

        return render(request, 'auth/register.html', {'form': form, "message": message})


class Login(LoginView):
    redirect_authenticated_user = True
    form_class = LoginForm
    template_name = 'auth/login.html'
    success_url = "home"

    def form_valid(self, form):
        remember = form.cleaned_data["remember_me"]
        if remember:
            self.request.session.set_expiry(None)
        else:
            self.request.session.set_expiry(0)

        user = AuthBackend().authenticate(
            self.request,
            username=form["username_email"].value(),
            password=form["password"].value()
        )

        if user is None:
            message = "username/Email or password is invalid"
            form = LoginForm()
            return render(self.request, self.template_name, {'form': form, "message": message})
        login(self.request, user, backend='Accounts.authentication.AuthBackend')
        return redirect(self.success_url)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("home")
