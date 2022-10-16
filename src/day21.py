import numpy as np

# vstack, dstack

# 3x3 becomes 4x4 becomes 6x6 becomes 9x9 becomes

from generic import get_file, lines


Grid = tuple[tuple[bool, ...], ...]
Rule = dict[Grid, Grid]


def from_array(g: np.array) -> Grid:
    g2 = g.tolist()
    return tuple([tuple(r) for r in g2])


def to_grid(s: str) -> Grid:
    return tuple([tuple([c == "#" for c in r]) for r in s.split("/")])


def parse_row(s: str) -> Rule:
    start, end = [to_grid(r) for r in s.split(" => ")]

    res: Rule = {}

    s = np.array(start)
    for a in [s, np.flipud(s), np.fliplr(s)]:
        k = a
        for _ in range(4):
            res[from_array(k)] = end
            k = np.rot90(k)

    return res


def parse(s: str) -> Rule:
    res: Rule = {}
    for r in map(parse_row, lines(s)):
        res |= r
    return res
    # apparently dict.union isn't a thing, only | and |=


def subgrids(xs: np.array, size: int):
    assert len(xs) % size == 0
    res = []
    for i in range(0, len(xs), size):
        part = []
        for j in range(0, len(xs), size):
            p = xs[i : i + size, j : j + size]
            part.append(p)
        res.append(part)
    return res


def step(d: Rule, g: Grid) -> Grid:
    if not len(g) % 2:
        size = 2
    else:
        size = 3
    parts = subgrids(np.array(g), size)
    rows = [np.hstack([d[from_array(c)] for c in row]) for row in parts]
    return np.vstack(rows)


def part1(s: str) -> int:
    base = """
.#.
..#
###"""
    start = to_grid(base.strip().replace("\n", "/"))

    print(start)

    maps = parse(s)
    grid = start
    for i in range(5):
        grid = step(maps, grid)
        ##print(grid)

    return sum(grid.flatten())


def part2(s: str) -> int:
    pass


def main():
    s = get_file(21).strip()
    print(f"{part1(s) = }")
    print(f"{part2(s) = }")


if __name__ == "__main__":
    main()
