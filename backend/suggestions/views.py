from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from account.models import User


class Comments(LoginRequiredMixin, DetailView):
    template_name = 'suggestions/suggestions.html'

    def get_object(self,**kwargs):
        return get_object_or_404(User.objects.filter(id=1))
