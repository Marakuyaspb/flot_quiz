import random
from xhtml2pdf import pisa
import matplotlib.pyplot as plt
from urllib.parse import quote

from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

import os
from django.urls import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template

from .models import Category, Question, Statistic, Winner
from .forms import WinnerForm


def error_404_view(request, exception):
	return render(request, 'magicflot/404.html', status=404)
def error_500(request):
	return render(request, 'magicflot/500.html', status=500)


def index(request):
	return render(request, 'magicflot/index.html')

def about(request):
	return render(request, 'magicflot/about.html')


# GAME
def display_question_details(request, question_id):
	question = Question.objects.get(id=question_id)
	return render(request, 'question_details.html', {'question': question})


def game(request):
	general_questions = Question.objects.filter(category__category='general').order_by('?')[:8]
	technical_questions = Question.objects.filter(category__category='technical').order_by('?')[:7]

	questions = list(general_questions) + list(technical_questions)

	if len(questions) < 15:
		# Adjust the number of questions retrieved if needed
		all_questions = Question.objects.all().order_by('?')[:15]
		selected_questions = list(all_questions)
	else:
		random.shuffle(questions)
		selected_questions = random.sample(questions, 15)

	context = {
		'questions': selected_questions
	}
	return render(request, 'magicflot/game.html', context)



# PDF


def get_win_sert(request):
	if request.method == 'POST':
		winner_form = WinnerForm(request.POST)
		if winner_form.is_valid():
			winner = winner_form.save()
			return redirect('download_pdf', pk=winner.pk)
	else:
		winner_form = WinnerForm()
	return render(request, 'magicflot/get_win_sert.html', {'winner_form': winner_form})


def download_pdf(request, pk):
	winner = Winner.objects.get(pk=pk)
	template_path = 'magicflot/pdf.html'
	context = {
		'winner': winner,
		'logo_url': 'https://городволшебныхкораблей.рф/static/logo_blue.png',
		'stamp_url': 'https://городволшебныхкораблей.рф/static/img/stamp.png',
		'back_sert_url': quote('https://городволшебныхкораблей.рф/static/img/back_sert.png'),
	}
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = f'attachment; filename="certificate_{winner.last_name}_{winner.first_name}.pdf"'
	template = get_template(template_path)
	html = template.render(context)
	pisa_status = pisa.CreatePDF(html, dest=response)
	if pisa_status.err:
		return HttpResponse('<pre>' + html + '</pre>')
	return response




# CREATE SOME STATISTIC

# def save_game_session(request):
# 	if request.method == 'POST':
# 		data = json.loads(request.body)
# 		game_session_data = data.get('data')

# 		# Save the game session data to a JSON file on the server
# 		with open('game_sessions.json', 'a') as file:
# 			file.write(game_session_data + '\n')

# 		return JsonResponse({'message': 'Game session data saved successfully.'})

# 	return JsonResponse({'error': 'Invalid request method.'})




def statistic_view(request):
	questions = Question.objects.all()
	stats = []

	for question in questions:
		total_answers = Statistic.objects.filter(question=question).count()
		true_answers = Statistic.objects.filter(question=question, is_true_answer=True).count()

		if total_answers > 0:  # Check if total_answers is not zero
			stats.append({'question': question, 'total_answers': total_answers, 'true_answers': true_answers})

	# Create a pie chart
	labels = [f"{stat['question'].question} - {stat['true_answers']}/{stat['total_answers']}" for stat in stats]
	sizes = [stat['true_answers'] for stat in stats]
	colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

	plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
	plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

	# Save the pie chart as a PNG image
	image_path = os.path.join('media', 'pie_chart.png')
	plt.savefig(image_path)

	return render(request, 'magicflot/statistic.html', {'stats': stats, 'image_path': image_path})
