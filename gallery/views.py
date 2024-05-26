import os
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template
from django.conf import settings

from .models import ArtWorkCategory, ArtWork


def gallery(request):
	return render(request, 'gallery/gallery.html')


def gallery_history(request):
	artworks = ArtWork.objects.all()
	context = {'artworks':artworks,}
	return render(request, 'gallery/gallery_history.html', context)


def gallery_modern(request):
	artworks = ArtWork.objects.all()
	context = {'artworks':artworks,}
	return render(request, 'gallery/gallery_modern.html')
