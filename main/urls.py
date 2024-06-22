from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nasa_image_gallery.urls')),
    path('accounts/', include('django.contrib.auth.urls')),#agrege este path en el directorio main que según averigué, maneja el sistema de usuarios de Django

]