from random import randint
from classes.generation import Generation


def probabilistic_tournament_selection(amount_to_select, populus, threshold=0.75):
    selected = []
    generation_len = len(populus)

    while len(selected) < amount_to_select:
        tournament_array = []
        random1 = randint(0, generation_len)
        random2 = randint(0, generation_len)
        tournament_array.append(populus[random1])
        tournament_array.append(populus[random2])
        tournament_array.sort(reverse=True)

        probability = randint(1, 101) / 100
        if probability > threshold:
            selected.append(tournament_array[0])
        else:
            selected.append(tournament_array[1])
