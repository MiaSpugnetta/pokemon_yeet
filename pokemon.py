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
        print(f"{self.name}: HP: {self.hp} STATUS: {self.status} TYPE: {self.type}")

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

    def add_member(self, pokemon):
        if len(self.members) < 3:
            self.members.append(pokemon)
        else:
            print("Sorry Team Already Full")

    def show_lineup(self):
        for i in self.members:
            i.get_status()

    # Randomly recruiting pokemon
    def recruit(self):
        for i in range(6):  # team of six
            rand_pokemon = random.randint(1, 151)  # select random pokemon
            poke_name, poke_type, poke_hp, moves = load_pokemon(rand_pokemon)  # fetch info from file

            if poke_type == "fairy":  # change to stay true to I generation
                poke_type = "normal"

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

    print("PREPARE TO FIGHT!!!")
    print("\n")
    #time.sleep(3)

    our_score = 0
    enemy_score = 0


# ToDo: figure out what happens when a pokemon that does 0 damage attacks first, have to manually interrupt
# ToDo: change score system to fight until all team pokemon have fainted
    # There are as many matches as pokemon per team
    for i in range(len(your_team.members)):
        print(f"MATCH #{i+1}: {our_team.members[i].name} (HPs {our_team.members[i].hp}, {our_team.members[i].type}) vs {your_team.members[i].name} (HPs {your_team.members[i].hp}, {your_team.members[i].type})")
        #print("\n")
        coin_flip = random.randrange(0, 2) # randomisation to see which pokemon attacks first
        print(f"coin is {coin_flip}")
        if coin_flip == 0:
            print("our pokemon starts")
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        else:
            print("enemy starts")
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%")

        while your_team.members[i].hp > 0 and our_team.members[i].hp > 0:  # attack randomly until the pokemon is dead
            if coin_flip == 0:

                damage = our_team.members[i].run_attack(your_team.members[i])
                your_team.members[i].receive_attack(damage)
                #time.sleep(1)

                if your_team.members[i].hp <= 0:
                    print(f"{your_team.members[i].name} has FAINTED")
                    your_team.members[i].status = "fainted"
                    our_score += 1
                    print(f"The Score is: Me: {our_score}, Enemy: {enemy_score}")
                    print("\n")
                    #time.sleep(1)

                    continue

                damage = your_team.members[i].run_attack(our_team.members[i])
                our_team.members[i].receive_attack(damage)

                if our_team.members[i].hp <= 0:
                    print(f"{our_team.members[i].name} has FAINTED")
                    our_team.members[i].status = "fainted"
                    enemy_score += 1
                    print(f"The Score is: Me: {our_score}, Enemy: {enemy_score}")
                    print("\n")
                    #time.sleep(1)

                    continue
            else:

                damage = your_team.members[i].run_attack(our_team.members[i]) 
                our_team.members[i].receive_attack(damage)
                #time.sleep(1)

                if our_team.members[i].hp <= 0:
                    print(f"{our_team.members[i].name} has FAINTED")
                    our_team.members[i].status = "fainted"
                    enemy_score += 1
                    print(f"The Score is: Me: {our_score}, Enemy: {enemy_score}")
                    print("\n")
                    #time.sleep(1)

                    continue

                damage = our_team.members[i].run_attack(your_team.members[i])
                your_team.members[i].receive_attack(damage)

                if your_team.members[i].hp <= 0:
                    print(f"{your_team.members[i].name} has FAINTED")
                    your_team.members[i].status = "fainted"
                    our_score += 1
                    print(f"The Score is: Me: {our_score}, Enemy: {enemy_score}")
                    print("\n")
                    #time.sleep(1)

                    continue

    if our_score > enemy_score:
        return "WE WON HAHAHAHAHAHAHAHAHAHAHAHA"

    elif our_score == enemy_score:
        return "IT'S A DRAW"

    else:
        return "WE LOST BECAUSE WE ARE LOSERS"


setup_game()

print(game_logic())
