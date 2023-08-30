
from classes.fighters import *

def get_fighter_class(fighter: Fighter):
    if isinstance(fighter,Archer):
        return Archer
    if isinstance(fighter,Warrior):
        return Warrior
    if isinstance(fighter,Defensor):
        return Defensor
    if isinstance(fighter,Infilitrate):
        return Infilitrate
    raise ValueError("This isnt a fighter type")