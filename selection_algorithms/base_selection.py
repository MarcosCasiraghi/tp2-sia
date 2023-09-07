import math

from classes.generation import *
from selection_algorithms.boltzmann import boltzmann_selection
from selection_algorithms.deterministic_tournament import deterministic_tournament_selection
from selection_algorithms.elite import elite_selection
from selection_algorithms.probabilistic_tournament import probabilistic_tournament_selection
from selection_algorithms.ranking import ranking_selection
from selection_algorithms.roulette import roulette_selection
from selection_algorithms.universal import universal_selection


def call_method(populus, method_name, selection_size, config):
    method = config[method_name]["method"]

    if method == "boltzmann_selection":
        return boltzmann_selection(selection_size, populus, config[method_name]['temperature_0'], config[method_name]['temperature_C'], config[method_name]['k'])
    elif method == "deterministic_tournament_selection":
        return deterministic_tournament_selection(selection_size, populus, config[method_name]['m_value'])
    elif method == "probabilistic_tournament_selection":
        return probabilistic_tournament_selection(selection_size, populus, config[method_name]['threshold'])

    elif method == "elite_selection":
        return elite_selection(selection_size, populus)
    elif method == "ranking_selection":
        return ranking_selection(selection_size, populus)
    elif method == "roulette_selection":
        return roulette_selection(selection_size, populus)
    elif method == "universal_selection":
        return universal_selection(selection_size, populus)
    else:
        quit("Invalid selection method")


def select_populus(populus, config):
    selection_size = config["selection_size"]

    size1 = round(selection_size * config["selection_rate_method1"])
    size2 = selection_size - size1

    s1 = call_method(populus, "selection_method1", size1, config)
    s2 = call_method(populus, "selection_method2", size2, config)

    # TODO: eficiencia por favor
    s1.extend(s2)
    return s1


def replace_populus(children, parent_generation, config):
    gen = Generation()  # Nueva generacion
    gen_size = config["generation_size"]

    if config["favour_children"] == True:
        if len(children) < gen_size:

            # Cuantos espacios quedan en la nueva generacion
            remaining_size = gen_size

            # Entran todos los hijos por default
            gen.extend(children)

            # Lo que queda para completar, lo hacemos con los 2 metodos
            remaining_size -= len(children)
            size1 = round(remaining_size * config["replacement_rate_method1"])
            size2 = remaining_size - size1

            # Elegimos de los padres
            s1 = call_method(parent_generation, "replacement_method1", size1, config)
            s2 = call_method(parent_generation, "replacement_method2", size2, config)

            gen.extend(s1)
            gen.extend(s2)

        elif len(children) > gen_size:
            size1 = round(gen_size * config["replacement_rate_method1"])
            size2 = gen_size - size1

            # Elegimos solo de los hijos, al tener suficiente para completar la generacion
            s1 = call_method(children, "replacement_method1", size1, config)
            s2 = call_method(children, "replacement_method2", size2, config)

            gen.extend(s1)
            gen.extend(s2)

        else:  # Caso: cant. de children = gen_size

            # Tomamos solo los hijos
            gen.extend(children)


    else:  # Caso: tradicional

        # Ahora tomamos los hijos y padres por igual
        parent_generation.extend(children)

        size1 = round(gen_size * config["replacement_rate_method1"])
        size2 = gen_size - size1

        s1 = call_method(parent_generation, "replacement_method1", size1, config)
        s2 = call_method(parent_generation, "replacement_method2", size2, config)

        gen.extend(s1)
        gen.extend(s2)

    return gen
