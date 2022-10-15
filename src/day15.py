from itertools import islice
from operator import eq


from generic import get_file, uncurry, ilen


def parse(s: str):
    rows = s.split("\n")
    return [int(r.split()[-1]) for r in rows]


def make_gen(start: int, factor: int, multiple: int):
    n = start
    while True:
        n *= factor
        n %= 2147483647
        if not n % multiple:
            yield n % (2**16)


def part1(s: str) -> int:
    factors = [16807, 48271]
    multiples = [1, 1]
    gets = map(make_gen, parse(s), factors, multiples)
    sequences = [islice(i, 40_000_000) for i in gets]

    return ilen(filter(uncurry(eq), zip(*sequences)))


def part2(s: str) -> int:
    factors = [16807, 48271]
    multiples = [4, 8]
    gets = map(make_gen, parse(s), factors, multiples)
    sequences = [islice(i, 5_000_000) for i in gets]

    return ilen(filter(uncurry(eq), zip(*sequences)))


def main():
    s = get_file(15).strip()
    print(f"{part1(s) = }")
    print(f"{part2(s) = }")


if __name__ == "__main__":
    main()
