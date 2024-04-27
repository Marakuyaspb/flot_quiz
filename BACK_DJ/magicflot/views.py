from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Winner

def index(request):
	return render(request, 'magicflot/index.html')

def about(request):
	return render(request, 'magicflot/about.html')

def gallery(request):
	return render(request, 'magicflot/gallery.html')

def game(request):
	return render(request, 'magicflot/game.html')