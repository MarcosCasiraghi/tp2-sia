def cross_population(selected_fighters_list: list, crossing_strategy):
    childList = []
    list_length = len(selected_fighters_list)
    for i in range(0, list_length, 2):
        parent1 = selected_fighters_list[i]
        parent2 = selected_fighters_list[(i + 1) % list_length]  # por si la lista es impar
        child1, child2 = crossing_strategy(parent1, parent2)
        childList.append(child1)
        childList.append(child2)
    return childList
