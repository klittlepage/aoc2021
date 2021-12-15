import statistics

from typing import Any, IO, List

TPosition = List[int]


def parse(input_file: IO) -> TPosition:
    return [int(x) for x in input_file.readline().split(",")]


def p_1(input_file: IO, debug: bool = False) -> Any:
    # The median minimizes the sum of absolute deviations for a set of real
    # numbers: https://math.stackexchange.com/questions/113270/
    # the-median-minimizes-the-sum-of-absolute-deviations-the-ell-1-norm

    positions = parse(input_file)
    optimal_position = int(statistics.median(positions))
    return sum(abs(x - optimal_position) for x in positions)


def p_2(input_file: IO, debug: bool = False) -> Any:
    # Assume that we have two coordinates x_1, x_2, and WLOG x_1 < x_2. The cost
    # to move from x_1 to x_2 is \sum_{i=1}^N i = N*(N+1)/2 where N = x_2-x_1 =
    # (x_2-x_1)^2 / 2 + O(N). The mean is a minimizer for this quantity (OLS),
    # so checking a unit integer radius around the mean is sufficient

    def fuel_cost(x_1: int, x_2: int) -> int:
        n = abs(x_2 - x_1)
        return n * (n + 1) // 2

    positions = parse(input_file)
    mean = int(sum(positions) / len(positions))
    return min(
        sum(fuel_cost(position, minimizer) for position in positions)
        for minimizer in (mean - 1, mean, mean + 1)
    )
