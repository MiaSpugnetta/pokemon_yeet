import random
import time

# POKEMON: YEET
# Class that defines a Pokemon
class Pokemon:
    def __init__(self, name, type, attacks, hp, weakness):
        self.name = name
        self.type = type
        self.attacks = attacks
        self.hp = hp
        self.weakness = weakness
        self.status = "awake"

    # print hp
    def get_status(self):
        print(f"{self.name}: HP: {self.hp} STATUS: {self.status}")

    # print move list
    def get_attacks(self):
        for k, v in self.attacks.items():
            print(k, v)

    def run_attack(self):
        attack = random.choice(list(self.attacks.keys()))
        damage = self.attacks[attack]
        print(f"{self.name} attacked with {attack} and it did {damage} damage")
        time.sleep(1)

        return damage

    def receive_attack(self, damage):
        self.hp -= damage
        self.get_status()


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

    def recruit(self, poke_dict):
        for i in range(3):
            pokemon_to_add = random.choice(list(poke_dict.values()))  # pick ranndom pokemon
            self.members.append(pokemon_to_add)  # add to the list
            del poke_dict[pokemon_to_add.name]  # remove from dict so that there are no duplicates
        return self


#class Fight():
#    def __init__(self):
#        pass
#
#    #def fight_to_the_death(pokemon):



poke_dict = {
            "bulbasaur": Pokemon("bulbasaur", "Grass", {"tackle": 10, "vine whip": 20, "razor leaf": 25, "hyper beam": 35}, 100, "Fire"),
            "squirtle": Pokemon("squirtle", "Water", {"tackle": 10, "water gun": 20, "bubble": 25, "hydro pump": 35}, 100, "Electric"),
            "charmander": Pokemon("charmander", "Fire", {"tackle": 10, "ember": 20, "fire blast": 25, "flame wheel": 35}, 100, "Water"),
            "rattata": Pokemon("rattata", "Fire", {"tackle": 10, "ember": 20, "fire blast": 25, "flame wheel": 35}, 100, "Water"),
            "ditto": Pokemon("ditto", "Fire", {"tackle": 10, "ember": 20, "fire blast": 25, "flame wheel": 35}, 100, "Water"),
            "mew": Pokemon("mew", "Fire", {"tackle": 10, "ember": 20, "fire blast": 25, "flame wheel": 35}, 100, "Water"),
            "arbok": Pokemon("arbok", "Fire", {"tackle": 10, "ember": 20, "fire blast": 25, "flame wheel": 35}, 100, "Water")
            }


def game_logic(poke_dict):
    print("Get Ready, Now Recruiting Your Team Of Pokemon!")
    our_team = Lineup().recruit(poke_dict)
    time.sleep(1.5)  # add delay for dramatic effect
    print("\n")

    print("Team Selected! Meet Your New Team")
    our_team.show_lineup()
    time.sleep(2)

    print("\n")
    print("Now Recruiting The Enemy Team!")
    print("\n")
    your_team = Lineup().recruit(poke_dict)
    time.sleep(1.5)

    print("Team Selected! Meet Your Enemies!")
    your_team.show_lineup()
    time.sleep(2)

    print("PREPARE TO FIGHT!!!")
    print("\n")
    time.sleep(3)

    our_score = 0
    enemy_score = 0


    # There are as many matches as pokemon per team
    for i in range(len(your_team.members)):
        while your_team.members[i].hp > 0 and our_team.members[i].hp > 0:  # attack randomly until the pokemon is dead
            damage = our_team.members[i].run_attack()
            your_team.members[i].receive_attack(damage)
            #time.sleep(1)

            if your_team.members[i].hp <= 0:
                print("\n")
                print(f"{your_team.members[i].name} has FAINTED")
                your_team.members[i].status = "fainted"
                your_team.members[i].get_status()
                our_score += 1
                print(f"The Score is: Me: {our_score}, Enemy: {enemy_score}")
                print("\n")
                time.sleep(1)

                continue

            damage = your_team.members[i].run_attack()
            our_team.members[i].receive_attack(damage)

            if our_team.members[i].hp <= 0:
                print("\n")
                print(f"{our_team.members[i].name} has FAINTED")
                our_team.members[i].status = "fainted"
                our_team.members[i].get_status()
                enemy_score += 1
                print(f"The Score is: Me: {our_score}, Enemy: {enemy_score}")
                print("\n")
                time.sleep(1)


                continue



    if our_score > enemy_score:
        print("WE WON HAHAHAHAHAHAHAHAHAHAHAHA")

    else:
        print("WE LOST BECAUSE WE ARE LOSERS")


game_logic(poke_dict)
