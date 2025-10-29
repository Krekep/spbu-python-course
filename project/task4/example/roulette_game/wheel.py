from random import randint
from typing import Dict, Any

from project.task4.example.roulette_game.enums import Color


class RouletteWheel:
    """Class representing a roulette wheel.

    Attributes:
        red_numbers (List[int]): List of red numbers
        black_numbers (List[int]): List of black numbers
    """

    def __init__(self):
        self.red_numbers = [
            1,
            3,
            5,
            7,
            9,
            12,
            14,
            16,
            18,
            19,
            21,
            23,
            25,
            27,
            30,
            32,
            34,
            36,
        ]
        self.black_numbers = [
            2,
            4,
            6,
            8,
            10,
            11,
            13,
            15,
            17,
            20,
            22,
            24,
            26,
            28,
            29,
            31,
            33,
            35,
        ]

    def spin(self) -> Dict[str, Any]:
        """Spins the roulette wheel

        Returns:
            Dict: Dictionary containing:
                - number (int): Winning number
                - color (str): 'red', 'black', or 'green' for 0
                - is_even (bool): True if even number, False if odd or zero
                - range (str): 'zero', '1-18', or '19-36'
        """
        winning_number = randint(0, 36)
        return {
            "number": winning_number,
            "color": self._get_color(winning_number),
            "is_even": self._is_even(winning_number),
            "range": self._get_range(winning_number),
        }

    def _get_color(self, number: int) -> Color:
        """Determines color

        Parameters:
            number (int): Winning number

        Returns:
            str: 'green' for 0, 'red' or 'black' for other numbers
        """

        if number in self.black_numbers:
            return Color.BLACK
        elif number in self.red_numbers:
            return Color.RED
        else:
            return Color.GREEN

    def _is_even(self, number: int) -> bool:
        """Checks if number is even.

        Parameters:
            number (int): Number to check

        Returns:
            bool: True if even and not zero, else False
        """
        return number % 2 == 0 if number != 0 else False

    def _get_range(self, number: int) -> str:
        """Determines range

        Parameters:
            number (int): Winning number

        Returns:
            str: 'zero' for 0, '1-18' for numbers 1-18, '19-36' for numbers 19-36
        """
        if number == 0:
            return "zero"
        elif 1 <= number <= 18:
            return "1-18"
        else:
            return "19-36"
