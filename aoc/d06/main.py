from collections import deque
from typing import Any, Deque, IO, List

TSwarm = List[int]


def parse(input_file: IO) -> TSwarm:
    return [int(x) for x in input_file.readline().split(",")]


def evolve(swarm: TSwarm, days: int) -> int:
    due_dates: Deque[int] = deque(0 for _ in range(9))
    for fish in swarm:
        due_dates[fish] += 1

    for _ in range(days):
        babies = due_dates[0]
        due_dates.rotate(-1)
        due_dates[6] += babies
        due_dates[8] = babies

    return sum(due_dates)


def p_1(input_file: IO, debug: bool = False) -> Any:
    return evolve(parse(input_file), 80)


def p_2(input_file: IO, debug: bool = False) -> Any:
    return evolve(parse(input_file), 256)
