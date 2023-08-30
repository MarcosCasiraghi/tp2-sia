# abstract base class work
from abc import ABC, abstractmethod
from math import pow


def check_valid_height(height):
    return 1.3 <= height <= 2.0


class Fighter(ABC):
    @abstractmethod
    def __init__(self, attack_lambda, stats, height):
        self.attack_lambda = attack_lambda
        self.defense_lambda = 1 - self.attack_lambda
        self.performance = self.get_performance()
        self.stats = stats
        if not check_valid_height(height):
            raise ValueError("Invalid height provided")
        self.height = height

    def get_performance(self):
        return self.attack_lambda * self.get_attack() + self.defense_lambda * self.get_defense()

    def get_atm_mod(self):
        return 0.5 - pow((3 * self.height - 5), 4) + pow((3 * self.height - 5), 2) + self.height/2

    def get_dem_mod(self):
        return 2 + pow((3 * self.height - 5), 4) - pow((3 * self.height - 5), 2) - self.height/2

    def get_attack(self):
        return (self.stats.get_agility() + self.stats.get_expertise()) * self.stats.get_strength() * self.get_atm_mod()

    def get_defense(self):
        return (self.stats.get_resistence() + self.stats.get_expertise) * self.stats.get_hp() * self.get_dem_mod()


class Warrior(Fighter):
    def __init__(self, stats, height):
        super().__init__(0.6, stats, height)


class Archer(Fighter):
    def __init__(self, stats, height):
        super().__init__(0.9, stats, height)


class Defensor(Fighter):
    def __init__(self, stats, height):
        super().__init__(0.1, stats, height)


class Infilitrate(Fighter):
    def __init__(self, stats, height):
        super().__init__(0.8, stats, height)  # todo ver si se confundio con el 0.3
