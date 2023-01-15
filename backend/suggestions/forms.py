from django import forms
from .models import QuesModel


# class QuestionForm(forms.Form):
#     STATUS_CHOICES = (
#         ('a', 'کاملا راضی'),
#         ('b', 'راضی'),
#         ('c', 'ناراضی'),
#         ('d', 'کاملا ناراضی'),
#     )
#     STATUS_Clark = (
#         ('c1', 'کاملا راضی'),
#         ('c2', 'راضی'),
#         ('c3', 'ناراضی'),
#     )
#     s1 = forms.CharField(label='1-کد پرسنلی منشی پاسخگو', widget=forms.RadioSelect(choices=STATUS_Clark,
#         attrs={'class': 'form-check-label'}))

class addQuestionform(forms.ModelForm):
    class Meta:
        model=QuesModel
        fields=('question','op1','op2','op3','op4')