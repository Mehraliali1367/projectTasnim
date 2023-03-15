from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from . import forms
from django.contrib import messages
from .models import User, Images
from django.contrib.auth import authenticate, login, logout
from rest_framework.generics import ListAPIView, ListCreateAPIView
from .mixins import AdminAccessMixin
from django.contrib.auth.mixins import LoginRequiredMixin
import random
from kavenegar import *

def check_melli(melli):
    try:
        obj = User.objects.filter(melli=melli)
        if not obj:
            return True
        else:
            return False
    except:
        return False

class UserLogin(View):
    form_class = forms.UserLoginForm

    def get(self, request):
        form = self.form_class
        return render(request, 'account/login.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        print(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, melli=cd['melli'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(
                    request, f'کاربر گرامی {user.first_name} {user.last_name}', 'success')
                return redirect('core:home')
            else:
                messages.error(request, 'خطا در ورود به سیستم', 'danger')
                return redirect('account:login')

        else:
            return render(request, 'account/login.html', {'form': form})


class UserLogOut(View):
    def get(self, request):
        logout(request)
        messages.error(request, 'شما از سیستم خارج شدید', 'danger')
        return redirect('account:login')


class UserRegister(View):
    form_class = forms.UserRegistrationForm

    def get(self, request):
        form = self.form_class
        return render(request, 'account/register.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            melli = check_melli(cd['melli'])
            if melli:
                User.objects.create_user(cd['melli'], cd['serial'],cd['tel'], cd['last_name'], cd['first_name'], cd['year_brithday'],
                                         cd['password'])
                messages.success(request, 'کاربر جدید اضافه شد', 'success')
                return redirect('core:home')
            else:
                messages.warning(request, 'کاربر قبلا ثبت شده است', 'warning')
                return render(request, 'account/register.html', {'form': form})
        else:
            messages.error(request, 'ورودی ها را چک کنید', 'error')
            return render(request, 'account/register.html', {'form': form})


class Profile(LoginRequiredMixin, UpdateView):
    form_class = forms.ProfileForms
    success_url = reverse_lazy('core:home')

    template_name = 'account/profile.html'

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        # messages.success(self.request, 'تصویر با موفقیت بارگذاری شد', 'info')
        return kwargs


class Dashboard(View):
    template_name = 'account/dashboard.html'
    form_class = forms.ImagesForm

    def get(self, request, slug):
        user = get_object_or_404(User, slug=slug)
        return render(request, self.template_name, {'user': user, 'form': self.form_class})

    def post(self, request, slug):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            user = get_object_or_404(User, slug=slug)
            Images.objects.create(user=user, image=cd['img'])
            messages.success(request, 'تصویر با موفقیت بارگذاری شد', 'info')
            return redirect('account:dashboard', user.slug)


class Edit(LoginRequiredMixin, AdminAccessMixin, UpdateView):
    form_class = forms.ProfileForms
    success_url = reverse_lazy('account:search')
    template_name = 'account/edit.html'

    def get_object(self):
        return User.objects.get(melli=self.request.GET["melli"])

    def get_form_kwargs(self):
        kwargs = super(Edit, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs


class Search(LoginRequiredMixin, AdminAccessMixin, View):
    template_name = 'account/search.html'
    form_class = forms.SearchForm

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self):
        pass
