import os
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template


def gallery(request):
	return render(request, 'gallery/gallery.html')

def gallery_history(request):
	return render(request, 'gallery/gallery_history.html')

def gallery_modern(request):
	return render(request, 'gallery/gallery_modern.html')