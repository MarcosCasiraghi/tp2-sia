import random
from random import randint
from classes.generation import Generation


def probabilistic_tournament_selection(amount_to_select, populus, threshold=0.75):
    selected = []

    while len(selected) < amount_to_select:
        character1 = random.choice(populus)
        character2 = random.choice(populus)

        probability = randint(1, 101) / 100

        # Caso: elijo el mejor de los dos
        if probability > threshold:
            if character1.__lt__(character2):
                selected.append(character2)
            else:
                selected.append(character1)

        # Caso: elijo el peor de los dos
        else:
            if character1.__lt__(character2):
                selected.append(character1)
            else:
                selected.append(character2)

    return selected