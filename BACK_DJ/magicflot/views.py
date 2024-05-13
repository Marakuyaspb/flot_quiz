import random
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from xhtml2pdf import pisa
from .models import Question, Category, Winner
from .forms import WinnerForm



def index(request):
	return render(request, 'magicflot/index.html')

def about(request):
	return render(request, 'magicflot/about.html')

def gallery(request):
	return render(request, 'magicflot/gallery.html')


# GAME
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
	context = {'winner': winner, 'logo_url': 'https://городволшебныхкораблей.рф/static/logo_blue.png'}
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = f'attachment; filename="certificate_{winner.last_name}_{winner.first_name}.pdf"'
	template = get_template(template_path)
	html = template.render(context)
	pisa_status = pisa.CreatePDF(html, dest=response)
	if pisa_status.err:
		return HttpResponse('Имеют место технические неполадки <pre>' + html + '</pre>')
	return response



@csrf_exempt
def save_quiz_interaction(request):
	if request.method == 'POST':
		data = json.loads(request.body)
		
		# Save the data to a JSON file
		with open('quiz_interactions.json', 'a') as file:
			json.dump(data, file)
			file.write('\n')
	
		return JsonResponse({'message': 'Quiz interaction saved successfully.'})