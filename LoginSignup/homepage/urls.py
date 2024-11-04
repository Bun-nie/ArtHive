from django.urls import include, path
from django.contrib.auth  import views as authView
from . import views

app_name = 'base'

urlpatterns = [
    path(' ', views.gallery, name='gallery'),
    # path('homepage/', views.gallery, name='homepage'),    
    path('homepage/<str:pk>/', views.viewArtwork, name='view_artwork'),
    path('add/', views.addArtwork, name='add_artwork')
]