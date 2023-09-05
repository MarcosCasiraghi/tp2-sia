from classes.generation import Generation
from selection_algorithms.roulette import relative_fitness, accumulative_fitness
from random import random


def universal_selection(amount_to_select, gen: Generation):
    #fitness acumulado
    accumulated_ft = []
    #fitness relativo a cada pj
    relative_ft = []
    #fitness individual de cada pj
    individual_ft = []
    #suma de los fitness individuales de todos los pj
    total_ft = 0
    #selection
    selected_pjs = []
    #variables de funcion universal
    r_j = []
    r = random()
    k = 0

    #calculo rj
    while k < amount_to_select:
        r_j.append((r+k)/amount_to_select)
        k += 1
    #fitness para cada pj

    individual_ft, total_ft = individual_fitness(gen)

    #fitness relativo para cada pj

    relative_ft = relative_fitness(individual_ft, total_ft)

    #fitness acumulado
    accumulated_ft = accumulative_fitness(relative_ft)
    #seleccion de pjs
    i = 0
    r_index = 0
    for _ in range(amount_to_select):
        for i in range(len(accumulated_ft)):
            if accumulated_ft[i] > r_j[r_index]:
                selected_pjs.append(gen[i])
                r_index += 1
                break

    return selected_pjs

def individual_fitness(gen: Generation):
    individual_fitness = []
    total_fitness = 0
    for elem in gen:
        fitness = elem.performance
        individual_fitness.append(fitness)
        total_fitness += fitness

    return (individual_fitness, total_fitness)

