from collections import defaultdict


from generic import get_file, lines

UP = -1j
LEFT = -1j
RIGHT = 1j

Positions = set[complex]


def parse(s: str) -> tuple[complex, Positions]:
    k, r = divmod(len(lines(s)[0]), 2)
    assert r == 1
    centre = complex(k, k)

    nodes = {
        complex(x, y)
        for y, r in enumerate(lines(s))
        for x, c in enumerate(r)
        if c == "#"
    }

    return centre, nodes


def display(xs: Positions):
    x1 = round(min(i.real for i in xs))
    y1 = round(min(i.imag for i in xs))
    top_left = complex(x1, y1)

    x2 = round(max(i.real for i in xs))
    y2 = round(max(i.imag for i in xs))
    bottom_right = complex(x2, y2)
    posses = [" ", chr(9608)]
    res = []
    for y in range(y1, y2 + 1):
        row = ""
        for x in range(x1, x2 + 1):
            row += posses[complex(x, y) in xs]
        res.append(row)
    print("\n".join(res))


def steps(start: complex, nodes: Positions, steps: int) -> int:
    deltas = [RIGHT, LEFT]
    direction = UP

    position = start

    times = 0
    for _ in range(steps):
        k = position not in nodes
        times += k
        nodes ^= {position}
        direction *= deltas[k]
        position += direction
    ##display(nodes)
    return times


def part1(s: str) -> int:
    centre, nodes = parse(s)

    return steps(centre, nodes, 10000)


def steps2(start: complex, nodes: defaultdict[complex, int], steps: int) -> int:
    deltas = [LEFT, 1, RIGHT, -1]
    direction = UP

    position = start

    times = 0
    for _ in range(steps):
        k = nodes[position]
        times += nodes[position] == 1
        nodes[position] += 1
        nodes[position] %= 4
        direction *= deltas[k]
        position += direction
    return times


def part2(s: str) -> int:
    clean, weakened, infected, flagged = range(4)

    centre, nodes_ = parse(s)
    nodes = defaultdict(int, {k: 2 for k in nodes_})

    return steps2(centre, nodes, 10000000)


def main():
    s = get_file(22).strip()
    print(f"{part1(s) = }")
    print(f"{part2(s) = }")


if __name__ == "__main__":
    main()
