from django import forms
from .models import Base


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
