import json
import random
from classes.fighters import *
from classes.generation import *
from selection_algorithms.elite import *
from genetic_operations.crossings.uniform_cross import uniform_cross
# # la idea aca es levantar la configuracion de un JSON y cambiar la funcion create_fighter por el constructor adecuado
# create_fighter = lambda stats, height: Warrior(stats, height)

class_map = {
    "Warrior": Warrior,
    "Fighter": Fighter,
    "Archer":  Archer,
    "Defensor": Defensor,
    "Infilitrate": Infilitrate
}

NUM_ATTRIBUTES = 5
MAX_POINTS = 150



def gen_random_character(config):
    attributes = []

    for _ in range(NUM_ATTRIBUTES):
        value = random.uniform(0, MAX_POINTS)
        attributes.append(value)

    # Normalizamos a que la suma sea 150, ya lo declara scale_array_to_sum
    scaled = scale_array_to_sum(attributes)

    height = random.uniform(1.3, 2)

    return class_map[config["class"]](*scaled, height)


def gen_zero(config):

    size = config["generation_size"]
    generation = Generation()

    for _ in range(size):
        generation.append(gen_random_character(config))

    return generation


def main():
    config = json.load(open("./config.json"))

    # Generate gen 0
    zero = gen_zero(config)

    # Ciclo con criterio de corte

    # Hacemos la seleccion
    selected = elite_selection(10,zero)

    # Hacemos el cruce
    

        # Hacemos la mutacion

        # Hacemos el reemplazo (usando los algoritmos de seleccion)
            # calcular la brecha



main()

