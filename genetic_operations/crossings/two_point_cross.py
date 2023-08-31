from random import randint
from classes.fighters import *
from utils.fighter_creation import get_fighter_class
from genetic_operations.crossings.cross_population import cross_population


# self.strength = strength
# self.agility = agility
# self.expertise = expertise
# self.resistence = resistence
# self.hp = hp


def two_point_cross_parents(parent1: Fighter, parent2: Fighter):
    child1_array = [parent1.strength, parent1.agility, parent1.expertise, parent1.resistence, parent1.hp, parent1.height]
    child2_array = [parent2.strength, parent2.agility, parent2.expertise, parent2.resistence, parent2.hp, parent2.height]

    array_length = len(child1_array)
    point1 = randint(0, array_length - 1)
    point2 = randint(point1, array_length - 1)

    for i in range(point1, point2):
        child1_array[i], child2_array[i] = child2_array[i], child1_array[i]

    child1_array = scale_array_to_sum(child1_array)
    child2_array = scale_array_to_sum(child2_array)

    cls = get_fighter_class(parent1)

    return cls(*child1_array), cls(*child2_array)


def two_point_cross(selected: list):
    return cross_population(selected, two_point_cross_parents)
