from models import Cell
from config import INITIAL_CELL_COUNT


class Player:
    def __init__(self):
        self.inventory = []
        self.selected_cell_index = 0

    def add_cell(self, cell):
        self.inventory.append(cell)

    def get_selected_cell(self):
        if self.inventory:
            return self.inventory[self.selected_cell_index]
        return None

    def next_cell(self):
        if self.inventory:
            self.selected_cell_index = (self.selected_cell_index + 1) % len(self.inventory)

    def prev_cell(self):
        if self.inventory:
            self.selected_cell_index = (self.selected_cell_index - 1) % len(self.inventory)
