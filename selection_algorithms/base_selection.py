import math

from classes.generation import *
from selection_algorithms.boltzmann import boltzmann_selection
from selection_algorithms.deterministic_tournament import deterministic_tournament_selection
from selection_algorithms.elite import elite_selection
from selection_algorithms.probabilistic_tournament import probabilistic_tournament_selection
from selection_algorithms.ranking import ranking_selection
from selection_algorithms.roulette import roulette_selection
from selection_algorithms.universal import universal_selection


# = - = - = - = - = - = Metodos auxiliares = - = - = - = - = - =

def remove_from_populus(populus, selected):

    # TODO: guarda con la eficiencia

    for item in reversed(populus):
        if item in selected:
            populus.remove(item)


# Llama el metodo apropiado, pasandole los parametros
def call_method(populus, method_name, selection_size, config, prev_gen_info):
    if selection_size <= 0:
        return []

    method = config[method_name]["method"]

    if method == "boltzmann_selection":
        return boltzmann_selection(selection_size, populus, config[method_name]['temperature_0'], config[method_name]['temperature_C'], config[method_name]['k'], prev_gen_info)
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


# Calculo el tamano del para cada metodo y llamamos el metodo
def size_and_call(populus, selection_size, rate, method_name1, method_name2, config, prev_gen_info):
    size1 = round(selection_size * rate)
    size2 = selection_size - size1

    # Elegimos de los padres
    s1 = call_method(populus, method_name1, size1, config, prev_gen_info)
    s2 = call_method(populus, method_name2, size2, config, prev_gen_info)

    return s1, s2


# = - = - = - = - = - = Metodos de seleccion y reemplazo = - = - = - = - = - =

def select_populus(populus, config, prev_gen_info):

    s1, s2 = size_and_call(populus, config["selection_size"], config["selection_rate_method1"],
                           "selection_method1", "selection_method2", config, prev_gen_info)

    s1.extend(s2)
    return s1


def replace_populus(children, parent_generation, config, prev_gen_info):
    gen = Generation()  # Nueva generacion
    gen_size = config["generation_size"]

    if config["favour_children"] == True:
        if len(children) < gen_size:

            # Entran todos los hijos por default
            gen.extend(children)

            # Lo que queda para completar, lo hacemos con los 2 metodos
            remaining_size = gen_size - len(children)

            s1, s2 = size_and_call(parent_generation, remaining_size, config["replacement_rate_method1"],
                                   "replacement_method1", "replacement_method2", config, prev_gen_info)

            gen.extend(s1)
            gen.extend(s2)

        elif len(children) > gen_size:

            s1, s2 = size_and_call(children, gen_size, config["replacement_rate_method1"],
                                   "replacement_method1", "replacement_method2", config, prev_gen_info)

            gen.extend(s1)
            gen.extend(s2)

        else:  # Caso: cant. de children = gen_size

            # Tomamos solo los hijos
            gen.extend(children)

    else:  # Caso: tradicional

        # Ahora tomamos los hijos y padres por igual
        parent_generation.extend(children)

        s1, s2 = size_and_call(parent_generation, gen_size, config["replacement_rate_method1"],
                               "replacement_method1", "replacement_method2", config, prev_gen_info)

        gen.extend(s1)
        gen.extend(s2)

    return gen
