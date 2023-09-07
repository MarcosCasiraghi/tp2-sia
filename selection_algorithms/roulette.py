from classes.generation import Generation
import random
import numpy as np


def roulette_selection(amount_to_select, populus):
    fitness_array = []
    # calculo el fitness total y agrego fitness en arreglo para despues normalizarlo
    for elem in populus:
        fitness = elem.performance
        fitness_array.append(fitness)

    return roulette_random_selection(amount_to_select, fitness_array, populus)


def roulette_random_selection(amount_to_select, fitness, populus):
    total_fitness = np.sum(fitness)

    # normalizo cada fitness a partir de valor total
    normalized_fitness = relative_fitness(fitness, total_fitness)

    # calculo fitness accumulativo a partir del normalizado
    accum_fitness = accumulative_fitness(normalized_fitness)

    # Calculo numero aleatorio y selecciono los fighters
    selected = []
    for _ in range(amount_to_select):
        random_value = random.uniform(0, 1)
        for i in range(len(accum_fitness)):
            if accum_fitness[i] > random_value:
                selected.append(populus[i])
                break

    return selected

def relative_fitness(individual_fitness, total_fitness):
    to_return = []
    for item in individual_fitness:
        to_return.append(item/total_fitness)
    return to_return


def accumulative_fitness(relative_fitness):
    accumulative_ft = []
    for i in range(len(relative_fitness)):
        if i == 0:
            accumulative_ft.append(relative_fitness[i])
        else:
            accumulative_ft.append(relative_fitness[i] + accumulative_ft[i-1])
    return accumulative_ft

