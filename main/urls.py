from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nasa_image_gallery.urls')),
    path('accounts/', include('django.contrib.auth.urls')),#agrege este path en el directorio main que según averigué, maneja el sistema de usuarios de Django

=======
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nasa_image_gallery.urls'))
>>>>>>> 5e03a3cc133e80fd231124345780da1d287b7343
]