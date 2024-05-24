import os
import json
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from django.conf import settings


def load_game_sessions():
    data = 'static/json/game_sessions.json'
    game_sessions = []

    with open(data, 'r') as file:
        for line in file:
            game_session_data = json.loads(line)
            game_sessions.append(game_session_data)

    return game_sessions


def generate_pie_chart(game_sessions):
    g_true_count = 0
    t_true_count = 0
    question_true_count = 0
    question_false_count = 0

    
    pie_chart_dir = os.path.join(settings.BASE_DIR, 'static/pies')
    if not os.path.exists(pie_chart_dir):
        os.makedirs(pie_chart_dir)


    for session in game_sessions:
        for answer in session['how_it_was']['answered_questions']:
            if answer['category'] == 'g' and answer['value'] == 'True':
                g_true_count += 1
            if answer['category'] == 't' and answer['value'] == 'True':
                t_true_count += 1
            if answer['value'] == 'True':
                question_true_count += 1
            else:
                question_false_count += 1

    labels = ['ОБЩИЕ', 'ТЕХНИЧЕСКИЕ']
    sizes = [g_true_count, t_true_count]
    colors = list(mcolors.CSS4_COLORS.values())[:len(labels)]
    plt.figure(figsize=(6, 5))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Распределение верных ответов по категориям')
    plt.savefig(os.path.join(pie_chart_dir, 'g_t_pie_chart.png'), transparent=True)
    

    labels = ['ВЕРНЫЕ', 'НЕПРАВИЛЬНЫЕ']
    sizes = [question_true_count, question_false_count]
    colors = list(mcolors.CSS4_COLORS.values())[len(labels):len(labels)+len(labels)]
    plt.figure(figsize=(5, 5))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Соотношение всех ответов на вопросы викторины')
    plt.savefig(os.path.join(pie_chart_dir, 'true_false_pie_chart.png'), transparent=True)

# Load game sessions data
game_sessions = load_game_sessions()

# Generate pie charts based on the game sessions data
generate_pie_chart(game_sessions)



def get_statistics(game_sessions):
    game_sessions_count = len(game_sessions)
    all_questions = sum(len(session["how_it_was"]["answered_questions"]) for session in game_sessions)
    
    return game_sessions_count, all_questions