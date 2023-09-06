
from classes.generation import Generation


def elite_selection(amount_to_select, populus):
    populus.sort(reverse=True)
    selection = []
    gen_size = len(populus)

    for i in range(amount_to_select):
        selection.append(populus[i % gen_size])

    return selection
