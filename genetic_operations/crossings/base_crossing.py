import random

from genetic_operations.crossings.two_point_cross import two_point_cross
from genetic_operations.crossings.anular_cross import anular_cross
from genetic_operations.crossings.one_point_cross import one_point_cross
from genetic_operations.crossings.uniform_cross import uniform_cross

crossing_map = {
    "anular_cross": anular_cross,
    "one_point_cross": one_point_cross,
    "two_point_cross": two_point_cross,
    "uniform_cross": uniform_cross
}


def cross_populus(populus, config):
    method = crossing_map[config["crossover_method"]]

    if method is None:
        quit("Invalid mutation method")

    # mezclamos los seleccionados (puede que hayan estado en orden)
    random.shuffle(populus)
    return method(populus)
