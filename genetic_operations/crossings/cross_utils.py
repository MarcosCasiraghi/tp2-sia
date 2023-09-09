from classes.fighters import Fighter
from random import randint


def get_crossing_data(parent1: Fighter, parent2: Fighter):
    parent1arr = [parent1.strength, parent1.agility, parent1.expertise, parent1.resistance, parent1.hp, parent1.height]
    parent2arr = [parent2.strength, parent2.agility, parent2.expertise, parent2.resistance, parent2.hp, parent2.height]

    array_length = len(parent1arr)
    change_point = randint(0, array_length - 1)

    return parent1arr, parent2arr, change_point, array_length


def cross_population(selected_fighters_list: list, crossing_strategy):
    childList = []
    list_length = len(selected_fighters_list)
    for i in range(0, list_length, 2):
        parent1 = selected_fighters_list[i]
        parent2 = selected_fighters_list[(i + 1) % list_length]  # por si la lista es impar
        child1, child2 = crossing_strategy(parent1, parent2)
        childList.append(child1)
        childList.append(child2)
    return childList
