from day10 import parse2, knot, to_dense
from generic import get_file, flatten


def bits(s: str):
    data = bin(int(s, base=16))[2:]
    return list(map(bool, map(int, data)))


def row(p: list[int]):
    xs = list(range(256))
    return bits(to_dense(knot(xs, p)))


def part1(s: str) -> int:
    parts = [(parse2(f"{s}-{i}") + [17, 31, 73, 47, 23]) * 64 for i in range(128)]

    return sum(flatten(map(row, parts)))


def part2(s: str) -> int:
    pass


def main():
    s = get_file(14).strip()
    print(f"{part1(s) = }")
    print(f"{part2(s) = }")


if __name__ == "__main__":
    main()
