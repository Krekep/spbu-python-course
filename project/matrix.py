from __future__ import annotations

from typing import Iterable, Iterator, List, Sequence, Tuple


class Matrix:
    """Immutable dense matrix with basic operations.

    - Addition: A + B
    - Multiplication: A * B (matrix-matrix) and A * a (scalar)
    - Transpose: A.T
    """

    __slots__ = ("_m", "_n", "_values")

    def __init__(self, rows: Iterable[Iterable[float]]):
        materialized: List[Tuple[float, ...]] = [
            tuple(float(x) for x in row) for row in rows
        ]
        if not materialized or not materialized[0]:
            raise ValueError("Matrix must not be empty")
        n = len(materialized[0])
        for r in materialized:
            if len(r) != n:
                raise ValueError("All rows must have the same length")
        self._m = len(materialized)
        self._n = n
        self._values: Tuple[Tuple[float, ...], ...] = tuple(materialized)

    def __repr__(self) -> str:  # pragma: no cover
        return f"Matrix({[list(r) for r in self._values]!r})"

    @property
    def shape(self) -> Tuple[int, int]:
        return self._m, self._n

    def __len__(self) -> int:
        return self._m

    def __iter__(self) -> Iterator[Tuple[float, ...]]:
        return iter(self._values)

    def __getitem__(self, index: int) -> Tuple[float, ...]:
        return self._values[index]

    # Elementwise addition
    def __add__(self, other: "Matrix") -> "Matrix":
        if self.shape != other.shape:
            raise ValueError("Matrices must have the same shape for addition")
        rows = (
            (a + b for a, b in zip(r1, r2))
            for r1, r2 in zip(self._values, other._values)
        )
        return Matrix(rows)

    # Scalar or matrix multiplication
    def __mul__(self, other: "Matrix | float | int") -> "Matrix":
        if isinstance(other, Matrix):
            m, k1 = self.shape
            k2, n = other.shape
            if k1 != k2:
                raise ValueError("Inner dimensions must match for multiplication")
            # Compute product
            prod_rows = []
            # Precompute columns of other for speed
            other_cols = [tuple(other[r][c] for r in range(k2)) for c in range(n)]
            for i in range(m):
                row_i = self[i]
                prod_row = []
                for c in range(n):
                    col_c = other_cols[c]
                    prod_row.append(sum(a * b for a, b in zip(row_i, col_c)))
                prod_rows.append(prod_row)
            return Matrix(prod_rows)
        # scalar multiply
        scalar = float(other)
        return Matrix(((a * scalar for a in r) for r in self._values))

    def __rmul__(self, other: float | int) -> "Matrix":
        return self.__mul__(other)

    # Transpose via property .T
    @property
    def T(self) -> "Matrix":
        m, n = self.shape
        return Matrix(((self._values[i][j] for i in range(m)) for j in range(n)))


__all__ = ["Matrix"]
