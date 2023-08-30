import random
from genetic_operations.mutations.single_gene import mutate_single_gene

mutation_map = {
    "single_gene": mutate_single_gene
}


def mutate_populus(populus, config):
    pm = config["mutation_prob"]
    method = mutation_map[config["mutation_method"]]

    for character in populus:
        if random.random() < pm:
            method(character, config)
