from random import randint
from classes.generation import Generation


def deterministic_tournament_selection(amount_to_select, populus, M=3):
    selected = []
    generation_len = len(populus)
    while len(selected) < amount_to_select:
        tournament_array = []
        for i in range(0, M):
            random = randint(0, generation_len-1)
            if populus[random] not in tournament_array:
                tournament_array.append(populus[random])
            else:
                i -= 1
        tournament_array.sort(reverse=True)
        selected.append(tournament_array[0])
    return selected
