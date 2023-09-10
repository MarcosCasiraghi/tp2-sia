from cutoff_criteria.acceptable_solution import acceptable_solution_cutoff
from cutoff_criteria.content import content_cutoff
from cutoff_criteria.generation_number import generation_cutoff
from cutoff_criteria.structure import structure_cutoff


def cutoff(populus, config, prev_gen_info):
    method = config["cutoff_criteria"]["method"]

    if method == "generation_cutoff":
        return generation_cutoff(populus, config["cutoff_criteria"]["generation_amount"])
    elif method == "content_cutoff":
        return content_cutoff(populus, config["cutoff_criteria"]["delta"], config["cutoff_criteria"]["max_gen_unchanged"], prev_gen_info)
    elif method == "acceptable_solution_cutoff":
        return acceptable_solution_cutoff(populus, config["cutoff_criteria"]["acceptable_fitness"])
    elif method == "structure_cutoff":
        return structure_cutoff(populus, config["cutoff_criteria"]["delta"], config["cutoff_criteria"]["max_gen_unchanged"], config["cutoff_criteria"]["percentage"], prev_gen_info)
    else:
        quit("Invalid cutoff method")

