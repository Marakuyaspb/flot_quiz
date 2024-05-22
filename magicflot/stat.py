import os
import json
from django.conf import settings
import matplotlib.pyplot as plt

def decode_unicode(data):
    if isinstance(data, dict):
        return {decode_unicode(key): decode_unicode(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [decode_unicode(item) for item in data]
    elif isinstance(data, str):
        return data.encode('utf-8').decode('unicode-escape')
    else:
        return data




def load_game_sessions():
    file_path = '/home/a/flot/static/game_sessions.json'
    
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return None
    
    try:
        with open(file_path, 'r') as file:
            # Load JSON data from the file
            game_sessions_data = json.load(file)
            return game_sessions_data
    except IOError as e:
        print(f"Error reading file: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None


def generate_pie_chart(values, labels):
    # Function to generate a pie chart based on the game sessions data
    plt.figure(figsize=(8, 8))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Distribution of True Answers by Category')
    
    # Save the pie chart as an image file
    plt.savefig('static/pie_chart.png')




def get_statistics():
    game_sessions = load_game_sessions()

    if game_sessions is None:
        return

    true_categories = {'t': 0, 'g': 0}
    for session in game_sessions:
        for question in session['how_it_was']['answered_questions']:
            category = question['category']
            if question['value'] == 'True' and category in true_categories:
                true_categories[category] += 1

    labels = ['Category T', 'Category G']
    values = true_categories['t'], true_categories['g']
    
    generate_pie_chart(values, labels)

    game_sessions_count = len(game_sessions)
    return game_sessions_count

game_sessions_count = get_statistics()
if game_sessions_count is not None:
    print(f"Number of game sessions: {game_sessions_count}")