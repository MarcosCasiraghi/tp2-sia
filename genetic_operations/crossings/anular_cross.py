from classes.fighters import *
from random import randint
from genetic_operations.crossings.cross_utils import cross_population
from genetic_operations.crossings.cross_utils import get_crossing_data
import math


# self.strength = strength
# self.agility = agility
# self.expertise = expertise
# self.resistence = resistence
# self.hp = hp

def anular_cross_parents(parent1: Fighter, parent2: Fighter):
    child1_array, child2_array, crosspoint, arrlen = get_crossing_data(parent1, parent2)

    segment_length = randint(0, math.ceil(arrlen / 2))

    for i in range(0,segment_length):
        current_index = (crosspoint + i) % arrlen
        child1_array[current_index], child2_array[current_index] = child2_array[current_index], child1_array[current_index]

    child1_array = scale_array_to_sum(child1_array)
    child2_array = scale_array_to_sum(child2_array)

    create_child = parent1.__class__
    return create_child(*child1_array), create_child(*child2_array)


def anular_cross(selected: list):
    return cross_population(selected, anular_cross_parents)
