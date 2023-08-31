from classes.generation import Generation
import random
import numpy as np


def roulette_selection(amount_to_select, generation: Generation):
    fitness_array = []
    # calculo el fitness total y agrego fitness en arreglo para despues normalizarlo
    for elem in generation:
        fitness = elem.get_performance()
        fitness_array.append(fitness)

    return roulette_random_selection(amount_to_select, fitness_array, generation)


def roulette_random_selection(amount_to_select, fitness, generation: Generation):
    total_fitness = np.sum(fitness)

    # normalizo cada fitness a partir de valor total
    normalized_fitness = []
    for elem in fitness:
        normalized_fitness.append(elem/total_fitness)

    # calculo fitness accumulativo a partir del normalizado
    accumulative_fitness = []
    for i in range(len(normalized_fitness)):
        if i == 0:
            accumulative_fitness.append(normalized_fitness[i])
        else:
            accumulative_fitness.append(normalized_fitness[i] + accumulative_fitness[i - 1])

    # Calculo numero aleatorio y selecciono los fighters
    selected = []
    for _ in range(amount_to_select):
        random_value = random.uniform(0, 1)
        for i in range(len(accumulative_fitness)):
            if accumulative_fitness[i] > random_value:
                selected.append(generation[i])
                break

    return selected
