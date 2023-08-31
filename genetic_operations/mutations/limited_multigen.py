import random
from classes.fighters import Fighter, Genes
from genetic_operations.mutations.gene_utils import gene_delta, mutate_gene


def mutate_limited_multi_gen(character: Fighter, config):

    # Primero vemos si le toca mutar
    pm = config["mutation_prob"]
    if random.random() >= pm:
        return

    num_genes_to_mutate = random.randint(1, len(Genes))

    genes = [0, 1, 2, 3, 4, 5]
    # Generamos cuantos genes se van a mutar
    genes_to_mutate = random.sample(genes, k=num_genes_to_mutate)

    mutation_change = config["mutation_change"]

    for i in genes_to_mutate:
        mutate_gene(character, i, mutation_change)

    # Reajustamos los genes por si quedo fuera de los valores aceptados
    character.readjust_genes()
