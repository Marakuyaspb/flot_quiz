import os
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template
from django.conf import settings


def gallery(request):
	return render(request, 'gallery/gallery.html')


def gallery_history(request):
	history_dir = os.path.join(settings.BASE_DIR, 'static/img/gallery/history')
	pics_h = [f for f in os.listdir(history_dir) if f.endswith('.jpg')]

	return render(request, 'gallery/gallery_history.html', {'pics_h':pics_h,})


def gallery_modern(request):
	modern_dir = os.path.join(settings.BASE_DIR, 'static/img/gallery/modern')
	pics_m = [f for f in os.listdir(modern_dir) if f.endswith('.jpg')]

	return render(request, 'gallery/gallery_modern.html', {'pics_m':pics_m,})
