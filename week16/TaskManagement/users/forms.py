from django import forms
from .models import CustomUser


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', ]


class LoginForm(forms.ModelForm):
    username_or_email = forms.CharField(label='Username or Email')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ["username_or_email","password"]