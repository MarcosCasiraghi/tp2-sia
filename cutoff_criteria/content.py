from classes.generation import Generation


def content_cutoff(new_gen: Generation, delta, max_gen_unchanged, prev_gen_info):
    new_best = max(new_gen)

    # Inicializo el objeto
    if "prev_best" not in prev_gen_info:
        prev_gen_info["prev_best"] = 0
    if "num_unchanged_gens" not in prev_gen_info:
        prev_gen_info["num_unchanged_gens"] = 0

    # Me fijo si el mejor fitness no cambio hace varias generaciones
    if prev_gen_info["prev_best"] - delta <= new_best.performance <= prev_gen_info["prev_best"] + delta:
        prev_gen_info["num_unchanged_gens"] += 1
    else:
        prev_gen_info["prev_best"] = new_best.performance
        prev_gen_info["num_unchanged_gens"] = 0

    return prev_gen_info["num_unchanged_gens"] >= max_gen_unchanged

