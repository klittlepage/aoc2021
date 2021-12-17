import itertools as it

from collections import defaultdict

from typing import Any, Dict, IO, Iterator, List, Optional, Tuple

TSegment = Tuple[List[str], List[str]]
TDigitMap = Dict[str, int]


def parse(input_file: IO) -> Iterator[TSegment]:
    for line in input_file:
        signals, outputs = [x.strip().split(" ") for x in line.split("|")]
        yield (signals, outputs)


def p_1(input_file: IO, debug: bool = False) -> Any:
    def _filter(segments: Iterator[TSegment]) -> Iterator[int]:
        for (_signals, outputs) in segments:
            for output in outputs:
                if len(output) in [2, 3, 4, 7]:
                    yield 1

    return sum(_filter(parse(input_file)))


def print_map(mapping: Dict[str, str]) -> None:
    print(
        ", ".join(
            f"{key} -> {value}"
            for key, value in sorted(mapping.items(), key=lambda x: x[0])
        )
    )


def p_2(input_file: IO, debug: bool = False) -> Any:
    segment_map = {
        "abcefg": 0,
        "cf": 1,
        "acdeg": 2,
        "acdfg": 3,
        "bcdf": 4,
        "abdfg": 5,
        "abdefg": 6,
        "acf": 7,
        "abcdefg": 8,
        "abcdfg": 9,
    }

    segments_by_length = defaultdict(list)
    for key in segment_map.keys():
        segments_by_length[len(key)].append(key)

    def sort_signal(signal: str) -> str:
        return "".join(sorted(signal))

    def map_digit(mapping: Dict[str, str], input: str) -> Optional[int]:
        return segment_map.get("".join(sorted(mapping[x] for x in input)))

    def find_consistent_mapping(signals: List[str]) -> TDigitMap:
        def _helper(
            signals: List[str], current_assignment: Dict[str, str]
        ) -> Optional[Dict[str, str]]:
            if len(current_assignment) == 7:
                return (
                    current_assignment
                    if all(
                        map_digit(current_assignment, signal) is not None
                        for signal in signals
                    )
                    else None
                )

            if not signals:
                return None

            signal = signals[0]
            for digit in segments_by_length[len(signal)]:
                output = set(digit) - set(current_assignment.values())
                input = set(signal) - current_assignment.keys()

                for augmentation in it.permutations(output, len(input)):
                    updated_map = {
                        **current_assignment,
                        **{k: v for k, v in zip(input, augmentation)},
                    }

                    if map_digit(updated_map, signal) is None:
                        continue

                    res = _helper(signals[1:], updated_map)
                    if res is not None:
                        return res

            return None

        mapping = _helper(sorted(signals, key=len), {}) or {}
        return {
            sort_signal(signal): segment_map[
                "".join(sorted(mapping[x] for x in signal))
            ]
            for signal in signals
        }

    def digit_sum(segment: TSegment) -> int:
        signals, outputs = segment
        digit_map = find_consistent_mapping(signals)
        return sum(
            10 ** (len(outputs) - idx - 1) * digit_map[sort_signal(signal)]
            for idx, signal in enumerate(outputs)
        )

    return sum(digit_sum(segment) for segment in parse(input_file))
