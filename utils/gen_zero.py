import random

from classes.fighters import *
from classes.generation import *

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
