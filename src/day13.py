from itertools import count
from collections import defaultdict
from math import lcm
from copy import deepcopy

from generic import get_file


def parse(s: str) -> dict[int, int]:
    res = {}
    for r in s.split("\n"):
        [k, v] = list(map(int, r.split(":")))
        res[k] = v

    return res


def as_danger(d: dict[int, int]) -> dict[int, int]:
    return {k: ((v - 1) * 2) for k, v in d.items()}


def reverses(d: dict[int, int]) -> dict[int, set[int]]:
    res = defaultdict(set)
    for k, v in d.items():
        res[v].add((v - k) % v)
        res[v]
    return dict(res)


def expanded(r: dict[int, set[int]]) -> dict[int, set[int]]:
    reversed = deepcopy(r)
    for k1, v1 in reversed.items():
        for k2, v2 in reversed.items():
            if not k2 % k1:
                for i in range(k2):
                    if i % k1 in v1:
                        v2.add(i)
    return reversed


def valids(layers: dict[int, int]) -> int:
    r1 = expanded(reverses(as_danger(layers)))
    res = {k: sorted(set(range(k)) - v) for k, v in r1.items()}
    groups = sorted(res.items(), key=lambda x: (len(x[1]), x[0]))

    all_allowed = {0}
    seen: list[int] = []
    for (i, posses) in groups:
        tmp = set()
        for a_ in all_allowed:
            for b in posses:
                a = a_
                while a % i != b:
                    a += lcm(*seen)
                tmp.add(a)
        all_allowed = tmp
        seen.append(i)

    return min(all_allowed)


def hit(time: int, depth: int) -> bool:
    return time % ((depth - 1) * 2) == 0


def severity(layers: dict[int, int], time: int) -> int:
    return sum(k * v * hit(k + time, v) for k, v in layers.items())


def gets_hit(layers: dict[int, int], time: int) -> bool:
    return any(hit(k + time, v) for k, v in layers.items())


def all_hit(layers: dict[int, int]) -> int:
    """not way to do it
    figured I could dfind point where it hits all, and then point-1
    """
    timers = as_danger(layers)
    seen: list[int] = []
    time = 0
    for k, v in timers.items():
        print(k, v)
        while (time + k) % v != 0:
            time += lcm(*seen)
        seen.append(v)
    return time


def part1(s: str) -> int:
    layers = parse(s)
    return severity(layers, 0)


def part2(s: str) -> int:
    layers = parse(s)
    return valids(layers)
    ##return next(i for i in count() if gets_hit(layers, i) == 0)


def main():
    s = get_file(13).strip()
    print(f"{part1(s) = }")
    print(f"{part2(s) = }")


if __name__ == "__main__":
    main()
