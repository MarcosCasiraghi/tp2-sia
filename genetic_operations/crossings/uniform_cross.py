from classes.fighters import *
from random import random
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




fighter1 = Archer(20,10,50,20,50,1.89)
fighter2 = Archer(10,20,20,60,40,1.32)


h1, h2 = uniform_cross_parents(fighter1,fighter2)

print(h1)
print(h2)












