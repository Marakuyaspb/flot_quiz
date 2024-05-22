import os
import random
from xhtml2pdf import pisa
from urllib.parse import quote

import json
from django.http import JsonResponse
from datetime import datetime

from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template

from .models import Category, Question, Statistic, Winner
from .forms import WinnerForm
from .stat import get_statistics


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


def download_pdf(request, pk):
	winner = Winner.objects.get(pk=pk)
	template_path = 'magicflot/pdf.html'
	context = {'winner': winner, 'logo_url': 'https://городволшебныхкораблей.рф/static/logo_blue.png', 'partners_logos': 'https://городволшебныхкораблей.рф/static/pdf/partners_logos.png', 'stamp_official': 'https://городволшебныхкораблей.рф/static/pdf/stamp_official.png', }
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = f'attachment; filename="certificate_{winner.last_name}_{winner.first_name}.pdf"'
	template = get_template(template_path)
	html = template.render(context)
	pisa_status = pisa.CreatePDF(html, dest=response)
	if pisa_status.err:
		return HttpResponse('Имеют место технические неполадки <pre>' + html + '</pre>')
	return response


def get_win_sert(request):
	if request.method == 'POST':
		winner_form = WinnerForm(request.POST)
		if winner_form.is_valid():
			winner = winner_form.save()
			return redirect('magicflot:download_pdf', pk=winner.pk)
	else:
		winner_form = WinnerForm()
	return render(request, 'magicflot/get_win_sert.html', {'winner_form': winner_form})





# CREATE SOME STATISTIC



def save_game_session(request):
	if request.method == 'POST':
		try:
			game_session_data = json.loads(request.body)
			file_path = os.path.join(settings.BASE_DIR, 'static/json/game_sessions.json')

			with open(file_path, 'a') as file:
				json.dump(game_session_data, file)
				file.write('\n')

			return JsonResponse({'message': 'Game session data saved successfully'})
		except Exception as e:
			return JsonResponse({'error': str(e)}, status=500)
	else:
		return JsonResponse({'error': 'Invalid request method'}, status=405)


def stat(request):
	game_sessions_count = get_statistics()
	image_path_category = 'static/pie_chart.png'

	return render(request, 'magicflot/stat.html', {'game_sessions_count': game_sessions_count, 'image_path_category': image_path_category})