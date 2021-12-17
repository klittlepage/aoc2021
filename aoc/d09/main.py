import heapq
import operator as op
import functools as ft

from collections import defaultdict
from typing import Any, IO, Dict, Iterator, List, Set, Tuple

TMatrix = List[List[int]]
TDelta = Tuple[int, int]
TCoord = Tuple[int, int]


def parse(input_file: IO) -> TMatrix:
    return [list(int(x) for x in line.strip()) for line in input_file]


def adjacencies(
    matrix: TMatrix, row_idx: int, col_idx: int, deltas: List[TDelta]
) -> Iterator[TCoord]:
    m = len(matrix)
    for (dy, dx) in deltas:
        if 0 <= row_idx + dy < m and 0 <= col_idx + dx < len(matrix[row_idx]):
            yield (row_idx + dy, col_idx + dx)


def find_low_points(matrix: TMatrix) -> Iterator[Tuple[int, int]]:
    deltas = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for row_idx, row in enumerate(matrix):
        for col_idx, value in enumerate(row):
            if all(
                value < matrix[ay][ax]
                for ay, ax in adjacencies(matrix, row_idx, col_idx, deltas)
            ):
                yield (row_idx, col_idx)


def p_1(input_file: IO, debug: bool = False) -> Any:

    matrix = parse(input_file)
    return sum(
        matrix[row_idx][col_idx] + 1 for row_idx, col_idx in find_low_points(matrix)
    )


def p_2(input_file: IO, debug: bool = False) -> Any:
    deltas = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def closest_low_point(
        matrix: TMatrix, row_idx: int, col_idx: int, low_points: Set[Tuple[int, int]]
    ) -> TCoord:
        frontier = [(0, (row_idx, col_idx))]
        while frontier:
            dist, (row_idx, col_idx) = heapq.heappop(frontier)
            if (row_idx, col_idx) in low_points:
                return (row_idx, col_idx)

            for ay, ax in adjacencies(matrix, row_idx, col_idx, deltas):
                if matrix[ay][ax] < matrix[row_idx][col_idx]:
                    heapq.heappush(frontier, (dist + 1, (ay, ax)))

        raise Exception("no lowpoint found")

    matrix = parse(input_file)
    low_points = set(find_low_points(matrix))
    basins: Dict[TCoord, int] = defaultdict(int)

    for row_idx, row in enumerate(matrix):
        for col_idx, value in enumerate(row):
            if value == 9:
                continue

            low_point = closest_low_point(matrix, row_idx, col_idx, low_points)
            basins[low_point] += 1

    return ft.reduce(op.mul, sorted(basins.values(), reverse=True)[:3])
