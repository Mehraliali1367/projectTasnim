from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from account.models import User


class Comments(LoginRequiredMixin, View):
    template_name = 'suggestions/suggestions.html'
    def get(self, request):
        return render(request, self.template_name)