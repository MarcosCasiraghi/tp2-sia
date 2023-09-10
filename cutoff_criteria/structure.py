from classes.generation import Generation
from collections import deque

def structure_cutoff(gen: Generation, delta, generation_quantity, percentage, prev_gen_info):
    if 'structure_cutoff_info' not in prev_gen_info:
        prev_gen_info['structure_cutoff_info'] = deque(maxlen=generation_quantity)

    sorted_generation = sorted(gen, reverse=True)  # sort the current generation from best to worst in performance
    generations_performance_info = prev_gen_info['structure_cutoff_info']
    generations_performance_info.append({
        'best': get_first_x_percent(sorted_generation, percentage),
        'worst': get_last_x_percent(sorted_generation, percentage),
        'mean': get_mean(sorted_generation)
    })
    if len(generations_performance_info) < generation_quantity:
        return False

    mean_performances = get_mean_performances(generations_performance_info)
    for index in mean_performances:
        for gen_info in generations_performance_info:
            if abs(mean_performances[index] - gen_info[index]) / mean_performances[index] > delta:
                return False
    return True


# get mean performance of the best X percent of population
def get_first_x_percent(gen, percentage):
    amount = round(len(gen) * percentage)
    first_x_percent = gen[:amount]
    sum = 0
    for fighter in first_x_percent:
        sum += fighter.calc_performance()
    return sum / amount


# get mean performance of the worst X percent of population
def get_last_x_percent(gen, percentage):
    amount = round(len(gen) * percentage)
    last_x_percent = gen[-amount:]
    sum = 0
    for fighter in last_x_percent:
        sum += fighter.calc_performance()
    return sum / amount


# get mean performance of all population
def get_mean(gen):
    sum = 0
    for fighter in gen:
        sum += fighter.calc_performance()
    return sum / len(gen)


def get_mean_performances(generations_performance_info):
    mean_performances = {
        "best": 0,
        "worst": 0,
        "mean": 0
    }

    for index in mean_performances:
        for gen_performance in generations_performance_info:
            mean_performances[index] += gen_performance[index]

    for index in mean_performances:
        mean_performances[index] /= len(generations_performance_info)

    return mean_performances
