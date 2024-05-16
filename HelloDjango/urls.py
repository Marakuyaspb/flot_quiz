from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from magicflot import urls
from gallery import urls

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('magicflot.urls')),
    path('', include('gallery.urls')),
]