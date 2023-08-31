from selection_algorithms.boltzmann import boltzmann_selection
from selection_algorithms.elite import elite_selection
from selection_algorithms.roulette import roulette_selection



def select_populus(populus, config, selection=True):
    if selection:
        method = config["selection_method1"]
    else:
        method = config["replacement_method1"]

    if method == "boltzmann_selection":
        return boltzmann_selection(config["selection_size"], populus, config['selection_temperature'])
    elif method == "elite_selection" or method == "roulette_selection":
        return elite_selection(config["selection_size"], populus)
    else:
        quit("Invalid selection method")

