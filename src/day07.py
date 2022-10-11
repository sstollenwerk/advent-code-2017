from collections import defaultdict

from generic import get_file


Node = str
Weights = dict[Node, int]
Children = defaultdict[Node, set[Node]]


def parse_row(row: str) -> tuple[Node, int, set[Node]]:
    parts = row.split("->")
    a = parts[0]
    if len(parts) > 1:
        b = parts[1]
    else:
        b = ""
    children = {i.strip() for i in b.split(",")}
    ax = a.replace("(", "").replace(")", "").split()
    node = ax[0]
    weight = int(ax[1])
    return (node, weight, children)


def parse(s: str) -> tuple[Weights, Children]:
    weights = dict()
    children = defaultdict(set)
    for (n, w, c) in map(parse_row, s.strip().split("\n")):
        weights[n] = w
        children[n] = c
    return weights, children


def part1(s: str) -> str:
    _, childs = parse(s)
    roots = set(childs.keys()) - set.union(*childs.values())
    assert len(roots) == 1
    return roots.pop()


def part2(s: str) -> str:
    pass


def main():
    s = get_file(7)
    print(f"{part1(s)=}")
    print(f"{part2(s)=}")


if __name__ == "__main__":
    main()
