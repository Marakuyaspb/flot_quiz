import os
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template
from django.conf import settings

from .models import ArtWork
from .forms import CategoryForm



def artgallery(request):
	artworks = ArtWork.objects.all()
	art_category = request.GET.get('art_category')

	if art_category:
		art_category = int(art_category)
		if art_category == 1:
			artworks = ArtWork.objects.filter(art_category=1)
		elif art_category == 2:
			artworks = ArtWork.objects.filter(art_category=2)

	category_form = CategoryForm()
	context = {'artworks':artworks,'category_form': category_form}

	return render(request, 'gallery/artgallery.html', context)




def gallery(request):
	artworks = ArtWork.objects.all()
	art_category = request.GET.get('art_category')

	if art_category == 1:
		artworks = Artwork.objects.filter(art_category=1)
	elif art_category == 2:
		artworks = Artwork.objects.filter(art_category=2)

	category_form = CategoryForm()
	context = {'artworks':artworks,'category_form': category_form}

	return render(request, 'gallery/gallery.html', context)




# def gallery_history(request):
# 	artworks = ArtWork.objects.all()
# 	context = {'artworks':artworks,}
# 	return render(request, 'gallery/gallery_history.html', context)


# def gallery_modern(request):
# 	artworks = ArtWork.objects.all()
# 	context = {'artworks':artworks,}
# 	return render(request, 'gallery/gallery_modern.html')