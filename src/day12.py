from generic import get_file


Node = str
Connections = dict[Node, set[Node]]


def parse(s: str) -> Connections:
    res = {}
    for r in s.split("\n"):
        k, v_ = r.split(" <-> ")
        v = set(i.strip() for i in v_.split(","))
        res[k] = v
    return res


def connects(conn: Connections, n: Node) -> set[Node]:
    res = {n}

    currents = {n}

    while currents:
        part = set.union(*(conn[c] for c in currents))
        currents = part - res
        res |= part
    return res


def part1(s: str) -> int:
    cons = parse(s)
    res = connects(cons, "0")
    return len(res)


def part2(s: str) -> int:
    cons = parse(s)
    to_see = set(cons.keys())
    groups = []
    while to_see:
        a = min(to_see)
        vals = connects(cons, a)
        assert a in vals
        groups.append(vals)
        to_see -= vals
    return len(groups)


def main():
    s = get_file(12).strip()
    print(f"{part1(s) = }")
    print(f"{part2(s) = }")


if __name__ == "__main__":
    main()
