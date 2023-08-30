# abstract base class work
from abc import ABC, abstractmethod
from math import pow, tanh


POINTS = 150


def check_valid_height(height):
    return 1.3 <= height <= 2.0


class Fighter(ABC):
    @abstractmethod
    def __init__(self, attack_lambda, defence_lambda, strength, agility, expertise, resistence, hp, height):
        self.attack_lambda = attack_lambda
        self.defense_lambda = defence_lambda

        self.strength = strength
        self.agility = agility
        self.expertise = expertise
        self.resistence = resistence
        self.hp = hp

        if not check_valid_height(height):
            raise ValueError("Invalid height provided")
        self.height = height

        self.performance = self.get_performance()

    def get_performance(self):
        return self.attack_lambda * self.get_attack() + self.defense_lambda * self.get_defense()

    def get_atm_mod(self):
        return 0.5 - pow((3 * self.height - 5), 4) + pow((3 * self.height - 5), 2) + self.height/2

    def get_dem_mod(self):
        return 2 + pow((3 * self.height - 5), 4) - pow((3 * self.height - 5), 2) - self.height/2

    def get_attack(self):
        return (self.get_agility() + self.get_expertise()) * self.get_strength() * self.get_atm_mod()

    def get_defense(self):
        return (self.get_resistence() + self.get_expertise()) * self.get_hp() * self.get_dem_mod()

    def get_strength(self):
        return 100 * tanh(0.01 * self.strength)

    def get_agility(self):
        return tanh(0.01 * self.agility)

    def get_expertise(self):
        return 0.6 * tanh(0.01 * self.expertise)

    def get_resistence(self):
        return tanh(0.01 * self.resistence)

    def get_hp(self):
        return tanh(0.01 * self.hp)

    def check_valid(self):
        return self.strength + self.agility + self.expertise + self.resistence + self.hp == POINTS

    def __str__(self):
        return f"strength: {self.strength}, agility: {self.agility}, expertise: {self.expertise}, resistance: {self.resistence}, hp: {self.hp}, height: {self.height}"


class Warrior(Fighter):
    def __init__(self, strength, agility, expertise, resistence, hp, height):
        super().__init__(0.6, 0.4, strength, agility, expertise, resistence, hp, height)


class Archer(Fighter):
    def __init__(self, strength, agility, expertise, resistence, hp, height):
        super().__init__(0.9, 0.1, strength, agility, expertise, resistence, hp, height)


class Defensor(Fighter):
    def __init__(self, strength, agility, expertise, resistence, hp, height):
        super().__init__(0.1, 0.9, strength, agility, expertise, resistence, hp, height)


class Infilitrate(Fighter):
    def __init__(self, strength, agility, expertise, resistence, hp, height):
        super().__init__(0.8, 0.3, strength, agility, expertise, resistence, hp, height)
