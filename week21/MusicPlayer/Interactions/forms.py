from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    # song = forms.CharField(widget=forms.HiddenInput(attrs={"value": "{{song.id}}"}), required=False)

    class Meta:
        model = Comment
        fields = ['content']
        widgets = {"content": forms.TextInput(attrs={'class': 'form-control', "style": "height:150px"})}
