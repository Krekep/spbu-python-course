from __future__ import annotations
from random import uniform
from config import *


class Gene:
    def __init__(self, old_gene: Gene = None) -> None:
        if old_gene:
            self.max_heat = old_gene.max_heat * (1 + uniform(-.5, .5))
            self.max_cold = old_gene.max_cold * (1 + uniform(-.5, .5))
            self.max_health = old_gene.max_health * (1 + uniform(-.5, .5))
            self.hunger = old_gene.hunger * (1 + uniform(-.5, .5))
            self.mutation_rate = old_gene.mutation_rate * (1 + uniform(-.5, .5))
        else:
            self.max_heat = MAX_HEAT_INITIAL
            self.max_cold = MAX_COLD_INITIAL
            self.max_health = MAX_HEALTH_INITIAL
            self.hunger = HUNGER_INITIAL
            self.mutation_rate = MUTATION_RATE_INITIAL

    def adaptation(self):
        pass
