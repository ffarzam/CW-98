from django import forms
from .models import Base, User, Artist
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class BaseCreationForm(UserCreationForm):
    class Meta:
        model = Base
        fields = ('username', 'email', 'name', "password1", "password2")


class BaseChangeForm(UserChangeForm):
    class Meta:
        model = Base
        fields = ['username', 'name', 'email', ]


class BaseUpdateForm(forms.ModelForm):
    class Meta:
        model = Base
        fields = ['username', 'name', 'email', ]
        widgets = {"username": forms.TextInput(attrs={'class': 'form-control'}),
                   "name": forms.TextInput(attrs={'class': 'form-control'}),
                   "email": forms.EmailInput(attrs={'class': 'form-control'}),
                   }


class MyUserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'name', 'email', 'image']
        widgets = {"username": forms.TextInput(attrs={'class': 'form-control'}),
                   "name": forms.TextInput(attrs={'class': 'form-control'}),
                   "email": forms.EmailInput(attrs={'class': 'form-control'}),
                   "image": forms.FileInput(
                       attrs={'class': 'form-control', "accept": "image/*"})}


class ArtistUpdateForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['username', 'name', 'email', 'bio', 'image']
        widgets = {"username": forms.TextInput(attrs={'class': 'form-control'}),
                   "name": forms.TextInput(attrs={'class': 'form-control'}),
                   "bio": forms.Textarea(attrs={'class': 'form-control'}),
                   "email": forms.EmailInput(attrs={'class': 'form-control'}),
                   "image": forms.FileInput(
                       attrs={'class': 'form-control', "accept": "image/*"})}


class RegisterForm(forms.ModelForm):
    CHOICES = (
        ('user', 'user'),
        ('artist', 'artist')
    )

    confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(
        attrs={'class': 'form-control text-light bg-dark', 'placeholder': 'Confirm Your Password Here'}))

    _type = forms.ChoiceField(label="Type", choices=CHOICES, required=True, widget=forms.Select(
        attrs={'class': 'form-control text-light bg-dark'}))

    class Meta:
        model = Base
        fields = ['username', 'email', 'password']
        widgets = {"password": forms.PasswordInput(
            attrs={'class': 'form-control text-light bg-dark', 'placeholder': 'Enter Your Password Here'}),
            "username": forms.TextInput(
                attrs={'class': 'form-control text-light bg-dark', 'placeholder': 'Enter Your Username Here'}),
            "email": forms.TextInput(
                attrs={'class': 'form-control text-light bg-dark', 'placeholder': 'Enter Your Email Here'}),
        }
        help_texts = {
            'username': None,
        }

        def clean(self):
            cleaned_data = super().clean()

            _type = cleaned_data.get("_type")
            username = cleaned_data.get("username")
            email = cleaned_data.get("email")

            if Base.objects.filter(username=username).exists() or Base.objects.filter(email=username).exists():
                raise forms.ValidationError("Username Already Exists!")

            if Base.objects.filter(username=email).exists() or Base.objects.filter(email=email).exists():
                raise forms.ValidationError("Email Already Exists!")

            if cleaned_data["password"] != cleaned_data["confirm_password"]:
                raise forms.ValidationError("passwords don't match")

            return cleaned_data


class LoginForm(forms.Form):
    username_email = forms.CharField(label='Username or Email',
                                     widget=forms.TextInput(attrs={'class': 'form-control text-light bg-dark',
                                                                   'placeholder': 'Enter Your Username or Email Here'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control text-light bg-dark', 'placeholder': 'Enter Your Password Here'}))

    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={"class": "form-check-input", "type": "checkbox"}))

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)
