import operator as op

from collections import Counter
from typing import Any, Callable, IO, List


def parse(input_file: IO) -> List[List[str]]:
    return list(zip(*list(list(x.strip()) for x in input_file.readlines())))


def p_1(input_file: IO, debug: bool = False) -> Any:
    gamma_bits = list()
    epsilon_bits = list()
    for counter in (Counter(x) for x in parse(input_file)):
        gamma_bits.append("0" if counter["0"] > counter["1"] else "1")
        epsilon_bits.append("0" if counter["0"] < counter["1"] else "1")

    return int("".join(gamma_bits), 2) * int("".join(epsilon_bits), 2)


def p_2(input_file: IO, debug: bool = False) -> Any:
    def _solve(
        bits: List[List[str]],
        cmp: Callable[[int, int], bool],
        equal: str,
    ) -> int:
        mask = [True for _ in bits[0]]
        for col in bits:
            counter = Counter(bit for idx, bit in enumerate(col) if mask[idx])
            keep = (
                equal
                if counter["0"] == counter["1"]
                else "0"
                if cmp(counter["0"], counter["1"])
                else "1"
            )
            mask = [mask[idx] and x == keep for idx, x in enumerate(col)]
            if sum(mask) == 1:
                measurement_idx = mask.index(True)
                return int("".join([col[measurement_idx] for col in bits]), 2)
        raise Exception("no measurement found")

    bits = parse(input_file)
    oxygen = _solve(bits, op.gt, "1")
    co2 = _solve(bits, op.lt, "0")
    return oxygen * co2
