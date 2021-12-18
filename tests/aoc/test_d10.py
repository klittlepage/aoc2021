import aoc.d10

from tests.aoc.test_base import BaseTestCase


class TestAll(BaseTestCase):
    def test_part_one(self) -> None:
        self.run_aoc_part(10, 318081, aoc.d10.p_1)

    def test_part_two(self) -> None:
        self.run_aoc_part(10, 4361305341, aoc.d10.p_2)
