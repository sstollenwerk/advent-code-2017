from collections import deque

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


def knot(xs: list[int], lengths: list[int]) -> list[int]:
    i = 0
    for skip, L in enumerate(lengths):
        xs = reverse(xs, i, L)
        ## print(i, skip, L)
        ## print(xs)
        ## print()
        i += L + skip
    return xs


def part1(s: str) -> int:
    xs = list(range(256))
    lengths = parse(s)
    r = knot(xs, lengths)

    return r[0] * r[1]


def part2(s: str) -> int:
    pass


def main():
    s = get_file(10).strip()
    print(f"{part1(s)=}")
    print(f"{part2(s)=}")


if __name__ == "__main__":
    main()
