import json
from datetime import datetime


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


# = = = = = = = = = =  Main functions = = = = = = = = = =


def initialize_metrics(config, metrics):
    metrics["config_used"] = config
    metrics["best_performance_list"] = []


def collect_time_metrics(start, end, metrics):
    metrics["execution_time"] = end - start


def collect_metrics_running(current_gen, metrics):
    best = max(current_gen)
    metrics["best_performance_list"].append(best.performance)


def collect_metrics_finished(final_gen, metrics):
    metrics["number_of_generations"] = final_gen.generation_number

    metrics["best_in_final_gen"] = collect_best_in_gen(final_gen)
    metrics["worst_in_final_gen"] = collect_worst_in_gen(final_gen)
    metrics["average_in_final_gen"] = collect_average_in_gen(final_gen)


def export_metrics(metrics):
    now = datetime.now().strftime("%d-%m-%Y_%H%M%S")
    with open(f"./results/results_{now}.json", mode="w") as file:
        file.write(json.dumps(metrics, indent=4))
