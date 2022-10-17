from functools import cache

from generic import get_file, lines

Component = tuple[int, int]


def parse_row(s: str) -> Component:
    return tuple(sorted(map(int, s.split("/"))))


def parse(s: str) -> list[Component]:
    return list(map(parse_row, lines(s)))


def score(xs: list[Component]) -> int:
    return sum(map(sum, xs))


@cache
def bridge(start: int, components: frozenset[Component]) -> list[Component]:
    comps = [i for i in components if start in i]

    posses: list[list[Component]] = [[]]
    for c in comps:
        next_ = c[1] if c[0] == start else c[0]
        res = bridge(next_, components - {c})
        posses.append([c] + res)
    return max(posses, key=score)


def part1(s: str) -> int:
    posses = parse(s)
    assert len(posses) == len(set(posses))
    print(posses)

    return score(bridge(0, frozenset(posses)))


def part2(s: str) -> int:
    pass


def main():
    s = get_file(24).strip()
    print(f"{part1(s) = }")
    print(f"{part2(s) = }")


if __name__ == "__main__":
    main()
