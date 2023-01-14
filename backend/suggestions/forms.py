from django import forms
from .models import suggestions


class SearchForm(forms.Form):
    class Meta:
        model = suggestions
        fields = ('comments',)
