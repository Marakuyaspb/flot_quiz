import os
import json

data = 'game_sessions.json'
game_sessions = []

with open(data, 'r') as file:
	for line in file:
		game_session_data = json.loads(line)
		game_sessions.append(game_session_data)

	for session in game_sessions:
		print(session)
		#pass
	
	#print (game_sessions)