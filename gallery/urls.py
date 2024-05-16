from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from gallery import views
from django.urls import reverse

app_name = 'gallery'


urlpatterns = [
    path('gallery/', views.gallery, name = 'gallery'),
    path('gallery/gallery_history/', views.gallery_history, name = 'gallery_history'),
    path('gallery/gallery_modern/', views.gallery_modern, name = 'gallery_modern'),
]