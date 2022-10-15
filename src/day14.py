from multiprocessing import Pool

from day10 import parse2, knot, to_dense
from generic import get_file, flatten


def bits(s: str):
    data = flatten(bin(int(c, base=16))[2:].zfill(4) for c in s)
    return list(map(bool, map(int, data)))


def row(p: list[int]):
    xs = list(range(256))
    return bits(to_dense(knot(xs, p)))


def make_grid(s: str) -> set[complex]:
    parts = [(parse2(f"{s}-{i}") + [17, 31, 73, 47, 23]) * 64 for i in range(128)]
    p = Pool(None)
    b = list(p.imap(row, parts))

    return {complex(x, y) for y, r in enumerate(b) for x, c in enumerate(r) if c}


def part1(s: str) -> int:

    return len(make_grid(s))


def adj(p: complex) -> list[complex]:
    return [p + c for c in [1, -1, 1j, -1j]]


def groups(g_: set[complex]) -> list[set[complex]]:
    res: list[set[complex]] = []
    g = g_.copy()
    while g:
        group = {min(g, key=abs)}
        while (next_ := g & (set(flatten(map(adj, group))) | group)) != group:
            group = next_
        res.append(group)
        g -= group
    return res


def part2(s: str) -> int:
    return len(groups(make_grid(s)))


def main():
    s = get_file(14).strip()
    print(f"{part1(s) = }")
    print(f"{part2(s) = }")


if __name__ == "__main__":
    main()
