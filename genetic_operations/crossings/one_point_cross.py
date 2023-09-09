from random import randint
from classes.fighters import *
from genetic_operations.crossings.cross_utils import cross_population
from genetic_operations.crossings.anular_cross import get_crossing_data


def one_point_cross_parents(parent1: Fighter, parent2: Fighter, recievedPoint=0):
    child1_array, child2_array, recievedPoint, array_length = get_crossing_data(parent1, parent2)

    for i in range(recievedPoint, array_length):
        child1_array[i], child2_array[i] = child2_array[i], child1_array[i]

    child1_array = scale_array_to_sum(child1_array)
    child2_array = scale_array_to_sum(child2_array)

    create_child = parent1.__class__
    return create_child(*child1_array), create_child(*child2_array)


def one_point_cross(selected: list):
    return cross_population(selected, one_point_cross_parents)
