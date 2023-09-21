
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'), 
    path('contact', views.contact, name='contact'), 
    path('episodes/<seasonNumber>', views.episodes, name='Episodes'),
    path('details/<seasonNumber>/<epNum>', views.episDetails, name='Details'),
    path('actors', views.actors, name='Actors'),
]

