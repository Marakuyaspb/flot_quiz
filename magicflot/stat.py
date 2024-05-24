import os
import json
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import textwrap
from collections import defaultdict
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
    colors=['aliceblue', 'skyblue']
    #colors=['chocolate', 'darkorange']
    plt.figure(figsize=(6, 5))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Распределение верных ответов по категориям')
    plt.savefig(os.path.join(pie_chart_dir, 'g_t_pie_chart.png'), transparent=True)
    

    labels = ['ВЕРНЫЕ', 'НЕПРАВИЛЬНЫЕ']
    sizes = [question_true_count, question_false_count]
    colors=['lightgreen', 'salmon']
    plt.figure(figsize=(5, 5))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Соотношение всех ответов на вопросы викторины')
    plt.savefig(os.path.join(pie_chart_dir, 'true_false_pie_chart.png'), transparent=True)


def generate_bar(game_sessions):
    bar_chart_dir = os.path.join(settings.BASE_DIR, 'static/bars')

    question_stats = defaultdict(lambda: {'True': 0, 'False': 0})

    for session in game_sessions:
        for question_data in session['how_it_was']['answered_questions']:
            question = question_data['question']
            value = question_data['value']

            # Ensure the question string is properly formatted before using it as a key
            question_key = str(question)

            if value == 'True':
                question_stats[question_key]['True'] += 1
            elif value == 'False':
                question_stats[question_key]['False'] += 1

    unique_questions = set([question_data['question'] for session in game_sessions for question_data in session['how_it_was']['answered_questions']])

    for question in unique_questions:
        data = question_stats[str(question)]
        labels = ['ВЕРНЫЕ', 'НЕ ВЕРНЫЕ']
        true_values = data['True']
        false_values = data['False']
        x = range(len(labels))

        wrapped_question = textwrap.fill(question, width=40)

        plt.figure()
        plt.bar(x, [true_values, false_values], color=['lightgreen', 'salmon'])
        plt.xticks(x, labels)
        plt.xlabel('Ответы')
        plt.ylabel('Количество')
        plt.title(f'{wrapped_question}', y=0.4)
        plt.savefig(os.path.join(bar_chart_dir, f'{question[:30]}.png'), transparent=True)



# Load game sessions data
game_sessions = load_game_sessions()

# Generate pie charts based on the game sessions data
generate_pie_chart(game_sessions)

# Generate bar for each question
generate_bar(game_sessions)


def get_statistics(game_sessions):
    game_sessions_count = len(game_sessions)
    all_questions = sum(len(session["how_it_was"]["answered_questions"]) for session in game_sessions)
    
    return game_sessions_count, all_questions