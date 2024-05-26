from django.contrib import admin
from .models import ArtWorkCategory, ArtWork


@admin.register(ArtWorkCategory)
class ArtWorkCategoryAdmin(admin.ModelAdmin):
	list_display = ['art_category', ]
	list_filter = ['art_category', ]


@admin.register(ArtWork)
class ArtWorkAdmin(admin.ModelAdmin):
	list_display = ['art_category', 'trumb', 'img', 'description']
	list_filter = ['art_category', 'description']