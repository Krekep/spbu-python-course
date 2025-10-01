from __future__ import annotations

from math import acos, isclose, sqrt
from typing import Iterable, Iterator, Sequence, Tuple


class Vector:
    """Immutable dense vector with basic linear algebra operations.

    - Addition/Subtraction: v + w, v - w
    - Scalar multiplication: v * a, a * v
    - Dot product: v @ w
    - Length (Euclidean norm): abs(v)
    - Iteration and indexing supported
    """

    __slots__ = ("_values",)

    def __init__(self, values: Iterable[float]) -> None:
        self._values: Tuple[float, ...] = tuple(float(x) for x in values)
        if len(self._values) == 0:
            raise ValueError("Vector must not be empty")

    def __repr__(self) -> str:  # pragma: no cover
        return f"Vector({list(self._values)!r})"

    def __len__(self) -> int:
        return len(self._values)

    def __iter__(self) -> Iterator[float]:
        return iter(self._values)

    def __getitem__(self, index: int) -> float:
        return self._values[index]

    # Vector addition and subtraction
    def _check_same_size(self, other: Sequence[float]) -> None:
        if len(self) != len(other):
            raise ValueError("Vectors must have the same size")

    def __add__(self, other: "Vector") -> "Vector":
        self._check_same_size(other._values)
        return Vector(a + b for a, b in zip(self._values, other._values))

    def __sub__(self, other: "Vector") -> "Vector":
        self._check_same_size(other._values)
        return Vector(a - b for a, b in zip(self._values, other._values))

    # Scalar multiplication
    def __mul__(self, scalar: float) -> "Vector":
        return Vector(a * float(scalar) for a in self._values)

    def __rmul__(self, scalar: float) -> "Vector":
        return self.__mul__(scalar)

    # Dot product via matrix-multiply operator
    def __matmul__(self, other: "Vector") -> float:
        self._check_same_size(other._values)
        return sum(a * b for a, b in zip(self._values, other._values))

    # Euclidean norm
    def __abs__(self) -> float:
        return sqrt(sum(a * a for a in self._values))

    # Angle between two vectors in radians
    def angle_with(self, other: "Vector") -> float:
        self._check_same_size(other._values)
        denom = abs(self) * abs(other)
        if isclose(denom, 0.0):
            raise ValueError("Angle is undefined for zero-length vectors")
        # Clamp due to possible floating errors
        cos_value = max(-1.0, min(1.0, (self @ other) / denom))
        return acos(cos_value)


__all__ = ["Vector"]
