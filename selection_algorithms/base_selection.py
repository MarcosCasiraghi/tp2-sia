from selection_algorithms.boltzmann import boltzmann_selection
from selection_algorithms.deterministic_tournament import deterministic_tournament_selection
from selection_algorithms.elite import elite_selection
from selection_algorithms.probabilistic_tournament import probabilistic_tournament_selection
from selection_algorithms.ranking import ranking_selection
from selection_algorithms.roulette import roulette_selection
from selection_algorithms.universal import universal_selection


def select_populus(populus, config, selection=True):
    if selection:
        method = config["selection_method1"]["method"]
    else:
        method = config["replacement_method1"]["method"]

    selection_size = config["selection_size"]

    if method == "boltzmann_selection":
        return boltzmann_selection(selection_size, populus, config["selection_method1"]['selection_temperature'])
    elif method == "deterministic_tournament_selection":
        return deterministic_tournament_selection(selection_size, populus, config["selection_method1"]['m_value'])
    elif method == "probabilistic_tournament_selection":
        return probabilistic_tournament_selection(selection_size, populus, config["selection_method1"]['threshold'])

    elif method == "elite_selection":
        return elite_selection(selection_size, populus)
    elif method == "ranking_selection":
        return ranking_selection(selection_size, populus)
    elif method == "roulette_selection":
        return roulette_selection(selection_size, populus)
    elif method == "universal_selection":
        return universal_selection(selection_size, populus)
    else:
        quit("Invalid selection method")

