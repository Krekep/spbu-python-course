from utils import *


class FieldCell:
    def __init__(self, x0: int, y0: int, x: int, y: int) -> None:
        self.x = x
        self.y = y

        self.alt = altitude(x0, y0)
        self.temperature = temperature(self.alt)
        self.nutrients = nutrients(self.alt)

        self.cell = None
