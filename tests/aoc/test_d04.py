import aoc.d04

from tests.aoc.test_base import BaseTestCase


class TestAll(BaseTestCase):
    def test_part_one(self) -> None:
        self.run_aoc_part(4, 16674, aoc.d04.p_1)

    def test_part_two(self) -> None:
        self.run_aoc_part(4, 7075, aoc.d04.p_2)
