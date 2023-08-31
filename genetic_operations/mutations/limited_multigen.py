import random
from classes.fighters import Fighter, Genes
from genetic_operations.mutations.gene_utils import gene_delta, mutate_gene


def mutate_limited_multi_gen(character: Fighter, config):

    # Primero vemos si le toca mutar
    pm = config["mutation_prob"]
    if random.random() >= pm:
        return

    # Generamos cuantos genes se van a mutar
    gene_mutation_range = random.randint(0, len(Genes) - 1)

    mutation_change = config["mutation_change"]

    for i in range(0, gene_mutation_range):

        mutate_gene(character, i, mutation_change)

    # Reajustamos los genes por si quedo fuera de los valores aceptados
    character.readjust_genes()
