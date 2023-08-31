import json
from cutoff_criteria.base_cutoff import cutoff
from genetic_operations.crossings.base_crossing import cross_populus
from genetic_operations.mutations.base_mutation import mutate_populus
from selection_algorithms.base_selection import select_populus
from utils.gen_zero import gen_zero


# # la idea aca es levantar la configuracion de un JSON y cambiar la funcion create_fighter por el constructor adecuado
# create_fighter = lambda stats, height: Warrior(stats, height)


def main():
    config = json.load(open("./config.json"))

    # Generate gen 0
    gen = gen_zero(config)

    # Ciclo con criterio de corte
    while cutoff(gen, config):

        # Hacemos la seleccion
        selected = select_populus(gen, config)

        # Hacemos el cruce
        children = cross_populus(selected, config)

        # Mutamos los nuevos
        mutate_populus(children, config)

        # Hacemos el reemplazo (usando los algoritmos de seleccion)
        gen = select_populus(children, config)

    gen.sort(reverse=True)
    print(f"The best character is:\n {gen[0]}")


main()

