from collections import deque
from functools import reduce
from operator import xor

from generic import get_file


def reverse(xs: list[int], start: int, amt: int) -> list[int]:
    start %= len(xs)
    r = deque(xs)
    r.rotate(start * -1)
    rx = list(r)
    r = deque((rx[:amt])[::-1] + rx[amt:])
    r.rotate(start)
    return list(r)


def parse(s: str) -> list[int]:
    return list(map(int, s.split(",")))


def parse2(s: str) -> list[int]:
    return list(map(ord, s))


def knot(xs: list[int], lengths: list[int]) -> list[int]:
    i = 0
    for skip, L in enumerate(lengths):
        xs = reverse(xs, i, L)
        i += L + skip
    return xs


def part1(s: str) -> int:
    xs = list(range(256))
    lengths = parse(s)
    r = knot(xs, lengths)

    return r[0] * r[1]


def chunks(xs, n):
    if not xs:
        return []
    return [xs[:n]] + chunks(xs[n:], n)


def sing_block(xs: list[int]) -> str:
    assert len(xs) > 0
    val = reduce(xor, xs)
    return "{:0>2x}".format(val)


def to_dense(xs: list[int]) -> str:
    parts = chunks(xs, 16)
    return "".join(map(sing_block, parts))


def part2(s: str) -> str:
    xs = list(range(256))
    lengths = (parse2(s) + [17, 31, 73, 47, 23]) * 64
    sparse = knot(xs, lengths)
    return to_dense(sparse)


def main():
    s = get_file(10).strip()
    print(f"{part1(s)=}")
    print(f"{part2(s)=}")


if __name__ == "__main__":
    main()
