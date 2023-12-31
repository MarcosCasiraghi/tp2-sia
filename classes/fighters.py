# abstract base class work
import random
from abc import ABC, abstractmethod
from enum import Enum
from math import pow, tanh

POINTS = 150
LAST_INDEX = 4
DELTA = 0.0000000001


def valid_height(height):
    return 1.3 <= height <= 2.0


def valid_attribute(strength, agility, expertise, resistance, hp):
    return (0 < strength < 150 and 0 < agility < 150 and 0 < expertise < 150 and 0 < resistance < 150 and 0 < hp < 150
            and - DELTA <= strength + agility + expertise + resistance + hp - 150 <= DELTA)


def scale_array_to_sum(arr):
    initial_sum = 0

    for idx in range(0, LAST_INDEX + 1):
        initial_sum += arr[idx]
    scaling_factor = POINTS / initial_sum

    for idx in range(0, LAST_INDEX + 1):
        arr[idx] = arr[idx] * scaling_factor

    # Ajustamos por los errores de redondeo
    aux_sum = 0
    for idx in range(0, LAST_INDEX + 1):
        aux_sum += arr[idx]

    sum_difference = POINTS - aux_sum

    adjusted = False
    while not adjusted:
        # Seleccionamos uno random para completar a que lleguen a 150
        index_to_complete = random.randint(0, LAST_INDEX)

        if arr[index_to_complete] + sum_difference > 0:
            arr[index_to_complete] += sum_difference
            adjusted = True

    return arr


class Fighter(ABC):
    @abstractmethod
    def __init__(self, attack_lambda, defence_lambda, strength, agility, expertise, resistance, hp, height):
        if not valid_attribute(strength, agility, expertise, resistance, hp):
            raise ValueError("Invalid attributes for character")

        if not valid_height(height):
            raise ValueError("Invalid height provided")

        self.attack_lambda = attack_lambda
        self.defense_lambda = defence_lambda

        self.strength = strength
        self.agility = agility
        self.expertise = expertise
        self.resistance = resistance
        self.hp = hp

        self.height = height

        self.performance = self.calc_performance()

    def calc_performance(self):
        return self.attack_lambda * self.get_attack() + self.defense_lambda * self.get_defense()

    def get_atm_mod(self):
        return 0.5 - pow((3 * self.height - 5), 4) + pow((3 * self.height - 5), 2) + self.height / 2

    def get_dem_mod(self):
        return 2 + pow((3 * self.height - 5), 4) - pow((3 * self.height - 5), 2) - self.height / 2

    def get_attack(self):
        return (self.get_agility() + self.get_expertise()) * self.get_strength() * self.get_atm_mod()

    def get_defense(self):
        return (self.get_resistance() + self.get_expertise()) * self.get_hp() * self.get_dem_mod()

    def get_strength(self):
        return 100 * tanh(0.01 * self.strength)

    def get_agility(self):
        return tanh(0.01 * self.agility)

    def get_expertise(self):
        return 0.6 * tanh(0.01 * self.expertise)

    def get_resistance(self):
        return tanh(0.01 * self.resistance)

    def get_hp(self):
        return 100 * tanh(0.01 * self.hp)

    def get_gene_by_idx(self, idx):

        # TODO: check. Creo que es mas eficiente que hacer una lista y despues obtener el valor por indice

        if idx == 0:
            return self.strength
        elif idx == 1:
            return self.agility
        elif idx == 2:
            return self.expertise
        elif idx == 3:
            return self.resistance
        elif idx == 4:
            return self.hp
        elif idx == 5:
            return self.height

    def set_gene_by_idx(self, idx, value):

        # TODO: check. Creo que es mas eficiente que hacer una lista y despues obtener el valor por indice

        if idx == 0:
            self.strength = value
        elif idx == 1:
            self.agility = value
        elif idx == 2:
            self.expertise = value
        elif idx == 3:
            self.resistance = value
        elif idx == 4:
            self.hp = value
        elif idx == 5:
            self.height = value

    # TODO: muy cabeza esto, arreglar en algun momento
    def readjust_genes(self):
        # Reajustamos la altura
        if self.height > 2.0:
            self.height = 2.0
        elif self.height < 1.3:
            self.height = 1.3

        # Reajustamos los otros genes
        current_genes = [self.strength, self.agility, self.expertise, self.resistance, self.hp]
        scaled = scale_array_to_sum(current_genes)

        for idx, value in enumerate(scaled):
            self.set_gene_by_idx(idx, value)

        self.performance = self.calc_performance()

    def __str__(self):
        return f"strength: {self.strength}, agility: {self.agility}, expertise: {self.expertise}, resistance: {self.resistance}, hp: {self.hp}, height: {self.height}, performance: {self.performance}"

    def __lt__(self, other):
        return self.performance < other.performance


class Warrior(Fighter):
    def __init__(self, strength, agility, expertise, resistance, hp, height):
        super().__init__(0.6, 0.4, strength, agility, expertise, resistance, hp, height)


class Archer(Fighter):
    def __init__(self, strength, agility, expertise, resistance, hp, height):
        super().__init__(0.9, 0.1, strength, agility, expertise, resistance, hp, height)


class Defensor(Fighter):
    def __init__(self, strength, agility, expertise, resistance, hp, height):
        super().__init__(0.1, 0.9, strength, agility, expertise, resistance, hp, height)


class Infiltrate(Fighter):
    def __init__(self, strength, agility, expertise, resistance, hp, height):
        super().__init__(0.8, 0.3, strength, agility, expertise, resistance, hp, height)


class Genes(Enum):
    STRENGTH = 0
    AGILITY = 1
    EXPERTISE = 2
    RESISTANCE = 3
    HP = 4
    HEIGHT = 5


class_map = {
    "Warrior": Warrior,
    "Archer": Archer,
    "Defensor": Defensor,
    "Infiltrate": Infiltrate
}
