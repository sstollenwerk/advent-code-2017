# position = p + nv + tri(n) a
# 2,4,6,
# 1,3,6,

from dataclasses import dataclass
from functools import partial
from generic import argmin, get_file, lines


@dataclass(frozen=True)
class Axis:
    pos: int
    vel: int
    acc: int

    def time(self, t: int):
        v = self.vel + t * self.acc
        p = self.pos + t * self.vel + tri(t) * self.acc

        return type(self)(p, v, self.acc)


Particle = list[Axis]


def manhatten(xs: Particle) -> int:
    return sum(abs(i.pos) for i in xs)


def at_time(t: int, xs: Particle) -> Particle:
    return [i.time(t) for i in xs]


def tri(n):
    return (n * (n + 1)) // 2


def parse_row(s: str) -> Particle:
    parts = s.split("=<")[1:]
    segments = [list(map(int, i.split(">")[0].split(","))) for i in parts]
    return list(map(Axis, *segments))
    print(segments)


def parse(s: str) -> list[Particle]:
    return list(map(parse_row, lines(s)))


def part1(s: str) -> int:
    particles = parse(s)
    time = 1_000_000
    parts = list(map(manhatten, map(partial(at_time, time), particles)))

    return argmin(parts)


def part2(s: str) -> int:
    pass


def main():
    s = get_file(20).strip()
    print(f"{part1(s) = }")
    print(f"{part2(s) = }")


if __name__ == "__main__":
    main()
