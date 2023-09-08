import json
import os.path
from datetime import datetime

import numpy as np

from classes.fighters import Genes


# = = = = = = = = = =  Side functions  = = = = = = = = = =

def collect_best_in_gen(gen):
    best = max(gen)

    best_in_gen = {
        "performance": best.performance, "strength": best.strength, "agility": best.agility,
        "expertise": best.expertise, "resistence": best.resistence, "hp": best.hp, "height": best.height
    }

    return best_in_gen


def collect_worst_in_gen(gen):
    best = min(gen)

    worst_in_gen = {
        "performance": best.performance, "strength": best.strength, "agility": best.agility,
        "expertise": best.expertise, "resistence": best.resistence, "hp": best.hp, "height": best.height
    }

    return worst_in_gen


def collect_average_in_gen(gen):
    # NOTAR: si vamos a estar usando esto para cada generacion, es mas eficiente usar variables directamente
    # en vez de un diccionario (que tenes que constantemente calcular el hash)

    performance_sum = 0
    strength_sum = 0
    agility_sum = 0
    expertise_sum = 0
    resistence_sum = 0
    hp_sum = 0
    height_sum = 0

    for elem in gen:
        performance_sum += elem.performance
        strength_sum += elem.strength
        agility_sum += elem.agility
        expertise_sum += elem.expertise
        resistence_sum += elem.resistence
        hp_sum += elem.hp
        height_sum += elem.height

    gen_size = len(gen)
    resp = {
        "performance": performance_sum / gen_size, "strength": strength_sum / gen_size, "agility": agility_sum / gen_size,
        "expertise": expertise_sum / gen_size, "resistence": resistence_sum / gen_size, "hp": hp_sum / gen_size, "height": height_sum / gen_size
    }

    return resp


def calculate_gen_variation(populus, gene_idx):
    values = [character.get_gene_by_idx(gene_idx) for character in populus]
    return np.std(values)


# = = = = = = = = = =  Main functions = = = = = = = = = =


def initialize_metrics(config, metrics):
    metrics["config_used"] = config

    # Para que aparezcan al principio
    metrics["execution_time"] = None
    metrics["number_of_generations"] = None
    metrics["best_in_final_gen"] = None
    metrics["worst_in_final_gen"] = None
    metrics["average_in_final_gen"] = None

    metrics["best_performance_list"] = []
    metrics["worst_performance_list"] = []
    metrics["average_performance_list"] = []
    for gen in Genes:
        metrics[f"{gen.name.lower()}_variation"] = []


def collect_time_metrics(start, end, metrics):
    metrics["execution_time"] = end - start


def collect_metrics_running(current_gen, metrics):
    # Calculo mejor, el peor y el promedio
    metrics["best_performance_list"].append(collect_best_in_gen(current_gen)["performance"])
    metrics["worst_performance_list"].append(collect_worst_in_gen(current_gen)["performance"])
    metrics["average_performance_list"].append(collect_average_in_gen(current_gen)["performance"])

    # Calculo variacion en genes
    for idx, gen in enumerate(Genes):
        metrics[f"{gen.name.lower()}_variation"].append(calculate_gen_variation(current_gen, idx))


def collect_metrics_finished(final_gen, metrics):
    metrics["number_of_generations"] = final_gen.generation_number

    metrics["best_in_final_gen"] = collect_best_in_gen(final_gen)
    metrics["worst_in_final_gen"] = collect_worst_in_gen(final_gen)
    metrics["average_in_final_gen"] = collect_average_in_gen(final_gen)


def export_metrics(metrics):
    now = datetime.now().strftime("%d-%m-%Y_%H%M%S")

    # Exporto las metricas
    with open(f"./results/results_{now}.json", mode="w+") as file:
        file.write(json.dumps(metrics, indent=4))

    # Creo el archivo si no existe
    if not os.path.exists("./results/best/best_configs.json"):
        with open("./results/best/best_configs.json", "w") as new_file:
            empty_map = {}
            for c in ["Warrior", "Archer", "Infilitrate", "Defensor"]:
                empty_map[c] = {
                    "config_used": {},
                    "performance": 0,
                    "strength": 0,
                    "agility": 0,
                    "expertise": 0,
                    "resistence": 0,
                    "hp": 0,
                    "height": 0
                }

            new_file.write(json.dumps(empty_map, indent=4))

    # Malisimo que tengo que abrir y cerrar 3 veces >:[

    # Leo los contenidos
    with open("./results/best/best_configs.json", "r") as best_file:
        best_characters = json.load(best_file)

    # Guardo la configuracion si genero un mejor individuo que el maximo anterior
    best_in_current = metrics["best_in_final_gen"]
    class_used = metrics["config_used"]["class"]

    if best_in_current["performance"] > best_characters[class_used]["performance"]:
        best_characters[class_used]["config_used"] = metrics["config_used"]
        best_characters[class_used]["performance"] = best_in_current["performance"]
        best_characters[class_used]["strength"] = best_in_current["strength"]
        best_characters[class_used]["agility"] = best_in_current["agility"]
        best_characters[class_used]["expertise"] = best_in_current["expertise"]
        best_characters[class_used]["resistence"] = best_in_current["resistence"]
        best_characters[class_used]["hp"] = best_in_current["hp"]
        best_characters[class_used]["height"] = best_in_current["height"]

        with open("./results/best/best_configs.json", "w") as best_file:
            best_file.write(json.dumps(best_characters, indent=4))


