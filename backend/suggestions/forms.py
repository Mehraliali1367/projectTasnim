from django import forms
from .models import QuesModel


class Questionform(forms.ModelForm):
    class Meta:
        model = QuesModel
        fields = ('question', 'op1', 'op2', 'op3', 'op4')
