import random
import time
from utilities import setup_game#, load_pokemon
#from weaknesses import weaknesses
from models import Pokemon, Lineup


# POKEMON: YEET
def game_logic():
    print("Get Ready, Now Recruiting Your Team Of Pokemon!")
    our_team = Lineup().recruit()
    time.sleep(1.5)  # add delay for dramatic effect
    print("\n")

    print("Team Selected! Meet Your New Team")
    our_team.show_lineup()
    time.sleep(1.5)

    print("\n")
    print("Now Recruiting The Enemy Team!")
    print("\n")
    your_team = Lineup().recruit()
    time.sleep(1.5)

    print("Team Selected! Meet Your Enemies!")
    your_team.show_lineup()
    time.sleep(1.5)

    print("\n")
    print("PREPARE TO FIGHT!!!")
    print("\n")
    time.sleep(2.5)

    #######################################################################################
    # define inner function to try out here

    def fight(first_pokemon, second_pokemon, first_team_score, second_team_score):
        while second_pokemon.hp > 0 and first_pokemon.hp > 0:
            damage = first_pokemon.run_attack(second_pokemon)
            second_pokemon.receive_attack(damage)
            if second_pokemon.hp <= 0:
                time.sleep(1)
                print(f"{second_pokemon.name} has FAINTED")
                time.sleep(1.5)
                second_pokemon.status = "fainted"
                first_team_score += 1
                continue

            damage = second_pokemon.run_attack(first_pokemon)
            first_pokemon.receive_attack(damage)
            if first_pokemon.hp <= 0:
                time.sleep(1)
                print(f"{first_pokemon.name} has FAINTED")
                time.sleep(1.5)
                first_pokemon.status = "fainted"
                second_team_score += 1
                continue
        return first_team_score, second_team_score

    #########################################################
    our_score = 0  # ToDo: change score system to fight until all team pokemon have fainted
    enemy_score = 0

    # There are as many matches as pokemon per team
    for i in range(len(your_team.members)):
        print(f"MATCH #{i + 1}: {our_team.members[i].name} (HPs {our_team.members[i].hp}, {our_team.members[i].type}) vs {your_team.members[i].name} (HPs {your_team.members[i].hp}, {your_team.members[i].type})")
        coin_flip = random.randrange(0, 2)  # randomisation to see which pokemon attacks first
        if coin_flip == 0:
            print(f"coin is {coin_flip}, our pokemon starts")
            our_score, enemy_score = fight(our_team.members[i], your_team.members[i], our_score, enemy_score)

        else:
            print(f"coin is {coin_flip}, enemy starts")
            enemy_score, our_score = fight(your_team.members[i], our_team.members[i], enemy_score, our_score)

        print("\n")
        print(f"The Score is: Me: {our_score}, Enemy: {enemy_score}")
        print("\n")
        time.sleep(2)

    if our_score > enemy_score:
        return "WE WON HAHAHAHAHAHAHAHAHAHAHAHA"

    elif our_score == enemy_score:
        return "IT'S A DRAW"

    else:
        return "WE LOST BECAUSE WE ARE LOSERS"


####################################################
setup_game()
time.sleep(1)

print(game_logic())
