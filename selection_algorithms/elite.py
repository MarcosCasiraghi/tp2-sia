
from classes.generation import Generation


def elite_selection(amount_to_select, generation: Generation):
    generation.sort(reverse=True)
    selection = Generation

    for i in range(amount_to_select):
        selection.append(generation[i % len(generation)])

    return selection



