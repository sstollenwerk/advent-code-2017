from math import ceil, sqrt
from collections.abc import Iterator, Callable, Iterable
from itertools import product

from generic import get_file, uncurry


def layer(n: int) -> int:
    return ceil(sqrt(n)) // 2


def top(n: int) -> int:
    return (2 * n + 1) ** 2


def corners(n: int) -> tuple[int, int, int, int]:
    prev = top(n - 1)
    delta = n * 2
    res = []
    for _ in range(4):
        prev += delta
        res.append(prev)
    return tuple(res)


def part1(s: str) -> int:
    n = int(s)
    lay = layer(n)
    d = min(abs(n - a) for a in corners(lay))
    return lay + lay - d


def part_2_oeis(n: int) -> int:
    # created 2008, before this puzzle was released
    import urllib.request

    nums_ = (
        k[1].decode("utf-8")
        for i in urllib.request.urlopen("https://oeis.org/A141481/b141481.txt")
        if len((k := i.split())) > 1
    )
    nums = (int(i) for i in nums_ if i.isnumeric())
    return next(i for i in nums if i > n)


def corner(c: complex) -> bool:
    return abs(c.real) == abs(c.imag)


def indices() -> Iterator[complex]:
    pos = 0 + 0j
    delta = 1 + 0j
    rotation = -1j
    move = True
    seen = set()
    while True:
        seen.add(pos)
        yield pos

        if move:
            pos += delta
            move = False
            delta *= rotation
            seen.add(pos)
            yield pos
        if corner(pos):
            delta *= rotation
            pos += delta
            if pos in seen:
                pos -= delta
                delta /= rotation
                move = True
        else:
            pos += delta


def adj(c: complex) -> list[complex]:
    deltas = range(-1, 2)
    square = map(uncurry(complex), product(deltas, repeat=2))
    return [c + s for s in square]


def part2(s: str) -> int:
    n = int(s)
    entries = {0 + 0j: 1}
    for i in indices():
        if i in entries:
            continue
        res = sum(entries.get(k, 0) for k in adj(i))
        entries[i] = res
        if res > n:
            return res

    assert False
    # mypy equivalent of rust's unreachable!()
    # according to https://stackoverflow.com/questions/72175135/mypy-how-to-mark-line-as-unreachable


def main():
    s = get_file(3)
    print(f"{part1(s)=}")
    print(f"{part2(s)=}")


if __name__ == "__main__":
    main()
