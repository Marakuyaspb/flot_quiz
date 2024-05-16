from django.contrib import admin
from .models import Category, Question, Winner
from django.utils.safestring import mark_safe
from django.template.loader import get_template
from django.db import models


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['category', ]
	list_filter = ['category', ]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
	list_display = ['question', 'category', 'answer_1', 'value_1', 'answer_2', 'value_2', 'answer_3', 'value_3', 'answer_4', 'value_4' ]
	list_filter = ['question', ]
