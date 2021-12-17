import aoc.d09

from tests.aoc.test_base import BaseTestCase


class TestAll(BaseTestCase):
    def test_part_one(self) -> None:
        self.run_aoc_part(9, 541, aoc.d09.p_1)

    def test_part_two(self) -> None:
        self.run_aoc_part(9, 847504, aoc.d09.p_2)
