from django import forms
from .models import CustomUser


class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        widgets = {"password": forms.PasswordInput}


class LoginForm(forms.ModelForm):
    username_email = forms.CharField(label='Username or Email',
                                     widget=forms.TextInput(attrs={
                                         'placeholder': 'Enter Your Username or Email Here'}))

    class Meta:
        model = CustomUser
        fields = ["username_email", "password"]
        widgets = {"password": forms.PasswordInput(attrs={'placeholder': 'Enter Your Password Here'})}
