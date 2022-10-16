from calendar import c
from re import A
from generic import get_file, lines

Position = complex
Places = dict[Position, str]


def parse(s: str) -> tuple[Position, Places]:
    nodes = {
        complex(x, y): c
        for y, r in enumerate(lines(s))
        for x, c in enumerate(r)
        if c != " "
    }

    letters = {k: v for k, v in nodes.items() if v.isalpha()}
    starts = [k for k in nodes.keys() if k.imag == 0]
    assert len(starts) == 1
    start = starts[0]
    return start, nodes


def adj(p: Position) -> list[Position]:
    return {p + 1, p - 1, p + 1j, p - 1j}


def part1(s: str) -> int:
    start, nodes = parse(s)
    nexts = nodes.keys() & adj(start)
    assert len(nexts) == 1
    direction = nexts.pop() - start

    prev, current = None, start

    seen = []

    while True:
        assert abs(direction) == 1
        if nodes[current].isalpha():
            seen.append(nodes[current])
        d = current + direction
        if d not in nodes.keys():
            nexts = (nodes.keys() & adj(current)) - {prev}
            if not nexts:
                break
            assert len(nexts) == 1
            d = nexts.pop()
            direction = d - current
        prev, current = current, d

    return "".join(seen)


def part2(s: str) -> int:
    pass


def main():
    s = get_file(19)
    print(f"{part1(s) = }")
    print(f"{part2(s) = }")


if __name__ == "__main__":
    main()
