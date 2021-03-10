import requests
import json
import os  # package to interact with host operative system


def setup_game():
    # Setup folder for cache if not already there
    if os.path.isdir('./pokemon') == False:  # check if folder exists
        print("Creating Pokemon directory...")
        os.mkdir('./pokemon')  # create folder

    for i in range(1, 152):
        # Check if data is not already present locally
        if os.path.isfile(f"./pokemon/{i}.json") == False:
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


#setup_game()
