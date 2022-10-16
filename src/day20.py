# position = p + nv + tri(n) a
# 2,4,6,
# 1,3,6,

from collections import defaultdict
from dataclasses import dataclass
from functools import partial
from itertools import combinations, starmap
from math import sqrt

from generic import argmin, get_file, lines, flatten


@dataclass(frozen=True)
class Axis:
    pos: int
    vel: int
    acc: int

    def time(self, t: int):
        v = self.vel + t * self.acc
        p = self.pos + t * self.vel + tri(t) * self.acc

        return type(self)(p, v, self.acc)

    def collide(self, other) -> bool:
        return self.pos == other.pos


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


def parse(s: str) -> list[Particle]:
    return list(map(parse_row, lines(s)))


def part1(s: str) -> int:
    particles = parse(s)
    time = 1_000_000
    parts = list(map(manhatten, map(partial(at_time, time), particles)))

    return argmin(parts)


def time_collide(t: int, q: Axis, r: Axis) -> bool:
    a = q.time(t)
    b = r.time(t)
    return a.collide(b)


def axis_collide(q: Axis, r: Axis) -> set[int]:
    # find x where (ax^2 + bx +c) == (dx^2 + ex + f)
    # ax^2 + bx + c = acc/2 = a, acc/2 + vel = b, pos = c
    # quadratic : (-b +- sqrt(b^2 - 4ac) ) /2a

    a = (q.acc - r.acc) / 2
    b = (q.acc - r.acc) / 2 + (q.vel - r.vel)
    c = q.pos - r.pos

    centre = b**2 - 4 * a * c
    if centre < 0:
        return set()

    if a == 0:
        if b == 0:
            posses = set()
        else:
            posses = {round(-1 * c / b)}
    else:

        p = sqrt(centre)
        posses = set(map(round, [(-b + p) / (2 * a), (-b - p) / (2 * a)]))
    # don't care about collisions at fractional seconds
    return {t for t in posses if t >= 0 and time_collide(t, q, r)}


def collide(q: Particle, r: Particle) -> set[int]:
    # find x both xs collide. see if y and z match.
    parts = list(zip(q, r))
    posses = axis_collide(*parts[0])
    return {t for t in posses if all(time_collide(t, *p) for p in parts)}


def delete_collisions(pars: list[Particle]) -> list[Particle]:
    places = defaultdict(list)
    for p in pars:
        pos = tuple([i.pos for i in p])
        places[pos].append(p)

    return list(flatten(v for v in places.values() if len(v) == 1))


def col_times(pars: list[Particle]) -> set[int]:
    return set.union(set(), *starmap(collide, combinations(pars, 2)))


def part2(s: str) -> int:
    particles = parse(s)
    collisions = sorted(col_times(particles))
    while collisions:
        t, *xs = collisions
        particles = delete_collisions([at_time(t, p) for p in particles])
        collisions = [i - t for i in xs]
    return len(particles)


def main():
    s = get_file(20).strip()
    print(f"{part1(s) = }")
    print(f"{part2(s) = }")


if __name__ == "__main__":
    main()
