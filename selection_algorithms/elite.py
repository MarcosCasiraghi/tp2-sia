
from classes.generation import Generation


def elite_selection(amount_to_select, generation: Generation):
    generation.sort(reverse=True)
    selection = Generation()
    gen_size = len(generation)

    for i in range(amount_to_select):
        selection.append(generation[i % gen_size])

    return selection



