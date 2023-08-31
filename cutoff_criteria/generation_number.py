from classes.generation import Generation


def generation_cutoff(generation: Generation, cutoff_value):
    return generation.generation_number >= cutoff_value
