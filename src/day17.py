from generic import get_file


def part1(s: str) -> int:
    n = int(s)
    vals = [0]
    for i in range(1, 2018):
        p = (vals.index(i - 1) + n) % len(vals) + 1
        vals.insert(p, i)
    return vals[vals.index(2017) + 1]


def part2(s: str) -> int:
    pass


def main():
    s = get_file(17).strip()
    print(f"{part1(s) = }")
    print(f"{part2(s) = }")


if __name__ == "__main__":
    main()
