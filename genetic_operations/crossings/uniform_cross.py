from classes.fighters import *
from random import random
from genetic_operations.crossings.cross_utils import cross_population

def uniform_cross_parents(parent1: Fighter, parent2: Fighter):
    SWAP_PROBABILITY = 0.5
    child1_array = [parent1.strength, parent1.agility, parent1.expertise, parent1.resistance, parent1.hp,parent1.height]
    child2_array = [parent2.strength, parent2.agility, parent2.expertise, parent2.resistance, parent2.hp,parent2.height]


    for i in range(len(child1_array)):
        if SWAP_PROBABILITY <= random():
            child1_array[i], child2_array[i] = child2_array[i], child1_array[i]

    # re-definir el array

    child1_array = scale_array_to_sum(child1_array)
    child2_array = scale_array_to_sum(child2_array)

    create_child = parent1.__class__
    return create_child(*child1_array), create_child(*child2_array)


def uniform_cross(selected_fighters_list):
    return cross_population(selected_fighters_list, uniform_cross_parents)
