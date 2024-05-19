from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from magicflot import views
from django.urls import reverse
#from .views import save_game_session_data


app_name = 'magicflot'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('game/', views.game, name = 'game'),
    path('get_win_sert/', views.get_win_sert, name='get_win_sert'),
    path('download_pdf/<int:pk>/', views.download_pdf, name='download_pdf'),
    path('statistic/', views.statistic_view, name = 'statistic'),
    #path('save_game_session_data/', save_game_session_data, name='save_game_session_data'),
]