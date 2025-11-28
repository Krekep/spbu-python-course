from config import WORLD_WIDTH, WORLD_HEIGHT
from .field_cell import FieldCell
from core import Observer, Event


class World(Observer):
    def __init__(self) -> None:
        self.width = WORLD_WIDTH
        self.height = WORLD_HEIGHT

        self._grid = []
        self.cells = []

        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append(FieldCell(x - self.width//2, y - self.height//2, x, y))
            self._grid.append(row)

    def on_event(self, event: Event) -> None:
        if event.event_type == "health_on_zero":
            reason = event.data['reason']
            print(f"health of cell is zero: {reason}")
            event.source.is_alive = False

        elif event.event_type == "low_health":
            health = event.data['health_level']
            print(f"Cell has low health: {health}")

        elif event.event_type == "cell_starving":
            print(f"The sell is starving: {event.data['reason']}")
            event.source.current_health -= event.data["damage"]

        elif event.event_type == "cell_dead":
            print(f'Rest in Peace cell')

        elif event.event_type == "new_cell_placement":
            print("Cell changed its location")

        elif event.event_type == "coordinate_changed":
            print(f"Coordinate has changed from {event.data['old']} to {event.data['new']}")

        elif event.event_type == "action_completed":
            print(event.data)
            pass

        if event.event_type == "cell_divided":
            print(f"new cell division")

    def get_field(self, x, y) -> FieldCell:
        return self._grid[x][y]
