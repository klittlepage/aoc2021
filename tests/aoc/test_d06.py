import aoc.d06

from tests.aoc.test_base import BaseTestCase


class TestAll(BaseTestCase):
    def test_part_one(self) -> None:
        self.run_aoc_part(6, 385391, aoc.d06.p_1)

    def test_part_two(self) -> None:
        self.run_aoc_part(6, 1728611055389, aoc.d06.p_2)
