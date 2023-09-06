from random import randint
from classes.generation import Generation


def deterministic_tournament_selection(amount_to_select, populus, M=3):
    new_generation = []
    generation_len = len(populus)
    while len(new_generation) < amount_to_select:
        tournament_array = []
        for i in range(0, M):
            random = randint(0, generation_len)
            if populus[random] not in tournament_array:
                tournament_array.append(populus)
            else:
                i -= 1
        tournament_array.sort(reverse=True)
        new_generation.append(tournament_array[0])
    return new_generation
