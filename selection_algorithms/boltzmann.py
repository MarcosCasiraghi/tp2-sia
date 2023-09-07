from classes.generation import Generation
from selection_algorithms.roulette import roulette_random_selection
import math
import numpy as np


def boltzmann_selection(amount_to_select, populus, T0, TC, k, prev_gen_info):
    boltzmann_func = []
    temperature = TC + (T0 - TC) * math.exp(-k * prev_gen_info["gen_number"])
    for elem in populus:
        boltzmann_func.append(math.exp(elem.performance/temperature))

    average = np.average(boltzmann_func)

    ExpVal = []
    for elem in boltzmann_func:
        ExpVal.append(elem/average)

    return roulette_random_selection(amount_to_select, ExpVal, populus)

