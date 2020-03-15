import json

with open('pokemon.json') as file:
	data = json.load(file)
	for x in data:
		print(x)