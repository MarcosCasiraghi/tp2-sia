from classes.generation import Generation
from selection_algorithms.roulette import roulette_random_selection
import math
import numpy as np


def boltzmann_selection(amount_to_select, populus, Temperature):
    boltzmann_func = []
    for elem in populus:
        boltzmann_func.append(math.exp(elem.performance/Temperature))

    average = np.average(boltzmann_func)

    ExpVal = []
    for elem in boltzmann_func:
        ExpVal.append(elem/average)

    return roulette_random_selection(amount_to_select, ExpVal, populus)

