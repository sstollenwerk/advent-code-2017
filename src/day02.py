from itertools import product
from operator import ne

from generic import get_file, uncurry


grid = list[list[int]]


def parse(s: str) -> grid:
    rows = s.strip().split("\n")
    return [list(map(int, r.split())) for r in rows]


def check_part_1(xs: list[int]) -> int:
    return max(xs) - min(xs)


def check_part_2(xs: list[int]) -> int:
    # n = 16, O(n**2) is good enough
    pairs = map(uncurry(divmod), filter(uncurry(ne), product(xs, repeat=2)))
    return next(x[0] for x in pairs if x[1] == 0)


def part1(s: str) -> int:
    vals = parse(s)
    return sum(map(check_part_1, vals))


def part2(s: str) -> int:
    vals = parse(s)
    return sum(map(check_part_2, vals))


def main():
    s = get_file(2)
    print(f"{part1(s)=}")
    print(f"{part2(s)=}")


if __name__ == "__main__":
    main()
