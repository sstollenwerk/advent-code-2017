from collections import defaultdict
from functools import cache
from typing import Callable

from generic import get_file, T


Node = str
Weights = dict[Node, int]
Children = dict[Node, set[Node]]


def parse_row(row: str) -> tuple[Node, int, set[Node]]:
    parts = row.split("->")
    a = parts[0]
    if len(parts) > 1:
        children = {i.strip() for i in parts[1].split(",")}
    else:
        children = set()
    ax = a.replace("(", "").replace(")", "").split()
    node = ax[0]
    weight = int(ax[1])
    return (node, weight, children)


def parse(s: str) -> tuple[Weights, Children]:
    weights = dict()
    children = dict()
    for (n, w, c) in map(parse_row, s.strip().split("\n")):
        weights[n] = w
        children[n] = c
    return weights, children


def find_root(childs: dict[T, set[T]]) -> T:
    roots = set(childs.keys()) - set.union(*childs.values())
    assert len(roots) == 1
    return roots.pop()


def part1(s: str) -> str:
    _, childs = parse(s)
    return find_root(childs)


def weight_finder(weights: Weights, children: Children) -> Callable[[Node], int]:
    @cache
    def weight(n: Node) -> int:
        return weights[n] + sum(weight(i) for i in children[n])

    return weight


def part2(s: str) -> int:
    weights, childs = parse(s)

    w = weight_finder(weights, childs)

    node = find_root(childs)
    delta = 0
    while True:
        datas = sorted([(w(n), n) for n in childs[node]])
        if datas[0][0] == datas[-1][0]:
            return weights[node] - delta
        else:
            node = datas[0][1] if datas[0][0] != datas[1][0] else datas[-1][1]
            delta = w(node) - datas[1][0]


def main():
    s = get_file(7)
    print(f"{part1(s)=}")
    print(f"{part2(s)=}")


if __name__ == "__main__":
    main()
