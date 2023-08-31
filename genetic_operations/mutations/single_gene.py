import random
from classes.fighters import *
from genetic_operations.mutations.gene_utils import gene_delta, mutate_gene


def mutate_single_gene(character: Fighter, config):

    # Primero vemos si le toca mutar
    pm = config["mutation_prob"]
    if random.random() >= pm:
        return

    # Mutamos un gen random
    gene_to_mutate = random.randint(0, len(Genes) - 1)

    mutation_change = config["mutation_change"]

    mutate_gene(character, gene_to_mutate, mutation_change)

    # Reajustamos los genes por si quedo fuera de los valores aceptados
    character.readjust_genes()
