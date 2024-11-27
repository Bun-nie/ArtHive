from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import authView, home, landing, aboutUs

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = 'registration/login.html'), name='login'), # default
    # path('home/', home, name='home'),
    path('', landing, name='landing'),
    path('about/', aboutUs, name='about'),
    path("signup/", authView, name="authView"),
]