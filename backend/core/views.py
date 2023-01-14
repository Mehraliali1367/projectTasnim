from django.shortcuts import render
from django.views import View
from account.models import User


# Create your views here.


class Home(View):
    def get(self, request):
        return render(request, 'core/home.html')

    def post(self):
        pass


class Messages(View):
    template_name = 'core/messages.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self):
        pass
