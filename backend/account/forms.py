from django import forms
from .models import User, Images
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='رمز', widget=forms.PasswordInput)
    password2 = forms.CharField(label='تکرار رمز', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('melli', 'first_name', 'last_name','year_brithday', 'tel')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise forms.ValidationError('رمز و تایید رمز باید برابر باشند')
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
        fields = ('melli', 'first_name', 'last_name','tel', 'year_brithday', 'place', 'password')

    def clean_password(self):
        return self.initial['password']


class UserLoginForm(forms.Form):
    melli = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegistrationForm(forms.Form):
    melli = forms.CharField(label='کدملی/اتباع/گذرنامه',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'مثال: 0386022775'}))
    tel = forms.CharField(label='موبایل', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'مثال: 09123541289'}))
    first_name = forms.CharField(label='نام', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'مثال: مرتضی'}))
    last_name = forms.CharField(label='نام خانوادگی', widget=forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'مثال: حسینی'}))
    year_brithday = forms.CharField(label='سال تولد', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'مثال: 1350'}))
    password = forms.CharField(label='رمز', widget=forms.TextInput(attrs={'class': 'form-control'}), initial="1111")
    # place = forms.CharField(label='آدرس', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'مثال: باجک'}),initial='قم')
    # serial = forms.CharField(label='سریال', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'برای وارد کردن سریال با رادیولوژی هماهنگ کنید'}))

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        # self.fields['melli'].required = False
        # self.fields['place'].required = False


class UserUpdate(forms.Form):
    # serial = forms.CharField(label='سریال', disabled=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    melli = forms.CharField(label='کدملی/اتباع/گذرنامه', disabled=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='نام', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='نام خانوادگی', widget=forms.TextInput(attrs={'class': 'form-control'}))
    year_brithday = forms.IntegerField(label='تاریخ تولد',widget=forms.TextInput(attrs={'class': 'normal-example form-control '}))
    tel = forms.CharField(label='موبایل', widget=forms.TextInput(attrs={'class': 'form-control'}))
    place = forms.CharField(label='محل سکونت', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        fields = ('melli', 'first_name', 'last_name','year_brithday', 'tel', 'place')


class ProfileForms(forms.ModelForm):
    # serial = forms.CharField(label='سریال', widget=forms.TextInput(attrs={'class': 'form-control'}))
    melli = forms.CharField(label='کدملی/اتباع/گذرنامه', widget=forms.TextInput(attrs={'class': 'form-control'}))
    tel = forms.CharField(label='موبایل', widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='نام', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='نام خانوادگی', widget=forms.TextInput(attrs={'class': 'form-control'}))
    year_brithday = forms.IntegerField(label='تاریخ تولد',
                                  widget=forms.TextInput(attrs={'class': 'on-select-example form-control '}))
    # place = forms.CharField(label='محل سکونت', widget=forms.TextInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(ProfileForms, self).__init__(*args, **kwargs)

        # self.fields['serial'].help_text = None
        self.fields['melli'].disabled = False
        if not user.is_admin:
            self.fields['melli'].disabled = True

    class Meta:
        model = User
        fields = ('melli', 'last_name', 'first_name','year_brithday', 'tel')


class ImagesForm(forms.Form):
    img = forms.ImageField(label='تصویر')


class SearchForm(forms.Form):
    txt = forms.CharField(label='جستجو', widget=forms.TextInput(attrs={'class': 'form-control'}))
