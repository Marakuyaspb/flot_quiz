from django.db import models

# Create your models here.
class Winner (models.Model):
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