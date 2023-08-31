from random import randint
from classes.fighters import *
from utils.fighter_creation import get_fighter_class
from genetic_operations.crossings.cross_population import cross_population


# self.strength = strength
# self.agility = agility
# self.expertise = expertise
# self.resistence = resistence
# self.hp = hp


def one_point_cross_parents(parent1: Fighter, parent2: Fighter):
    parent1arr = [parent1.strength, parent1.agility, parent1.expertise, parent1.resistence, parent1.hp, parent1.height]
    parent2arr = [parent2.strength, parent2.agility, parent2.expertise, parent2.resistence, parent2.hp, parent2.height]

    array_length = len(parent1arr)
    recievedPoint = randint(0, array_length - 1)

    for i in range(recievedPoint, array_length):
        parent1arr[i], parent2arr[i] = parent2arr[i], parent1arr[i]

    parent1arr = scale_array_to_sum(parent1arr)
    parent2arr = scale_array_to_sum(parent2arr)

    cls = get_fighter_class(parent1)

    return cls(*parent1arr), cls(*parent2arr)


def one_point_cross(selected: list):
    return cross_population(selected, one_point_cross_parents)
