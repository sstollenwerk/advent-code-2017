from math import ceil, sqrt

from generic import get_file


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


def part2(s: str) -> int:
    pass


def main():
    s = get_file(3)
    print(f"{part1(s)=}")
    print(f"{part2(s)=}")


if __name__ == "__main__":
    main()
