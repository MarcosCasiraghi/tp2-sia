from classes.fighters import *
from random import random
from classes.generation import *
from utils.fighter_creation import get_fighter_class


# self.strength = strength
# self.agility = agility
# self.expertise = expertise
# self.resistence = resistence
# self.hp = hp


def uniform_cross_parents(parent1:Fighter , parent2: Fighter):
    SWAP_PROBABILITY = 0.5
    p1_stats = [parent1.strength,parent1.agility,parent1.expertise,parent1.resistence,parent1.hp]
    p2_stats = [parent2.strength,parent2.agility,parent2.expertise,parent2.resistence,parent2.hp]

    p1_height = parent1.height
    p2_height = parent2.height


    for i in range(len(p1_stats)):
        if SWAP_PROBABILITY <= random():
            p1_stats[i], p2_stats[i] = p2_stats[i], p1_stats[i]
    
    #re-definir el array
    
    p1_stats = scale_array_to_sum(p1_stats)
    p2_stats = scale_array_to_sum(p2_stats)

    #for height
    if SWAP_PROBABILITY <= random():
        p1_height, p2_height = p2_height, p1_height

    cls = get_fighter_class(parent1)
    return cls(*p1_stats,p1_height) , cls(*p2_stats,p2_height)



def uniform_cross(selected_fighters_list):

    childList = []
    list_length = len(selected_fighters_list)
    for i in range(0,list_length,2):
        parent1 = selected_fighters_list[i]
        parent2 = selected_fighters_list[(i + 1) % list_length] # por si la lista es impar
        child1, child2 = uniform_cross_parents(parent1,parent2)
        childList.append(child1)
        childList.append(child2)
    return childList















