from classes.generation import Generation
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
    for elem in gen:
        fitness = elem.get_perfomance()
        individual_ft.append(fitness)
        total_ft += fitness
    #fitness relativo para cada pj
    for item in individual_ft:
        relative_ft.append(item/total_ft)

    #fitness acumulado
    for i in range(len(relative_ft)):
        if i == 0:
            accumulated_ft.append(relative_ft[i])
        else:
            accumulated_ft.append(relative_ft[i] + relative_ft[i-1])
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
