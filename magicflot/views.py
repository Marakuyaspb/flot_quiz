import os
import random
import json
from datetime import datetime
from weasyprint import HTML
from urllib.parse import quote


from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template, render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse


from .models import Category, Question, Statistic, Winner
from .forms import WinnerForm
from .stat import get_statistics, load_game_sessions, generate_pie_chart, generate_easy, generate_hard, generate_bar


def error_404_view(request, exception):
	return render(request, 'magicflot/404.html', status=404)
def error_500(request):
	return render(request, 'magicflot/500.html', status=500)


def index(request):
	return render(request, 'magicflot/index.html')
def about(request):
	return render(request, 'magicflot/about.html')
def blog(request):
	return render(request, 'magicflot/blog.html')
def book(request):
	return render(request, 'magicflot/book.html')

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
		all_questions = Question.objects.exclude(id__in=[q.id for q in questions]).order_by('?')[:15 - len(questions)]
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

	context = {
		'winner': winner,
	}

	html_string = render_to_string(template_path, context)

	pdf_file = HTML(string=html_string, base_url=request.build_absolute_uri()).write_pdf()

	response = HttpResponse(pdf_file, content_type='application/pdf')
	response['Content-Disposition'] = f'attachment; filename="certificate_{winner.last_name}_{winner.first_name}.pdf"'

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
	game_sessions = load_game_sessions()
	game_sessions_count, all_questions = get_statistics(game_sessions)

	generate_pie_chart_result = generate_pie_chart(game_sessions)
	generate_easy_result = generate_easy(game_sessions)
	generate_hard_result = generate_hard(game_sessions)
	generate_bar_result = generate_bar(game_sessions)

	# Display bars about each question
	bar_chart_dir = os.path.join(settings.BASE_DIR, 'static/bars')
	bars = [f for f in os.listdir(bar_chart_dir) if f.endswith('.png')]
	
	context = {
		'game_sessions_count': game_sessions_count, 
		'all_questions': all_questions,
		'bars': bars,
		'generate_pie_chart_result':generate_pie_chart,
		'generate_easy_result':generate_easy,
		'generate_hard_result':generate_hard,
		'generate_bar_result':generate_bar_result
	}

	return render(request, 'magicflot/stat.html', context)