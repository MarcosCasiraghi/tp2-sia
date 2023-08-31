from random import randint
from classes.fighters import *
from utils.fighter_creation import get_fighter_class
from genetic_operations.crossings.cross_utils import cross_population
from genetic_operations.crossings.anular_cross import get_crossing_data

# self.strength = strength
# self.agility = agility
# self.expertise = expertise
# self.resistence = resistence
# self.hp = hp


def one_point_cross_parents(parent1: Fighter, parent2: Fighter, recievedPoint=0):

    parent1arr, parent2arr , recievedPoint, array_length = get_crossing_data(parent1,parent2)

    for i in range(recievedPoint, array_length):
        parent1arr[i], parent2arr[i] = parent2arr[i], parent1arr[i]

    parent1arr = scale_array_to_sum(parent1arr)
    parent2arr = scale_array_to_sum(parent2arr)

    cls = get_fighter_class(parent1)

    return cls(*parent1arr), cls(*parent2arr)


def one_point_cross(selected: list):
    return cross_population(selected, one_point_cross_parents)
