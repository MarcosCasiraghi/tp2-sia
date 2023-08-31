import random
from classes.fighters import *
from genetic_operations.mutations.gene_utils import gene_delta, mutate_gene


def mutate_complete(character: Fighter, config):

    # Primero vemos si le toca mutar
    pm = config["mutation_prob"]
    if random.random() >= pm:
        return

    mutation_change = config["mutation_change"]

    for gene_to_mutate in Genes:
        mutate_gene(character, gene_to_mutate, mutation_change)

    # Reajustamos los genes por si quedo fuera de los valores aceptados
    character.readjust_genes()
