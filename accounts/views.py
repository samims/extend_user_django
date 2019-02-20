from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView

from .forms import UserCreateForm
from .models import User


class CustomLoginView(LoginView):
    model = User
    template_name = 'accounts/login.htm'


class IndexView(TemplateView):
    template_name = 'accounts/index.htm'


class SignupView(CreateView):
    model = User
    form_class = UserCreateForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'
