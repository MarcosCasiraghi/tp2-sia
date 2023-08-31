import random

from classes.fighters import Fighter, Genes
from genetic_operations.mutations.gene_utils import  mutate_gene


def mutate_uniform_multi_gen(character: Fighter, config):

    pm = config["mutation_prob"]
    mutation_change = config["mutation_change"]

    for i in range(len(Genes)):

        # Primero vemos si le toca mutar este gen especifico
        if random.random() >= pm:
            continue

        mutate_gene(character, i, mutation_change)

    # Reajustamos los genes por si quedo fuera de los valores aceptados
    character.readjust_genes()