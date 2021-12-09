import re

from typing import Any, IO, Iterable, List, Tuple

TCoord = Tuple[int, int]
TCoordPair = Tuple[TCoord, TCoord]


def parse(input_file: IO) -> Iterable[TCoordPair]:
    regex = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")
    for line in input_file:
        match = regex.match(line)
        if match is not None:
            x_1, y_1, x_2, y_2 = [int(x) for x in match.groups()]
            p_1 = (x_1, y_1)
            p_2 = (x_2, y_2)
            yield (p_1, p_2) if p_1 <= p_2 else (p_2, p_1)


def display_grid(grid: List[List[int]]) -> None:
    for row in grid:
        print("".join(str(x) if x > 0 else "." for x in row))


def bounding_box(coord_pairs: List[TCoordPair]) -> TCoordPair:
    min_x = min(min(x[0][0] for x in coord_pairs), min(x[1][0] for x in coord_pairs))
    min_y = min(min(x[0][1] for x in coord_pairs), min(x[1][1] for x in coord_pairs))
    max_x = max(max(x[0][0] for x in coord_pairs), max(x[1][0] for x in coord_pairs))
    max_y = max(max(x[0][1] for x in coord_pairs), max(x[1][1] for x in coord_pairs))
    return ((min_x, min_y), (max_x, max_y))


def delta_x(coord_pair: TCoordPair) -> int:
    return coord_pair[1][0] - coord_pair[0][0]


def delta_y(coord_pair: TCoordPair) -> int:
    return coord_pair[1][1] - coord_pair[0][1]


def step_direction(delta: int) -> int:
    if delta == 0:
        return 0
    if delta > 0:
        return 1
    return -1


def plot_lines(bounds: TCoordPair, coord_pairs: List[TCoordPair]) -> List[List[int]]:
    x_offset, y_offset = bounds[0]
    x_distance = delta_x(bounds) + 1
    y_distance = delta_y(bounds) + 1
    grid = [[0 for _ in range(x_distance)] for _ in range(y_distance)]

    for coord_pair in coord_pairs:
        dx = step_direction(delta_x(coord_pair))
        dy = step_direction(delta_y(coord_pair))
        x_idx = coord_pair[0][0] - x_offset
        y_idx = coord_pair[0][1] - y_offset
        while True:
            grid[y_idx][x_idx] += 1
            x_idx += dx
            y_idx += dy
            if (
                x_idx == coord_pair[1][0] - x_offset
                and y_idx == coord_pair[1][1] - y_offset
            ):
                grid[y_idx][x_idx] += 1
                break

    return grid


def hazard_sum(grid: List[List[int]]) -> int:
    return sum(1 for row in grid for x in row if x > 1)


def p_1(input_file: IO, debug: bool = False) -> Any:
    coord_pairs = list(parse(input_file))
    bounds = bounding_box(coord_pairs)
    horizontal_or_vertical = [
        x for x in coord_pairs if x[0][0] == x[1][0] or x[0][1] == x[1][1]
    ]
    return hazard_sum(plot_lines(bounds, horizontal_or_vertical))


def p_2(input_file: IO, debug: bool = False) -> Any:
    coord_pairs = list(parse(input_file))
    bounds = bounding_box(coord_pairs)
    return hazard_sum(plot_lines(bounds, coord_pairs))
