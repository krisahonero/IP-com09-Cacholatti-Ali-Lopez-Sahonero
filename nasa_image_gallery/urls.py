from django.contrib import admin
from django.urls import path
from . import views
<<<<<<< HEAD

urlpatterns = [
    path('', views.index_page, name='index-page'),
   # path('login/', views.login, name='login'), #se cambió views.index_page por views.login para llamar a la vista de la funcion login que se agregó en VIEWS.PY
    path('home/', views.home, name='home'),
    path('buscar/', views.search, name='buscar'),
    path('favourites/', views.getAllFavouritesByUser, name='favoritos'),
    path('favourites/add/', views.saveFavourite, name='agregar-favorito'),
    path('favourites/delete/', views.deleteFavourite, name='borrar-favorito'),
    path('exit/', views.exit, name='exit'),
]
=======
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index_page, name='index-page'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    #                                                   ruta del login, vista del login redirr. 
    path('home/', views.home, name='home'),
    path('buscar/', views.search, name='buscar'),

    path('favourites/', views.getAllFavouritesByUser, name='favoritos'),
    path('favourites/add/', views.saveFavourite, name='agregar-favorito'),
    path('favourites/delete/', views.deleteFavourite, name='borrar-favorito'),

    path('exit/', LogoutView.as_view(next_page='index-page'), name='exit'),
]
#                        log out view
>>>>>>> 5e03a3cc133e80fd231124345780da1d287b7343
