from generic import get_file, ilen

Passphrase = list[str]


def valid(p: Passphrase) -> bool:
    return len(p) == len(set(p))


def valid2(p: Passphrase) -> bool:
    parts = ["".join(sorted(i)) for i in p]
    return valid(parts)


def parse(s: str) -> list[Passphrase]:
    return [r.split() for r in s.strip().split("\n")]


def part1(s: str) -> int:
    vals = parse(s)
    return ilen(filter(valid, vals))


def part2(s: str) -> int:
    vals = parse(s)
    return ilen(filter(valid2, vals))


def main():
    s = get_file(4)
    print(f"{part1(s)=}")
    print(f"{part2(s)=}")


if __name__ == "__main__":
    main()
