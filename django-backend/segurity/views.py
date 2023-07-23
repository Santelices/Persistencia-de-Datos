from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

# Create your views here.
class HomeView(LoginRequiredMixin, View):
    login_url = '/segurity/login'
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        data = {
            'title': "Home web"
        }
        return render(request, 'segurity/index.html', data)
