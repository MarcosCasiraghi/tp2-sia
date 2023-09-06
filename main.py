import json
import time

from cutoff_criteria.base_cutoff import cutoff
from genetic_operations.crossings.base_crossing import cross_populus
from genetic_operations.mutations.base_mutation import mutate_populus
from selection_algorithms.base_selection import select_populus, replace_populus
from utils.gen_zero import gen_zero
from utils.metrics import *


# # la idea aca es levantar la configuracion de un JSON y cambiar la funcion create_fighter por el constructor adecuado
# create_fighter = lambda stats, height: Warrior(stats, height)


def main():
    config = json.load(open("./config.json"))

    # Aca pondremos las distintas metricas medidas a lo largo del algoritmo
    metrics = {}

    # Guardamos la configuracion usada
    collect_config(config, metrics)

    # Informacion sobre las generaciones anteriores (por si lo necesita el criterio de corte)
    prev_gen_info = {}

    # = - = - = Comienza el algoritmo = - = - =
    start_time = time.time()

    # Generamos la generacion cero
    gen = gen_zero(config)

    # Ciclo con criterio de corte
    while not cutoff(gen, config, prev_gen_info):
        # Hacemos la seleccion
        selected = select_populus(gen, config)

        # Hacemos el cruce
        children = cross_populus(selected, config)

        # Mutamos los nuevos
        mutate_populus(children, config)

        # Hacemos el reemplazo (usando los algoritmos de seleccion)
        gen = replace_populus(children, gen, config)

    # = - = - = Termina el algoritmo = - = - =
    end_time = time.time()

    collect_time_metrics(start_time, end_time, metrics)
    collect_metrics_finished(gen, metrics)

    export_metrics(metrics)


main()
