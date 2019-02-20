from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import CustomLoginView, IndexView, SignupView

app_name = 'accounts'

urlpatterns = [
    path('', IndexView.as_view(), name="account_list"),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup')
]
