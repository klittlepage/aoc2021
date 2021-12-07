import aoc.d02

from tests.aoc.test_base import BaseTestCase


class TestAll(BaseTestCase):
    def test_part_one(self) -> None:
        self.run_aoc_part(2, 1648020, aoc.d02.p_1)

    def test_part_two(self) -> None:
        self.run_aoc_part(2, 1759818555, aoc.d02.p_2)
