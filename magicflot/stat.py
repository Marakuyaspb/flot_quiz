import os
import json
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import textwrap
import numpy as np
from collections import defaultdict
from django.conf import settings


def load_game_sessions():
    data = 'static/json/game_sessions.json'
    game_sessions = []
    with open(data, 'r') as file:
        for line in file:
            try:
                game_session_data = json.loads(line)
                game_sessions.append(game_session_data)
            except json.JSONDecodeError as e:
                print(f"Failed to load JSON data: {e}")
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

    plt.rcParams['text.color'] = '#fff'
    labels = ['ОБЩИЕ', 'ТЕХНИЧЕСКИЕ']
    sizes = [g_true_count, t_true_count]
    colors=['navy', 'purple']
    plt.figure(figsize=(6, 5))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, textprops={'color': '#fff'})
    plt.axis('equal')
    plt.title('Распределение верных ответов по категориям')
    plt.savefig(os.path.join(pie_chart_dir, 'g_t_pie_chart.png'), transparent=True)
    

    labels = ['ВЕРНЫЕ', 'НЕ ВЕРНЫЕ']
    sizes = [question_true_count, question_false_count]
    colors=['seagreen', 'crimson']
    plt.figure(figsize=(5, 5))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, textprops={'color': '#fff'})
    plt.axis('equal')
    plt.title('Соотношение всех ответов на вопросы викторины')
    plt.savefig(os.path.join(pie_chart_dir, 'true_false_pie_chart.png'), transparent=True)



def generate_easy(game_sessions):
    question_stats = defaultdict(lambda: {'True': 0, 'False': 0})
    pie_chart_dir = os.path.join(settings.BASE_DIR, 'static/pies')

    for session in game_sessions:
        for question_data in session['how_it_was']['answered_questions']:
            question = question_data['question']
            value = question_data['value']

            question_key = str(question)

            if value == 'True':
                question_stats[question_key]['True'] += 1
            elif value == 'False':
                question_stats[question_key]['False'] += 1

    unique_questions = set([question_data['question'] for session in game_sessions for question_data in session['how_it_was']['answered_questions']])

    filtered_questions = [q for q in unique_questions if str(q) in question_stats and not np.isnan(question_stats[str(q)]['True'])]

    # Sort filtered questions based on the number of True answers
    sorted_questions = sorted(filtered_questions, key=lambda q: question_stats[str(q)]['True'], reverse=True)

    # Create most_easy_chart.png
    most_easy_questions = sorted_questions[:7]
    most_easy_values = [question_stats[str(q)]['True'] if not np.isnan(question_stats[str(q)]['True']) else 0 for q in most_easy_questions]

    fig, ax = plt.subplots(figsize=(10, 6))
    
    y_pos = np.arange(len(most_easy_questions))
    
    bars = ax.barh(y_pos, most_easy_values, color=['darkgreen','green','seagreen', 'teal', 'royalblue', 'mediumblue',  'navy'])
    
    for i, bar in enumerate(bars):
        ax.text(bar.get_width() - 0.2, bar.get_y() + bar.get_height()/2, most_easy_values[i], ha='center', va='center', color='white', fontsize=14)
    
    ax.set_yticks(y_pos)
    ax.set_yticklabels(['\n'.join(textwrap.wrap(str(q), width=45)) for q in most_easy_questions], color='#fff')
    ax.invert_yaxis()
    plt.subplots_adjust(left=0.4, right=0.9)

    plt.savefig(os.path.join(pie_chart_dir, 'most_easy_chart.png'), transparent=True)

    
def generate_hard(game_sessions):
    question_stats = defaultdict(lambda: {'True': 0, 'False': 0})
    pie_chart_dir = os.path.join(settings.BASE_DIR, 'static/pies')

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

    # Filter out questions with missing or invalid data
    filtered_questions = [q for q in unique_questions if str(q) in question_stats and not np.isnan(question_stats[str(q)]['True'])]

    # Sort filtered questions based on the number of True answers
    sorted_questions = sorted(filtered_questions, key=lambda q: question_stats[str(q)]['False'], reverse=True)


    plt.rcParams['text.color'] = '#fff'
    # Create most_easy_chart.png
    most_easy_questions = sorted_questions[:7]
    most_easy_values = [question_stats[str(q)]['True'] if not np.isnan(question_stats[str(q)]['True']) else 0 for q in most_easy_questions]

    fig, ax = plt.subplots(figsize=(10, 6))
    
    y_pos = np.arange(len(most_easy_questions))
    
    bars = ax.barh(y_pos, most_easy_values, color=['maroon', 'firebrick',  'crimson', 'mediumvioletred','purple', 'darkviolet'])
    
    for i, bar in enumerate(bars):
        ax.text(bar.get_width() - 0.2, bar.get_y() + bar.get_height()/2, most_easy_values[i], ha='center', va='center', color='white', fontsize=14)
    
    ax.set_yticks(y_pos)
    ax.set_yticklabels(['\n'.join(textwrap.wrap(str(q), width=45)) for q in most_easy_questions], color='#fff')
    ax.invert_yaxis()
    plt.subplots_adjust(left=0.4, right=0.9)

    plt.savefig(os.path.join(pie_chart_dir, 'most_hard_chart.png'), transparent=True)


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

    plt.rcParams['text.color'] = '#fff'

    for question in unique_questions:
        data = question_stats[str(question)]
        labels = ['ВЕРНЫЕ', 'НЕ ВЕРНЫЕ']
        true_values = data['True']
        false_values = data['False']
        x = range(len(labels))

        wrapped_question = textwrap.fill(question, width=40)

        plt.figure()
        plt.bar(x, [true_values, false_values], color=['seagreen', 'crimson'])
        plt.xticks(x, labels, color='#fff')
        plt.xlabel('Ответы', color='#fff')
        plt.ylabel('Количество', color='#fff')
        plt.title(f'{wrapped_question}', y=0.4, color='#fff')

        plt.savefig(os.path.join(bar_chart_dir, f'{question[:13]}.png'), transparent=True)



# Load game sessions data
game_sessions = load_game_sessions()

# Generate pie charts based on the game sessions data
generate_pie_chart(game_sessions)

#Generate most easy & most
generate_easy(game_sessions)
generate_hard(game_sessions)

# Generate bar for each question
generate_bar(game_sessions)


def get_statistics(game_sessions):
    game_sessions_count = len(game_sessions)
    all_questions = sum(len(session["how_it_was"]["answered_questions"]) for session in game_sessions)
    
    return game_sessions_count, all_questions