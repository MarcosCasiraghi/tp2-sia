from classes.generation import Generation
import random


def roulette_selection(amount_to_select, generation: Generation):
    total_fitness = 0
    normalized_fitness = []
    # calculo el fitness total y agrego fitness en arreglo para despues normalizarlo
    for elem in generation:
        fitness = elem.get_performance()
        normalized_fitness.append(fitness)
        total_fitness += fitness

    #normalizo cada fitness a partir de valor total
    for i in range(len(normalized_fitness)):
        normalized_fitness[i] /= total_fitness

    #calculo fitness accumulativo a partir del normalizado
    accumulative_fitness = []
    for i in range(len(normalized_fitness)):
        if i == 0:
            accumulative_fitness.append(normalized_fitness[i])
        else:
            accumulative_fitness.append(normalized_fitness[i] + accumulative_fitness[i-1])

    # Calculo numero aleatorio y selecciono los fighters
    selected = []
    for _ in range(amount_to_select):
        random_value = random.uniform(0, 1)
        for i in range(len(accumulative_fitness)):
            if accumulative_fitness[i] > random_value:
                selected.append(generation[i])
                break

    return selected
