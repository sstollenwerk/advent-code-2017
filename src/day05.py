import itertools

from generic import get_file



def part1(s: str) -> int:
    vals = list(map(int, s.strip().split() ))
    i = 0
    for k in itertools.count():
        if i < 0 or i >= len(vals):
            return k
        d = vals[i]
        vals[i] += 1
        i += d
    


def part2(s: str) -> int:
    vals = list(map(int, s.strip().split() ))
    pass


def main():
    s = get_file(5)
    print(f"{part1(s)=}")
    print(f"{part2(s)=}")


if __name__ == "__main__":
    main()
