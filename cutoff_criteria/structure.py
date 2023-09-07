from classes.generation import Generation
from functools import reduce
from classes.fighters import Fighter

#parte relevante => que % de poblacion no cambia para que criterio de corte se de
# ej: Quiero que 80% no cambie en 
# ej: Que no cambia quiere decir que la diferencia entre alelos no pasa mas que un delta
# ej: No cambiar => Alelos iguales
# ej: Altura no cambia




#  self.strength = strength
#  self.agility = agility
#  self.expertise = expertise
#  self.resistence = resistence
#  self.hp = hp


def obtain_attribute_sum(gen, attribute):
    sum = 0
    for elem in gen:
        sum += getattr(elem,attribute)
    return sum / len(gen)




def structure_cutoff( gen: Generation ,prev_gen_info, delta, delta_height):
    attributes = ["height", "agility", "strength", "expertise", "resistance", "hp"]

    # Inicializamos valores por ser la primera vez
    if "num_unchanged_generations" not in prev_gen_info:
        prev_gen_info["num_unchanged_generations"] = 0

        # iteramos por los atributos
        # sacamos le promedio de cada uno
        for attribute in attributes:
            prev_gen_info[f"avg_{attribute}"] = sum(getattr(fighter, attribute) for fighter in gen) / len(gen)
        return False

    #si es una generacion que no es la primera
    avg_height = obtain_attribute_sum(gen, "height")
    avg_agility = obtain_attribute_sum(gen,"agility")
    avg_strength = obtain_attribute_sum(gen,"strength")
    avg_expertise = obtain_attribute_sum(gen,"expertise")
    avg_resistance = obtain_attribute_sum(gen,"resistance")
    avg_hp = obtain_attribute_sum(gen,"hp")
    # comparamos
    if prev_gen_info["avg_height"] - avg_height < delta:
        
    





