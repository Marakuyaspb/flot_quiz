from django.db import models

class ArtWorkCategory(models.Model):
	id = models.AutoField(primary_key=True)
	art_category = models.CharField(max_length=50)

	class Meta:
		ordering = ['art_category']
		verbose_name = 'Категория работы'
		verbose_name_plural = 'Категории работ'	

	def __str__(self):
		return self.art_category



class ArtWork(models.Model):
	id = models.AutoField(primary_key=True)
	art_category = models.ForeignKey(
		ArtWorkCategory,
		related_name='artwork',
		on_delete=models.CASCADE, verbose_name = 'Категория')
	trumb = models.ImageField(upload_to='trumb/', verbose_name = 'Миниатюра')
	img = models.ImageField(upload_to='gallery/', verbose_name = 'Путь к картинке')
	description = models.TextField(null=True, blank=True, verbose_name = 'Аннотация работы')

	class Meta:
		verbose_name = 'Работа'
		verbose_name_plural = 'Работы'

	def __str__(self):
		return self.description