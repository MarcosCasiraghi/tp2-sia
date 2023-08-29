from math import tanh
POINTS = 150


class Stats:
    def __init__(self, strength, agility, expertise, resistence, hp):
        self.strength = strength
        self.agility = agility
        self.expertise = expertise
        self.resistence = resistence
        self.hp = hp
        self.stats_array = [self.strength, self.agility, self.expertise, self.resistence, self.hp]

    @classmethod
    def get_stats_quantity(cls):
        return 5

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
