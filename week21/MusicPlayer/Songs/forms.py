from django import forms
from .models import Song, Genre
from Accounts.models import Artist


class SongUploadForm(forms.ModelForm):
    genre = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(), widget=forms.SelectMultiple(
        attrs={"id": "dselect-genre"}))
    other_artists = forms.ModelMultipleChoiceField(label="Other Artists", queryset=Artist.objects.all(),
                                                   widget=forms.SelectMultiple(attrs={"id": "dselect-other_artists"}),
                                                   required=False)

    class Meta:
        model = Song
        fields = ['title', 'audio_file', 'cover_photo', "genre", "other_artists"]
        widgets = {"title": forms.TextInput(attrs={'class': 'form-control'}),

                   "audio_file": forms.FileInput(
                       attrs={'class': 'form-control', "accept": "audio/*"}),
                   "cover_photo": forms.FileInput(
                       attrs={'class': 'form-control', "accept": "image/*"})}
