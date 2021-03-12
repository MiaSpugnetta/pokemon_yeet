from collections import defaultdict


weaknesses = {  'normal':   {'rock': 0.5, 'ghost': 0},
                'fire':     {'fire':0.5, 'water': 0.5, 'grass': 2,
                            'ice': 2, 'bug': 2, 'rock': 0.5, 'dragon': 0.5},
                'water':    {'fire': 2, 'water': 0.5, 'grass': 0.5,
                            'ground': 2, 'rock': 2, 'dragon': 0.5},
                'electric': {'water': 2, 'electric': 0.5,
                            'grass': 0.5, 'ground': 0, 'flying': 2,
                            'dragon': 0.5},
                'grass':    {'fire': 0.5, 'water': 2, 'grass': 0.5,
                            'poison': 0.5, 'ground': 2, 'flying': 0.5,
                            'bug': 0.5, 'rock': 2, 'dragon': 0.5},
                'ice':      {'water': 0.5, 'grass': 2, 'ice': 0.5,
                            'ground': 2, 'flying': 2, 'dragon': 2},
                'fighting': {'normal': 2, 'ice': 2, 'poison': 0.5,
                            'flying': 0.5, 'psychic': 0.5, 'bug': 0.5, 'rock': 2, 'ghost': 0},
                'poison':   {'grass': 2, 'poison': 0.5,
                            'ground': 0.5, 'bug': 2, 'rock': 0.5,
                            'ghost': 0.5},
                'ground':   {'fire': 2, 'grass': 2, 'ice': 0.5,
                            'poison': 2, 'flying': 0, 'bug': 0.5,
                            'rock': 2},
                'flying':   {'electric':0.5,'grass':2,
                            'fighting': 2, 'bug': 2, 'rock': 0.5},
                'psychic':  {'fighting': 2, 'poison': 2,
                            'psychic': 0.5},
                'bug':      {'fire': 0.5, 'grass': 2,
                            'fighting': 0.5, 'poison': 2,
                            'flying': 0.5, 'psychic': 2,
                            'ghost': 0.5},
                'rock':     {'fire': 2, 'ice': 2, 'fighting': 0.5,
                            'ground': 0.5, 'flying': 2, 'rock': 2},
                'ghost':    {'normal': 0, 'psychic': 0, 'ghost': 2},
                'dragon':   {'dragon': 2}
                }




default_weakness = defaultdict(lambda: defaultdict(lambda: 1))

# # do same thing as lambda: 1
# def default_value_1():
#     return 1
#
# def default_value_default_dict():
#     return defaultdict(default_value_1)
#
#
## function() vs function no parenthesis: function() is a call of function - function is the definition, the 'callable' (because it can be called)
#default_weakness = defaultdict(default_value_default_dict)

assert default_weakness['test']['test'] == 1

for type in weaknesses:  # for key in the original dict
    tmp_default_dict = defaultdict(lambda: 1)  # create a temporary defaultdict
    assert tmp_default_dict['test'] == 1
    for type2 in weaknesses[type]:  # for key in the inner dictionary
        tmp_default_dict[type2] = weaknesses[type][type2]  #

    default_weakness[type] = tmp_default_dict

weaknesses = default_weakness


#most important part: test your assumptions
assert weaknesses['test']['test'] == 1
assert weaknesses['normal']['rock'] == 0.5
assert weaknesses['normal']['boob'] == 1
