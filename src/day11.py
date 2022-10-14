from dataclasses import dataclass
import functools
from typing import TypeVar

from generic import get_file


"""
with help from 
https://www.redblobgames.com/grids/hexagons
using axial coordinates
"""


Self = TypeVar("Self")


@dataclass(frozen=True)
class Hex:
    q: int
    r: int

    @functools.cached_property
    def neigbours(self) -> dict[str, Self]:
        deltas = [
            Hex(+1, 0),
            Hex(+1, -1),
            Hex(0, -1),
            Hex(-1, 0),
            Hex(-1, +1),
            Hex(0, +1),
        ]
        news = [Hex(self.q + a.q, self.r + a.r) for a in deltas]
        dirs = ["se", "ne", "n", "nw", "sw", "s"]

        return dict(zip(dirs, news))

    ##def neighbour(self, d:str) -> Self:

    def distance(self: Self, other: Self) -> int:
        vec = Hex(self.q - other.q, self.r - other.r)
        res = (abs(vec.q) + abs(vec.q + vec.r) + abs(vec.r)) / 2

        return round(res)


def part1(s: str) -> int:
    start = Hex(0, 0)
    pos = start
    for d in s.split(","):
        pos = pos.neigbours[d]
    return start.distance(pos)


def part2(s: str) -> int:
    pass


def main():
    s = get_file(11).strip()
    print(f"{part1(s)=}")
    print(f"{part2(s)=}")


if __name__ == "__main__":
    main()
