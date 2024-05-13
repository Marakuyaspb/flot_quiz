import requests

def push_data_to_yandex_sheets():
    with open('quiz_interactions.json', 'r') as file:
        interactions = file.readlines()
    
    for interaction in interactions:
        data = json.loads(interaction)
        
        # Use Yandex API to push data to Sheets
        # Make API requests here
        
        # Once data is successfully pushed, remove the interaction from the JSON file
        # os.remove('quiz_interactions.json')