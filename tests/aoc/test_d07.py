import aoc.d07

from tests.aoc.test_base import BaseTestCase


class TestAll(BaseTestCase):
    def test_part_one(self) -> None:
        self.run_aoc_part(7, 353800, aoc.d07.p_1)

    def test_part_two(self) -> None:
        self.run_aoc_part(7, 98119739, aoc.d07.p_2)
