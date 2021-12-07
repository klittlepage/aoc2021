import aoc.d01

from tests.aoc.test_base import BaseTestCase


class TestAll(BaseTestCase):
    def test_part_one(self) -> None:
        self.run_aoc_part(1, 1752, aoc.d01.p_1)

    def test_part_two(self) -> None:
        self.run_aoc_part(1, 1781, aoc.d01.p_2)
