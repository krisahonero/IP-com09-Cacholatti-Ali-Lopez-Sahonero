from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index-page'),
    path('login/', views.login, name='login'), #se cambió views.index_page por views.login para llamar a la vista de la funcion login que se agregó en VIEWS.PY
    path('home/', views.home, name='home'),
    path('buscar/', views.search, name='buscar'),
    path('favourites/', views.getAllFavouritesByUser, name='favoritos'),
    path('favourites/add/', views.saveFavourite, name='agregar-favorito'),
    path('favourites/delete/', views.deleteFavourite, name='borrar-favorito'),
    path('exit/', views.exit, name='exit'),
]