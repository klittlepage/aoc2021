import aoc.d05

from tests.aoc.test_base import BaseTestCase


class TestAll(BaseTestCase):
    def test_part_one(self) -> None:
        self.run_aoc_part(5, 5690, aoc.d05.p_1)

    def test_part_two(self) -> None:
        self.run_aoc_part(5, 17741, aoc.d05.p_2)
