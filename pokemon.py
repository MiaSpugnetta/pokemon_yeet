import random
import time
from utilities import setup_game, load_pokemon
from weaknesses import weaknesses

# POKEMON: YEET
# Class that defines a Pokemon
class Pokemon:
    def __init__(self, name, type, attacks, hp):#, weakness):
        self.name = name
        self.type = type
        self.attacks = attacks
        self.hp = hp
        #self.weakness = weakness
        self.status = "awake"

    # print hp
    def get_status(self):
        print(f"{self.name}: HP: {self.hp} TYPE: {self.type}")#STATUS: {self.status}")

    # print move list
    def get_attacks(self):
        for k, v in self.attacks.items():
            print(k, v)

    def run_attack(self, adversary):
        attack = random.choice(list(self.attacks.keys()))
        damage = self.attacks[attack] * weaknesses[self.type][adversary.type]
        print(f"{self.name} attacked with {attack} and it did {damage} damage")
        #time.sleep(1)
        return damage

    def receive_attack(self, damage):
        self.hp -= damage
        self.get_status()


# Lineup class of pokemon so that they can fight
class Lineup:
    def __init__(self):
        self.members = []

    def show_lineup(self):
        for i in self.members:
            i.get_status()

    # Randomly recruiting pokemon
    def recruit(self):
        for i in range(6):  # team of six
            rand_pokemon = random.randint(1, 151)  # select random pokemon
            poke_name, poke_type, poke_hp, moves = load_pokemon(rand_pokemon)  # fetch info from file

            if poke_type == "fairy":
                poke_type = "normal"  # changed to stay true to I generation

            attacks = dict(zip(moves, damage))  # make a dict out of the list of moves from json and list of damage
            pokemon_to_add = Pokemon(poke_name, poke_type, attacks, poke_hp)#, "None" )
            self.members.append(pokemon_to_add)

        return self


# List of damage to randomly pair with selected attacks from file
damage = [10, 20, 25, 35]


#def game_logic(poke_dict):
def game_logic():
    print("Get Ready, Now Recruiting Your Team Of Pokemon!")
    our_team = Lineup().recruit()
    #time.sleep(1.5)  # add delay for dramatic effect
    print("\n")

    print("Team Selected! Meet Your New Team")
    our_team.show_lineup()
    #time.sleep(2)

    print("\n")
    print("Now Recruiting The Enemy Team!")
    print("\n")
    your_team = Lineup().recruit()
    #time.sleep(1.5)

    print("Team Selected! Meet Your Enemies!")
    your_team.show_lineup()
    #time.sleep(2)

    print("\n")
    print("PREPARE TO FIGHT!!!")
    print("\n")
    #time.sleep(3)

    #######################################################################################
    # define inner function to try out here

    def fight(first_pokemon, second_pokemon, first_team_score, second_team_score):
        while second_pokemon.hp > 0 and first_pokemon.hp > 0:
            damage = first_pokemon.run_attack(second_pokemon)
            second_pokemon.receive_attack(damage)
            if second_pokemon.hp <= 0:
                print(f"{second_pokemon.name} has FAINTED")
                second_pokemon.status = "fainted"
                first_team_score += 1
                #time.sleep(1)
                continue

            damage = second_pokemon.run_attack(first_pokemon)
            first_pokemon.receive_attack(damage)
            if first_pokemon.hp <= 0:
                print(f"{first_pokemon.name} has FAINTED")
                first_pokemon.status = "fainted"
                second_team_score += 1
                #time.sleep(1)
                continue
        return first_team_score, second_team_score

#########################################################
    our_score = 0  # ToDo: change score system to fight until all team pokemon have fainted
    enemy_score = 0

    # There are as many matches as pokemon per team
    for i in range(len(your_team.members)):
        print(f"MATCH #{i+1}: {our_team.members[i].name} (HPs {our_team.members[i].hp}, {our_team.members[i].type}) vs {your_team.members[i].name} (HPs {your_team.members[i].hp}, {your_team.members[i].type})")
        coin_flip = random.randrange(0, 2)  # randomisation to see which pokemon attacks first
        # ToDo: somehow it appears to be biased towards our_team again. even if the coin_flip is fair and value gets swapped
        if coin_flip == 0:
            print(f"coin is {coin_flip}, our pokemon starts")
            our_score, enemy_score = fight(our_team.members[i], your_team.members[i], our_score, enemy_score)

        else:
            print(f"coin is {coin_flip}, enemy starts")
            enemy_score, our_score = fight(your_team.members[i], our_team.members[i], our_score, enemy_score)

        print(f"The Score is: Me: {our_score}, Enemy: {enemy_score}")
        print("\n")

    if our_score > enemy_score:
        return "WE WON HAHAHAHAHAHAHAHAHAHAHAHA"

    elif our_score == enemy_score:
        return "IT'S A DRAW"

    else:
        return "WE LOST BECAUSE WE ARE LOSERS"

####################################################
setup_game()

print(game_logic())
