from random import randint
from classes.generation import Generation


def probabilistic_tournament_selection(amount_to_select, generation: Generation, threshold=0.75):
    new_generation = Generation()
    generation_len = len(generation)

    while len(new_generation) < amount_to_select:
        tournament_array = []
        random1 = randint(0, generation_len)
        random2 = randint(0, generation_len)
        tournament_array.append(generation[random1])
        tournament_array.append(generation[random2])
        tournament_array.sort(reverse=True)

        probability = randint(1, 101) / 100
        if probability > threshold:
            new_generation.append(tournament_array[0])
        else:
            new_generation.append(tournament_array[1])
