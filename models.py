import random
from utilities import load_pokemon
from weaknesses import weaknesses


# List of damage to randomly pair with selected attacks from file
damage = [10, 20, 25, 35]


# Class that defines a Pokemon
class Pokemon:
    def __init__(self, name, type, attacks, hp):  # , weakness):
        self.name = name
        self.type = type
        self.attacks = attacks
        self.hp = hp
        # self.weakness = weakness
        self.status = "awake"

    # print hp
    def get_status(self):
        print(f"{self.name}: HP: {self.hp} TYPE: {self.type}")  # STATUS: {self.status}")

    # print move list
    def get_attacks(self):
        for k, v in self.attacks.items():
            print(k, v)

    def run_attack(self, adversary):
        attack = random.choice(list(self.attacks.keys()))
        damage = self.attacks[attack] * weaknesses[self.type][adversary.type]
        print(f"{self.name} attacked with {attack} and it did {damage} damage")
        # time.sleep(1)
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
            pokemon_to_add = Pokemon(poke_name, poke_type, attacks, poke_hp)  # , "None" )
            self.members.append(pokemon_to_add)

        return self
