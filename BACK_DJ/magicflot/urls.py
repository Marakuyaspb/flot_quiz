from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import reverse


app_name = 'magicflot'


# urlpatterns = [
#     path('', views.index, name = 'index'),
#     path('about/', views.about, name = 'about'),
#     path('gallery/', views.gallery, name = 'gallery'),
#     path('game/', views.game, name = 'game')
# ]