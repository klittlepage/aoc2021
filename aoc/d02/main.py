import re


from typing import Any, IO, Iterable, Tuple


def parse(input_file: IO) -> Iterable[Tuple[int, ...]]:
    regex = re.compile(r"(forward|down|up) (\d+)")
    directions = {"forward": (1, 0), "down": (0, 1), "up": (0, -1)}
    for line in input_file:
        match = regex.match(line)
        if match:
            direction, distance_str = match.groups()
            distance = int(distance_str)
            yield tuple(x * distance for x in directions[direction])


def p_1(input_file: IO, debug: bool = False) -> Any:
    distance = 0
    depth = 0
    for delta_distance, delta_depth in parse(input_file):
        distance += delta_distance
        depth += delta_depth
    return distance * depth


def p_2(input_file: IO, debug: bool = False) -> Any:
    distance = 0
    depth = 0
    aim = 0
    for delta_distance, delta_aim in parse(input_file):
        distance += delta_distance
        aim += delta_aim
        depth += aim * delta_distance
    return distance * depth
