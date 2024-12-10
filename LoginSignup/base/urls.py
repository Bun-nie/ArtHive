from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = 'registration/login.html'), name='login'), # default
    # path('home/', home, name='home'),
    path('', landing, name='landing'),
    path('about/', aboutUs, name='about'),
    path("signup/", authView, name="authView"),
    path("profile/", userProfile, name='userProfile'), 
    path("artboard/", viewHoneycomb, name='honeycomb'),
    path("order-track/", viewOrderTrack, name='orderTrack')
]

# if settings.DEBUG:
#   urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# ^ to access profile picture. will change later.
