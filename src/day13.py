from generic import get_file


def parse(s: str) -> dict[int, int]:
    res = {}
    for r in s.split("\n"):
        [k, v] = list(map(int, r.split(":")))
        res[k] = v

    return res


def hit(time: int, depth: int) -> bool:
    return time % ((depth - 1) * 2) == 0


def severity(layers: dict[int, int], time: int):
    return sum(k * v * hit(k + time, v) for k, v in layers.items())


def part1(s: str) -> int:
    layers = parse(s)
    return severity(layers, 0)


def part2(s: str) -> int:
    pass


def main():
    s = get_file(13).strip()
    print(f"{part1(s) = }")
    print(f"{part2(s) = }")


if __name__ == "__main__":
    main()
