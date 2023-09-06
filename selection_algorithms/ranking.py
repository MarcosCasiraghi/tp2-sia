from selection_algorithms.roulette import roulette_random_selection
from classes.generation import Generation


def ranking_selection(amount_to_select, populus):
    ranking_func = []

    #se ordena por fitness
    populus.sort(reverse=True)
    size = len(populus)
    for i in range(size):
        ranking_func.append((size - i)/size)

    return roulette_random_selection(amount_to_select, ranking_func, populus)
