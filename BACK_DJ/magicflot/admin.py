from django.contrib import admin
from .models import Winner
from django.utils.safestring import mark_safe
from django.template.loader import get_template
from django.db import models


# Register your models here.
@admin.register(Winner)
class WinnerAdmin(admin.ModelAdmin):
	list_display = ['last_name', 'first_name', 'school', 'the_class']
	list_filter = ['school', 'the_class']