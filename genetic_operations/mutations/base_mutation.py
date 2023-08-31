from genetic_operations.mutations.limited_multigen import mutate_limited_multi_gen
from genetic_operations.mutations.single_gene import mutate_single_gene
from genetic_operations.mutations.uniform_multigen import mutate_uniform_multi_gen

mutation_map = {
    "single_gene": mutate_single_gene,
    "mutate_limited_multi_gen": mutate_limited_multi_gen,
    "mutate_uniform_multi_gen": mutate_uniform_multi_gen
}


def mutate_populus(populus, config):
    method = mutation_map[config["mutation_method"]]

    for character in populus:
        method(character, config)

