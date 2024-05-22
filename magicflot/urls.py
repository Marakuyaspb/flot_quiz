from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from magicflot import views
from django.urls import reverse
from magicflot import views
from .views import save_game_session

app_name = 'magicflot'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('game/', views.game, name = 'game'),
    path('get_win_sert/', views.get_win_sert, name='get_win_sert'),
    path('download_pdf/<int:pk>/', views.download_pdf, name='download_pdf'),
    path('save_game_session/', save_game_session, name='save_game_session'),
    path('stat/', views.stat, name = 'stat'),
]