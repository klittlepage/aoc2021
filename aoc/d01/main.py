from typing import Any, IO, Iterable, Tuple

import aoc.common as common


def parse(input_file: IO, window_length: int) -> Iterable[Tuple[int, ...]]:
    yield from (
        tuple(int(x) for x in window)
        for window in common.sliding_window(input_file, window_length)
    )


def p_1(input_file: IO, debug: bool = False) -> Any:
    return sum(window[1] > window[0] for window in parse(input_file, 2))


def p_2(input_file: IO, debug: bool = False) -> Any:
    windows_sums = (sum(window) for window in parse(input_file, 3))
    return sum(
        window[1] > window[0] for window in common.sliding_window(windows_sums, 2)
    )
