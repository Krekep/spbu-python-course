from __future__ import annotations
from core import Cell_metaclass, Observable, HealthDescriptor, StomachDescriptor,\
    CoordinateDescriptor, IsAliveDescriptor
from .gene import Gene
from random import uniform
from .action_type import ActionType
from core import auto_update_state


class Cell(Observable, metaclass=Cell_metaclass):
    current_health = HealthDescriptor()
    stomach = StomachDescriptor()
    x = CoordinateDescriptor()
    y = CoordinateDescriptor()
    is_alive = IsAliveDescriptor()

    def __init__(self, gene: Gene = None) -> None:
        super().__init__()
        if gene:
            if gene.mutation_rate >= uniform(0, 1):
                self.gene = Gene(old_gene=gene)
            else:
                self.gene = gene
        else:
            self.gene = Gene()

        self.world = None
        self._current_health = self.gene.max_health
        self._stomach = 0.0
        self.cell_field = None

    @auto_update_state
    def _eat(self) -> None:
        got = min(self.gene.hunger * 1.5, self.cell_field.nutrients)
        self.cell_field.nutrients -= got
        self.stomach += got

    @auto_update_state
    def _rest(self) -> None:
        self.stomach -= self.gene.hunger / 2

    @auto_update_state
    def _divide(self) -> None:
        if (self.stomach >= 50 and
                self.current_health >= self.gene.max_health * 0.6 and
                self.is_alive):
            new_cell = Cell(self.gene)

            new_cell._current_health = self.current_health * 0.4
            new_cell._stomach = self.stomach * 0.3

            self.current_health *= 0.6
            self.stomach *= 0.7

            from core.observer import Event
            self.notify_observers(Event(
                event_type="cell_divided",
                data={
                    'parent': self,
                    'child': new_cell,
                    'parent_health_after': self.current_health,
                    'parent_stomach_after': self.stomach
                },
                source=self
            ))

    @auto_update_state
    def _metabolize(self) -> None:
        taken = min(self.stomach, self.gene.max_health - self.current_health)
        self.stomach -= taken
        self.current_health += taken

    def handle_action(self, do: ActionType) -> None:
        if do == ActionType.EAT:
            self._eat()
        elif do == ActionType.DIVIDE:
            self._divide()
        elif do == ActionType.REST:
            self._rest()
        elif do == ActionType.METABOLIZE:
            self._metabolize()

    def update(self) -> None:
        if self.is_alive and self.x is not None and self.cell_field is not None:
            if hasattr(self.cell_field, 'temperature'):
                temp = self.cell_field.temperature
                if temp < self.gene.max_cold:
                    self.current_health -= abs(self.gene.max_cold - temp)
                elif temp > self.gene.max_heat:
                    self.current_health -= abs(self.gene.max_heat - temp)

    def get_display_char(self):
        return '(*)' if self.is_alive else '[ ]'

    def placement(self, world, x: int, y: int) -> None:
        self.world = world
        self.x = x
        self.y = y
        self.cell_field = self.world.get_field(x, y)

        if world not in self._observers:
            self.add_observer(world)
