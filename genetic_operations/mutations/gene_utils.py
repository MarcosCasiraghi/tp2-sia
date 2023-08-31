import random

from classes.fighters import Fighter, Genes


def gene_delta():
    # Vemos si aumenta o decrementa el gen
    change = random.randint(0, 1)  # 1 incrementa y 0 es decrementa
    if change == 1:
        return 1
    else:
        return -1


def mutate_gene(character: Fighter, gene_idx, mutation_change):
    # Vemos si suma o resta el cambio
    delta = gene_delta()

    # Alteramos el gen especifico
    if gene_idx == Genes.HEIGHT:
        new_height = character.height * (1 + delta * mutation_change)
        character.height = new_height

    else:  # Caso: muto los genes regulados por el maximo de 150
        old = character.get_gene_by_idx(gene_idx)
        new_value = old * (1 + delta * mutation_change)
        character.set_gene_by_idx(gene_idx, new_value)