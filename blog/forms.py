from django import forms
from .models import Review


class CreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'content')