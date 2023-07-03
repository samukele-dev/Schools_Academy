from django.urls import path
from .views import home, profile, RegisterView
from . import views

urlpatterns = [
    path('', home, name='users-home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.profile, name='profile'),
]
