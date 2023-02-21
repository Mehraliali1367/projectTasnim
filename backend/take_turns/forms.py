from django import forms
from .models import Doctor, Presence, Visit,Services


class DoctorForm(forms.ModelForm):
    name = forms.CharField(label='نام پزشک', widget=forms.TextInput(attrs={'class': 'form-control'}))
    CHOICES= (
        ('1','ME'),
        ('2','YOU'),
        ('3','WE'),
    )
    select = forms.ChoiceField(label='رسته پزشک',widget=forms.Select, choices=CHOICES)

    status = forms.BooleanField(label='وضعیت', widget=forms.CheckboxInput(attrs={'class': 'form-check'}))

    class Meta:
        model = Doctor
        fields = ('name','select')


class PresenceForm(forms.ModelForm):
    class Meta:
        model = Presence
        fields = ('doctor', 'datetime_persian', 'from_hour', 'to_hour', 'interval_sick')
        # fields = ('__exclude__')


class ServicesForm(forms.ModelForm):
    service = forms.CharField(label='خدمت', widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Services
        fields = ("service",)


class SearchForm(forms.Form):
    txt = forms.CharField(label='جستجو',widget=forms.TextInput(attrs={'class':'form-control'}))