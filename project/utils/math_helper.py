from sympy import *
from config import WORLD_ALTITUDE_FORMULA, WORLD_TEMPERATURE_FORMULA, WORLD_NUTRIENTS_FORMULA


def altitude(x0: int, y0: int) -> float:
    x, y = symbols('x y')
    return WORLD_ALTITUDE_FORMULA.evalf(subs={x: x0, y: y0})


def temperature(alt: float) -> float:
    z = symbols('z')
    return WORLD_TEMPERATURE_FORMULA.evalf(subs={z: alt})


def nutrients(alt: float) -> float:
    z = symbols('z')
    return WORLD_NUTRIENTS_FORMULA.evalf(subs={z: alt})
