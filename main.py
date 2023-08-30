import json
import random
from classes.fighters import *
from classes.generation import *

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

def scale_array_to_sum(arr, desired_sum):
    initial_sum = sum(arr)
    scaling_factor = desired_sum / initial_sum

    scaled_array = [num * scaling_factor for num in arr]

    # Ajustamos por los errores de redondeo
    sum_difference = desired_sum - sum(scaled_array)
    scaled_array[-1] += sum_difference

    return scaled_array


def gen_random_character(config):
    attributes = []

    for _ in range(NUM_ATTRIBUTES):
        value = random.uniform(0, MAX_POINTS)
        attributes.append(value)

    # Normalizamos a que la suma sea 150
    scaled = scale_array_to_sum(attributes, MAX_POINTS)

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

        # Hacemos el cruce

        # Hacemos la mutacion

        # Hacemos el reemplazo (usando los algoritmos de seleccion)
            # calcular la brecha



main()
