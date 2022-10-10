from generic import get_file


grid = list[list[int]]


def parse(s: str) -> grid:
    rows = s.strip().split("\n")
    return [list(map(int, r.split())) for r in rows]


def check_part_1(xs: list[int]):
    return max(xs) - min(xs)


def part1(s: str) -> int:
    vals = parse(s)
    return sum(map(check_part_1, vals))


def part2(s: str) -> int:
    pass


def main():
    s = get_file(2)
    print(f"{part1(s)=}")
    print(f"{part2(s)=}")


if __name__ == "__main__":
    main()
