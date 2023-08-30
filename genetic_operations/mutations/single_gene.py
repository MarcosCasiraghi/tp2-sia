import random
from enum import Enum
from classes.fighters import Fighter


class Genes(Enum):
    STRENGTH = 0
    AGILITY = 1
    EXPERTISE = 2
    RESISTANCE = 3
    HP = 4
    HEIGHT = 5


def mutate_single_gene(character: Fighter, config):
    change = random.randint(0, 1) # 1 incrementa y 0 es decrementa
    if change == 1:
        delta = 1
    else:
        delta = -1

    gene_to_mutate = random.randint(0, len(Genes))

    # No es muy lindo asi, pero creo que es lo mas eficiente

    if gene_to_mutate == Genes.HEIGHT:
        new_height = character.height * (1 + delta * config["mutation_change"])

        character.height = new_height

    else:   # Caso: muto los genes regulados por el maximo de 150
        old = character.get_gene_by_idx(gene_to_mutate)
        new_value = old * (1 + delta * config["mutation_change"])

        character.set_gene_by_idx(gene_to_mutate, new_value)

    character.readjust_genes()
