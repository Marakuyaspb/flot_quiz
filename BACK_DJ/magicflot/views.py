from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Category
import random


def index(request):
	return render(request, 'magicflot/index.html')

def about(request):
	return render(request, 'magicflot/about.html')

def gallery(request):
	return render(request, 'magicflot/gallery.html')


def display_question_details(request, question_id):
	question = Question.objects.get(id=question_id)
	return render(request, 'question_details.html', {'question': question})


def game(request):
    general_questions = Question.objects.filter(category__category='general').order_by('?')[:8]
    technical_questions = Question.objects.filter(category__category='technical').order_by('?')[:7]

    questions = list(general_questions) + list(technical_questions)
    random.shuffle(questions)
    selected_questions = random.sample(questions, 15)

    context = {
        'questions': selected_questions
    }

    return render(request, 'magicflot/game.html', context)