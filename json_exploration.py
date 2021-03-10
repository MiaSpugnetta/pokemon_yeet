import json
import random


with open('pokemon/4.json') as file:
  data = json.load(file)
print(data.keys())
#print(data['moves'][3]['move']['name'])

moves=[]

#for i in range(len(data['moves'])):
#    moves.append(data['moves'][i]['move']['name'])

#for i in range(len(data['moves'])):#
#    for n in range(5):#
#        move = random.choice(data['moves'][i]['move']['name'])
#        moves.append(move)
for i in range(5):
    move = random.choice(data['moves'])
    move_name = move['move']['name']
    moves.append(move_name)
print(moves)
