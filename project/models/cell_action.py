from .cell import Cell
from typing import Generator
from .action_type import ActionType


class CellActions:
    @staticmethod
    def can_eat(cell: Cell) -> bool:
        return (cell.cell_field is not None and
                hasattr(cell.cell_field, 'nutrients') and
                cell.cell_field.nutrients > 0)

    @staticmethod
    def can_divide(cell: Cell) -> bool:
        return (cell.stomach >= 50 and
                cell.current_health >= cell.gene.max_health * 0.6 and
                cell.is_alive)

    @staticmethod
    def can_metabolize(cell: Cell) -> bool:
        return cell.stomach > 0

    @staticmethod
    def get_available_actions(cell: Cell) -> list[ActionType]:
        available = []

        if CellActions.can_eat(cell):
            available.append(ActionType.EAT)
        if CellActions.can_divide(cell):
            available.append(ActionType.DIVIDE)
        if CellActions.can_metabolize(cell):
            available.append(ActionType.METABOLIZE)
        if cell.is_alive:
            available.append(ActionType.REST)

        return available

    @staticmethod
    def choose_action(cell: Cell) -> ActionType:
        available = CellActions.get_available_actions(cell)

        if not available:
            return ActionType.REST

        if cell.current_health <= 20:
            if ActionType.METABOLIZE in available and cell.stomach > 0:
                return ActionType.METABOLIZE
            if ActionType.EAT in available:
                return ActionType.EAT

        if ActionType.DIVIDE in available:
            return ActionType.DIVIDE

        return available[0]

    @staticmethod
    def action_generator(cell: Cell) -> Generator[ActionType, None, None]:
        while cell.is_alive:
            next_action = CellActions.choose_action(cell)
            yield next_action
