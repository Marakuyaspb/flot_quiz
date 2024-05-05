from django.db import models
from django.conf import settings


# QUESTIONS

class Category(models.Model):
	id = models.AutoField(primary_key=True)
	category = models.CharField(max_length=50)

	class Meta:
		ordering = ['category']
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'	

	def __str__(self):
		return self.category


class Question(models.Model):
	id = models.AutoField(primary_key=True)
	question = models.CharField(max_length=300, verbose_name = 'Вопрос')
	category = models.ForeignKey(
		Category,
		related_name='question',
		on_delete=models.CASCADE, verbose_name = 'Категория')
	icon = models.ImageField(upload_to='q_icons/', verbose_name ='Иконка')
	answer_1 = models.CharField(max_length=100, null=True, verbose_name = 'Ответ 1')
	value_1 = models.BooleanField(null=True,default=False, verbose_name = 'Верно?')
	answer_2 = models.CharField(max_length=100, null=True, verbose_name = 'Ответ 2')
	value_2 = models.BooleanField(null=True, default=False, verbose_name = 'Верно?')
	answer_3 = models.CharField(max_length=100, null=True, verbose_name = 'Ответ 3')
	value_3 = models.BooleanField(null=True, default=False, verbose_name = 'Верно?')
	answer_4 = models.CharField(max_length=100, null=True, verbose_name = 'Ответ 4')
	value_4 = models.BooleanField(null=True,default=False, verbose_name = 'Верно?')

	class Meta:
		verbose_name = 'Вопрос'
		verbose_name_plural = 'Вопросы'

	def __str__(self):
		return self.question



# WINNERS

class Winner (models.Model):
	id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=30, verbose_name = 'Имя')
	last_name = models.CharField(max_length=30, verbose_name = 'Фамилия')
	school = models.CharField(max_length=30, verbose_name = 'Школа')
	the_class = models.CharField(max_length=30, verbose_name = 'Класс')

	class Meta:
		ordering = ['last_name']
		indexes = [
			models.Index(fields=['last_name']),
		]
		verbose_name = 'Фамилия'
		verbose_name_plural = 'Фамилии'	

	def __str__(self):
		return self.last_name