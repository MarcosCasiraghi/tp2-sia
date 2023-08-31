from classes.fighters import Fighter
from random import randint
from genetic_operations.crossings.cross_utils import cross_population
from genetic_operations.crossings.cross_utils import get_crossing_data
from utils.fighter_creation import get_fighter_class
import math


# self.strength = strength
# self.agility = agility
# self.expertise = expertise
# self.resistence = resistence
# self.hp = hp

def anular_cross_parents(parent1: Fighter, parent2: Fighter):
    parent1arr, parent2arr, crosspoint, arrlen = get_crossing_data(parent1, parent2)

    segment_length = randint(0, math.ceil(arrlen / 2))

    for i in range(0,segment_length):
        current_index = (crosspoint + i) % arrlen
        parent1arr[current_index], parent2arr[current_index] = parent2arr[current_index], parent1arr[current_index]

    cls = get_fighter_class(parent1)
    return cls(*parent1arr), cls(*parent2arr)


def anular_cross(selected: list):
    return cross_population(selected, anular_cross_parents)
