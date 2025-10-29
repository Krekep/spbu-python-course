from enum import Enum


class BetType(Enum):
    NUMBER = "number"
    COLOR = "color"
    EVEN_ODD = "even_odd"
    DOZEN = "dozen"
    COLUMN = "column"
    HALF = "half"


class Color(Enum):
    RED = "red"
    BLACK = "black"
    GREEN = "green"


class EvenOdd(Enum):
    EVEN = "even"
    ODD = "odd"


class Dozen(Enum):
    FIRST = "1st"
    SECOND = "2nd"
    THIRD = "3rd"


class Half(Enum):
    FIRST_18 = "1-18"
    LAST_18 = "19-36"
