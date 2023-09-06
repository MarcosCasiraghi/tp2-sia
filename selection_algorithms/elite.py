
from classes.generation import Generation


def elite_selection(amount_to_select, populus):
    populus.sort(reverse=True)
    return populus[0: amount_to_select]
