from django.urls import include, path
from .views import gallery, viewArtwork, addArtwork

app_name = 'base'

urlpatterns = [
    path('', gallery, name='gallery'),
    # path('homepage/', views.gallery, name='gallery'),
    path('views/<int:pk>/', viewArtwork, name='view_artwork'),
    path('add/', addArtwork, name='add_artwork')
]