from classes.generation import Generation


def acceptable_solution_cutoff(generation: Generation, acceptable_fitness):
    new_best = max(generation)

    # El mejor tiene mas (o igual) fitness que la solucion acceptable
    return new_best.performance >= acceptable_fitness
