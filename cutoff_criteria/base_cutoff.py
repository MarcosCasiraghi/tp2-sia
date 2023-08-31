from cutoff_criteria.generation_number import generation_cutoff

cutoff_map = {
    "generation_cutoff": generation_cutoff
}


def cutoff(populus, config):
    method = config["cutoff_criteria"]["method"]

    if method == "generation_cutoff":
        return generation_cutoff(populus, config["cutoff_criteria"]["generation_amount"])
    else:
        quit("Invalid mutation method")

