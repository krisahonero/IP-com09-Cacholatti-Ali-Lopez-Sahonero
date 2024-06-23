# capa de vista/presentación
# si se necesita algún dato (lista, valor, etc), esta capa SIEMPRE se comunica con services_nasa_image_gallery.py

from django.shortcuts import redirect, render
from .layers.services import services_nasa_image_gallery
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView
from .models import Favourite

# función que invoca al template del índice de la aplicación.
def index_page(request):
    return render(request, 'index.html')

# auxiliar: retorna 2 listados -> uno de las imágenes de la API y otro de los favoritos del usuario.
def getAllImagesAndFavouriteList(request):
    images = services_nasa_image_gallery.getAllImages()
    favourite_list = []
   

    return images, favourite_list

# función principal de la galería.
def home(request):
    # llama a la función auxiliar getAllImagesAndFavouriteList() y obtiene 2 listados: uno de las imágenes de la API y otro de favoritos por usuario*.
    # (*) este último, solo si se desarrolló el opcional de favoritos; caso contrario, será un listado vacío [].
    images = []
    favourite_list = []
    images,favourite_list=getAllImagesAndFavouriteList(request)
    return render(request, 'home.html', {'images': images, 'favourite_list': favourite_list} )


# función utilizada en el buscador.
def search(request):
    images, favourite_list = getAllImagesAndFavouriteList(request)
    search_msg = request.POST.get('query', '')
    if search_msg!="":
        return render(request, 'home.html', {'images':services_nasa_image_gallery.getImagesBySearchInputLike(search_msg)  } )
    else:
        return(home(request)) 

    # si el usuario no ingresó texto alguno, debe refrescar la página; caso contrario, debe filtrar aquellas imágenes que posean el texto de búsqueda.



# las siguientes funciones se utilizan para implementar la sección de favoritos: traer los favoritos de un usuario, guardarlos, eliminarlos y desloguearse de la app.
# @login_required
# def getAllFavouritesByUser(request):
#     favourite_list = []
#     return render(request, 'favourites.html', {'favourite_list': favourite_list})


# @login_required
# def saveFavourite(request):
#     getAllFavouritesByUser = []
#     if getAllFavouritesByUser
#     pass


# @login_required
# def deleteFavourite(request):
#     pass


# @login_required
# def exit(request):
#     pass


@login_required
def getAllFavouritesByUser(request):
    favourite_list = Favourite.objects.filter(user=request.user)
    return render(request, 'favourites.html', {'favourite_list': favourite_list})

@login_required
def saveFavourite(request):
    if request.method == 'POST':
        image_url = request.POST.get('image_url')
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('date')
        Favourite.objects.create(
            user=request.user,
            image_url=image_url,
            title=title,
            description=description,
            date=date
        )
    return redirect('favoritos')

@login_required
def deleteFavourite(request):
    if request.method == 'POST':
        fav_id = request.POST.get('id')
        favourite = Favourite.objects.get(id=fav_id, user=request.user)
        favourite.delete()
    return redirect('favoritos')


@login_required
def exit(request):
    logout(request)
    return redirect('exit')