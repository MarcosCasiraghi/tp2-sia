import json
import os
import plotly.graph_objects as go


def generate_gene_variation_graph(results):

    generations = list(range(0, len(results["strength_variation"]) + 1))

    traces = [
        go.Scatter(x=generations, y=results["strength_variation"], mode='markers', name='Strength Variation'),
        go.Scatter(x=generations, y=results["agility_variation"], mode='markers', name='Agility Variation'),
        go.Scatter(x=generations, y=results["expertise_variation"], mode='markers', name='Expertise Variation'),
        go.Scatter(x=generations, y=results["resistance_variation"], mode='markers', name='Resistance Variation'),
        go.Scatter(x=generations, y=results["hp_variation"], mode='markers', name='HP Variation')
    ]

    layout = go.Layout(
        title='Gene Variations',
        xaxis=dict(title='Generation'),
        yaxis=dict(title='Standard Deviation'),
        xaxis_range=[0, len(generations) - 1]
    )

    fig = go.Figure(data=traces, layout=layout)
    fig.show()

def generate_variation_rate_of_change_graph(results):

    strength_variation = results["strength_variation"]
    agility_variation = results["agility_variation"]
    expertise_variation = results["expertise_variation"]
    resistance_variation = results["resistance_variation"]
    hp_variation = results["hp_variation"]

    strength_rate = [0] + [strength_variation[i] - strength_variation[i - 1] for i in range(1, len(strength_variation))]
    agility_rate = [0] + [agility_variation[i] - agility_variation[i - 1] for i in range(1, len(agility_variation))]
    expertise_rate = [0] + [expertise_variation[i] - expertise_variation[i - 1] for i in range(1, len(expertise_variation))]
    resistance_rate = [0] + [resistance_variation[i] - resistance_variation[i - 1] for i in range(1, len(resistance_variation))]
    hp_rate = [0] + [hp_variation[i] - hp_variation[i - 1] for i in range(1, len(hp_variation))]

    generations = list(range(0, len(results["strength_variation"]) + 1))

    strength_trace = go.Scatter(x=generations, y=strength_rate, mode='markers', name='Strength Rate of Change')
    agility_trace = go.Scatter(x=generations, y=agility_rate, mode='markers', name='Agility Rate of Change')
    expertise_trace = go.Scatter(x=generations, y=expertise_rate, mode='markers', name='Expertise Rate of Change')
    resistance_trace = go.Scatter(x=generations, y=resistance_rate, mode='markers',
                                  name='Resistance Rate of Change')
    hp_trace = go.Scatter(x=generations, y=hp_rate, mode='markers', name='HP Rate of Change')

    layout = go.Layout(
        title='Rate of Change of Genetic Algorithm Variations',
        xaxis=dict(title='Generation'),
        yaxis=dict(title='Rate of Change'),
        xaxis_range=[0, len(generations) - 1]
    )

    # Create the figure and show it
    fig = go.Figure(data=[strength_trace, agility_trace, expertise_trace, resistance_trace, hp_trace], layout=layout)
    fig.show()


def generate_best_performance_graph(results):

    generations = list(range(0, len(results["best_performance_list"]) + 1))

    trace = [
        go.Scatter(x=generations, y=results["best_performance_list"], mode='markers', name='Best Performance'),
        go.Scatter(x=generations, y=results["worst_performance_list"], mode='markers', name='Worst Performance'),
        go.Scatter(x=generations, y=results["average_performance_list"], mode='markers', name='Average Performance')
    ]
    layout = go.Layout(
        title='Best, Worst and Average Performance per Generation',
        xaxis=dict(title='Generation'),
        yaxis=dict(title='Performance'),
        xaxis_range=[0, len(generations) - 1]
    )
    fig = go.Figure(data=trace, layout=layout)
    fig.show()


# Genera graficos de los resultados especificados (o usa el ultimo set de resultados)
def generate_graphs(file_name=None):
    if file_name is None:
        path = "./results"
        files = os.listdir(path)
        files.sort()
        file_name = f"{path}/{files[-2]}"

    with open(file_name) as file:
        results = json.load(file)

    generate_best_performance_graph(results)
    generate_gene_variation_graph(results)
    generate_variation_rate_of_change_graph(results)


generate_graphs()


