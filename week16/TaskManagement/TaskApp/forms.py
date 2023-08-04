from django import forms
from .models import Task, Tag


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', "status", "category", "tag", "file"]

        widgets = {'due_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
                   'title': forms.TextInput(attrs={'class': 'form-control'}),
                   'description': forms.Textarea(attrs={'class': 'form-control'}),
                   "status": forms.Select(attrs={'class': 'form-control'}),
                   "category": forms.Select(attrs={'class': 'form-control'}),
                   "tag": forms.SelectMultiple(attrs={'class': 'form-control'}),
                   "file": forms.FileInput(attrs={'class': 'form-control'}), }


class CreateTagForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
