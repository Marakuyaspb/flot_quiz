from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from magicflot import views
from django.urls import reverse


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('gallery/', views.gallery, name = 'gallery'),
    path('game/', views.game, name = 'game'),
    path('get_win_sert/', views.get_win_sert, name='get_win_sert'),
    path('download_pdf/<int:pk>/', views.download_pdf, name='download_pdf'),
]