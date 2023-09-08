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


def generate_best_performance_graph(results):
    best_performances = results["best_performance_list"]

    generations = list(range(0, len(best_performances) + 1))

    trace = go.Scatter(x=generations, y=best_performances, mode='markers', name='Best Performance')
    layout = go.Layout(title='Best Performance per Generation',xaxis=dict(title='Generation'),yaxis=dict(title='Best Performance'), xaxis_range=[0, len(generations) - 1])
    fig = go.Figure(data=[trace], layout=layout)
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


generate_graphs()


