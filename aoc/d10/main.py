import functools as ft
import statistics

from collections import defaultdict

from typing import Any, IO, Dict, Iterator, List, Union


def parse(input_file: IO) -> Iterator[List[str]]:
    yield from (list(line.strip()) for line in input_file.readlines())


COMPLETIONS = {"(": ")", "[": "]", "{": "}", "<": ">"}


def validate(entry: List[str]) -> Union[str, List[str]]:
    stack = []
    for token in entry:
        if token in ["(", "[", "{", "<"]:
            stack.append(token)
        if token in [")", "]", "}", ">"]:
            if not stack or COMPLETIONS[stack.pop()] != token:
                return token

    return stack


def p_1(input_file: IO, debug: bool = False) -> Any:
    error_counts: Dict[str, int] = defaultdict(int)

    for line in parse(input_file):
        res = validate(line)
        if isinstance(res, str):
            error_counts[res] += 1

    scores = {")": 3, "]": 57, "}": 1197, ">": 25137}

    return sum((scores[token] * count for token, count in error_counts.items()))


def p_2(input_file: IO, debug: bool = False) -> Any:
    def helper() -> Iterator[int]:
        scores = {")": 1, "]": 2, "}": 3, ">": 4}
        for line in parse(input_file):
            res = validate(line)
            if isinstance(res, list):
                completion = (COMPLETIONS[token] for token in reversed(res))
                yield ft.reduce(
                    lambda acc, token: 5 * acc + scores[token], completion, 0
                )

    return statistics.median(list(helper()))
