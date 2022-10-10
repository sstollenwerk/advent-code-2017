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


def part2(s: str) -> int:
    return part_2_oeis(int(s))


def main():
    s = get_file(3)
    print(f"{part1(s)=}")
    print(f"{part2(s)=}")


if __name__ == "__main__":
    main()
