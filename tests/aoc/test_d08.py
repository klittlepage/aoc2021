import aoc.d08

from tests.aoc.test_base import BaseTestCase


class TestAll(BaseTestCase):
    def test_part_one(self) -> None:
        self.run_aoc_part(8, 548, aoc.d08.p_1)

    def test_part_two(self) -> None:
        self.run_aoc_part(8, 1074888, aoc.d08.p_2)
