from django import forms
from .models import User, Images
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='رمز', widget=forms.PasswordInput)
    password2 = forms.CharField(label='تکرار رمز', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('serial', 'melli', 'full_name', 'brithday', 'tel')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise forms.ValidationError('passwords must match')
        return cd['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('serial', 'melli', 'full_name', 'tel', 'brithday', 'place', 'password')

    def clean_password(self):
        return self.initial['password']


class UserLoginForm(forms.Form):
    serial = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegistrationForm(forms.Form):
    serial = forms.CharField(label='سریال', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'برای وارد کردن سریال با رادیولوژی هماهنگ کنید'}))
    full_name = forms.CharField(label='نام کامل', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'مثال: مرتضی حسینی'}))
    tel = forms.CharField(label='موبایل',
                          widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'مثال: 09123541289'}))
    password = forms.CharField(label='رمز', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserUpdate(forms.Form):
    serial = forms.CharField(label='سریال', disabled=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    melli = forms.CharField(label='کدملی', disabled=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    full_name = forms.CharField(label='نام کامل', widget=forms.TextInput(attrs={'class': 'form-control'}))
    brithday = forms.IntegerField(label='تاریخ تولد',
                             widget=forms.TextInput(attrs={'class': 'normal-example form-control '}))
    tel = forms.CharField(label='موبایل', widget=forms.TextInput(attrs={'class': 'form-control'}))
    place = forms.CharField(label='محل سکونت', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        fields = ('serial', 'melli', 'full_name', 'age', 'tel', 'place')


class ProfileForms(forms.ModelForm):
    serial = forms.CharField(label='سریال', widget=forms.TextInput(attrs={'class': 'form-control'}))
    melli = forms.CharField(label='کدملی', widget=forms.TextInput(attrs={'class': 'form-control'}))
    full_name = forms.CharField(label='نام کامل', widget=forms.TextInput(attrs={'class': 'form-control'}))
    brithday = forms.IntegerField(label='تاریخ تولد',
                             widget=forms.TextInput(attrs={'class': 'on-select-example form-control '}))
    tel = forms.CharField(label='موبایل', widget=forms.TextInput(attrs={'class': 'form-control'}))
    place = forms.CharField(label='محل سکونت', widget=forms.TextInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(ProfileForms, self).__init__(*args, **kwargs)

        # self.fields['serial'].help_text = None
        self.fields['serial'].disabled = True
        if not user.is_admin:
            self.fields['serial'].disabled = True

    class Meta:
        model = User
        fields = ('serial', 'melli', 'full_name', 'brithday', 'tel', 'place')


class ImagesForm(forms.Form):
    img = forms.ImageField(label='تصویر')


class SearchForm(forms.Form):
    txt = forms.CharField(label='جستجو',widget=forms.TextInput(attrs={'class':'form-control'}))
