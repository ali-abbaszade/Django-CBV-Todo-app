from django.urls import path
from .views import RegisterUser, CustomLoginView

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/' ,RegisterUser.as_view(), name='register'),
    path('login/' ,CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
