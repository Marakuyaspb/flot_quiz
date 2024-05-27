from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from gallery import views
from django.urls import reverse

app_name = 'gallery'


urlpatterns = [
    path('artgallery/', views.artgallery, name = 'artgallery'),
    path('gallery/', views.gallery, name = 'gallery'),
]