from generic import get_file, lines


def parse_row(s: str):
    pass


def parse(s: str):
    return list(map(parse_row, lines(s)))


def part1(s: str) -> int:
    pass


def part2(s: str) -> int:
    pass


def main():
    s = get_file(0).strip()
    print(f"{part1(s) = }")
    print(f"{part2(s) = }")


if __name__ == "__main__":
    main()
