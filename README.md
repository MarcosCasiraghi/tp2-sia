# Trabajo Práctico 2 - SIA

## Requisitos:
1) Python 3
2) Pip 3


## Ejecución:
1) Ejecutar en una linea de comandos (con pip instalado):
```
pip install -r requirements.txt
```
2) Configurar el archivo config.json (se describe la configuración abajo).
3) Ejecutar:
```
python main.py
```
4) Para generar los gráficos asociados a una ejecución ejecutar:
```
python graphs.py <path de archivo>
```
o ejecutar (esta elige el último set de datos generados)
```
python graphs.py
```

## Configuración:
| Campo                    | Descripción                                                                    | Valores aceptados                                                                                                         |  
|--------------------------|--------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| seed                     | Permite especificar el numero inicial usado al generar los valores aleatorios. | Debe entero positivo. Tambien se puede usar -1 si no se quiere usar un seed.                                              |
| class                    | El tipo de personaje que se generara.                                          | "Warrior", "Archer", "Defensor" o "Infiltrate"                                                                            |
| generation_size          | Tamaño de generación.                                                          | Valor entero positivo.                                                                                                    |
| selection_method1        | Especifica que metodo de seleccion se usara.                                   | Debe ser un diccionario con como minimo un campo llamado "method", en donde se especifica el metodo. [Ver tabla numero 1] |
| selection_method2        | Idem anterior.                                                                 | Idem anterior.                                                                                                            | 
| selection_rate_method1   | Define el porcentaje de la seleccion que se hara con el metodo 1.              | Numero de punto flotante entre 0 y 1.                                                                                     |
| selection_size           | Tamaño de poblacion que se elgie para hacer la crusa.                          | Valor entero positivo.                                                                                                    |
| crossover_method         | Define el metodo de crusa usado.                                               | [Ver tabla numero 2]                                                                                                      |
| mutation_method          | Define el metodo de mutacion usado                                             | [Ver tabla numero 3]                                                                                                      |
| mutation_prob            | Define la probabilidad de que un individuo mute.                               | Numero de punto flotante entre 0 y 1.                                                                                     |
| mutation_change          | Define cuanto cambiara cierto gen al mutar.                                    | Numero de punto flotante entre 0 y 1.                                                                                     |
| replacement_method1      | Especifica que metodo de reemplazo se usara.                                   | Debe ser un diccionario con como minimo un campo llamado "method", en donde se especifica el metodo. [Ver tabla numero 1] |
| replacement_method2      | Idem anterior.                                                                 | Idem anterior.                                                                                                            | 
| replacement_rate_method1 | Define el porcentaje de la seleccion que se hara con el metodo 1.              | Numero de punto flotante entre 0 y 1.                                                                                     | 
| favour_children          | Define si se tendra un sesgo joven al reemplazar los individuos.               | Valor booleano. true = sesgo joven.                                                                                       |
| cutoff_criteria          | Especifica el criterio de corte que se usara.                                  | Debe ser un diccionario con como minimo un campo llamado "method", en donde se especifica el metodo. [Ver tabla numero 3] |


## Tabla 1: Metodo de seleccion y reemplazo
| Metodo                              | Parametros                                                                                                        |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| elite_selection                     | -                                                                                                                 | 
| ranking_selection                   | -                                                                                                                 |
| roulette_selection                  | -                                                                                                                 |
| universal_selection                 | -                                                                                                                 |
| boltzmann_selection                 | "temperature_0": La temperatura inicial. "temperature_C": Temperatura limite TODO "k": valor racional entre 0 y 1 |
| deterministic_tournament_selection  | "m_value": Numero entero, cantidad de individuos en torneo                                                        |
| probabilistic_tournament_selection  | "threshold": valor racional entre 0.5 y 1. Cuanto más grande, más favorece al más apto                            | 

## Tabla 2: Metodo de cruza
| Metodo             | 
|--------------------|
| anular_cross       |
| one_point_cross    |
| two_point_cross    |
| uniform_cross      |


 ## Tabla 3: Metodo de mutacion
| Metodo                    |
|---------------------------|
| single_gene               |
| mutate_limited_multi_gen  |
| mutate_uniform_multi_gen  |
| mutate_complete           |



 ## Tabla 4: Criterio de corte
| Metodo                       | Parametros                                                                                                                                                                                                                                                                               |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| generation_cutoff            | "generation_amount": cantidad de generaciones creadas antes de cortar.                                                                                                                                                                                                                   | 
| acceptable_solution_cutoff   | "acceptable_fitness": fitness del mejor individuo deseado.                                                                                                                                                                                                                               |
| content_cutoff               | "delta": diferencia minima entre mejores individuos. "max_gen_unchanged": cantidad de generaciones sin cambio en el mejor fitness                                                                                                                                                        |
| structure_cutoff             | "max_gen_unchanged": cantidad de generaciones pasadas a comparar con la actual. "delta": porcentaje de diferencia maximo que pueden tener los fitness entre generaciones "percentage": porcentaje de la poblacion para incluir en el X porciento con mas fitness y X porciento con menos |
