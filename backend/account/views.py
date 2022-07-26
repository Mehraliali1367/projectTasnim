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


class UserLogin(View):
    form_class = forms.UserLoginForm

    def get(self, request):
        form = self.form_class
        return render(request, 'account/login.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, serial=cd['serial'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, f'کاربر گرامی {user.full_name}', 'success')
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
            User.objects.create_user(cd['serial'], cd['full_name'], cd['tel'], cd['password'])
            messages.success(request, 'کاربر جدید اضافه شد', 'success')
            return redirect('core:home')
        else:
            return render(request, 'account/register.html', {'form': form})


class Profile(LoginRequiredMixin, UpdateView):
    form_class = forms.ProfileForms
    success_url = reverse_lazy('account:profile')
    template_name = 'account/profile.html'

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs


class Dashboard(View):
    template_name = 'account/dashboard.html'
    form_class = forms.ImagesForm

    def get(self, request, serial):
        user = get_object_or_404(User, serial=serial)
        return render(request, self.template_name, {'user': user, 'form': self.form_class})

    def post(self, request, serial):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            user = get_object_or_404(User, serial=serial)
            Images.objects.create(user=user, image=cd['img'])
            messages.success(request, 'your image updated successfully', 'info')
            return redirect('account:dashboard', user.serial)


class Edit(LoginRequiredMixin, AdminAccessMixin, UpdateView):
    form_class = forms.ProfileForms
    success_url = reverse_lazy('account:search')
    template_name = 'account/edit.html'

    def get_object(self):
        print("@" * 100)
        print(self.request)
        return User.objects.get(serial=self.request.GET["serial"])

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
