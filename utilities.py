import requests
import json
import os  # package to interact with host operative system
import random


# Setup folder for cache if not already there
def setup_game():
    if not os.path.isdir('./pokemon'):  # check if folder exists
        print("Creating Pokemon directory...")
        os.mkdir('./pokemon')  # create folder

    for i in range(1, 152):
        # Check if data is not already present locally
        if not os.path.isfile(f"./pokemon/{i}.json"):
            try:
                # for every pokemon send request to the API and write data to a json file
                r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}')  # get data

                print("Importing Pokemon...")
                # write to json file
                f = open(f"./pokemon/{i}.json", "a")
                f.write(r.text)
                f.close()

            except:
                print(f'Pokemon Number: {i} not found')
                continue
    print("Game is setup and ready to begin!")


# Load data from files
def load_pokemon(pokemon):
    with open(f'./pokemon/{pokemon}.json') as f:
        poke_data = json.load(f)

        # From json file:
        poke_name = poke_data['name']  # fetch name
        poke_type = poke_data['types'][0]['type']['name']  # fetch type
        poke_hp = poke_data['stats'][0]['base_stat']  # fetch HPs

        moves = []
        for i in range(4):  # fetch four random moves
            move = random.choice(poke_data['moves'])
            move_name = move['move']['name']
            moves.append(move_name)

    return poke_name, poke_type, poke_hp, moves
