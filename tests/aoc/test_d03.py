import aoc.d03

from tests.aoc.test_base import BaseTestCase


class TestAll(BaseTestCase):
    def test_part_one(self) -> None:
        self.run_aoc_part(3, 3320834, aoc.d03.p_1)

    def test_part_two(self) -> None:
        self.run_aoc_part(3, 4481199, aoc.d03.p_2)
