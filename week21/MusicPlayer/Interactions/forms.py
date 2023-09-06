from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    # song = forms.CharField(widget=forms.HiddenInput(attrs={"value": "{{song.id}}"}), required=False)

    class Meta:
        model = Comment
        fields = ['content']
        widgets = {"content": forms.Textarea(attrs={'class': 'form-control', })}
