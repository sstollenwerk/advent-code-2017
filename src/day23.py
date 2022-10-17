from collections import Counter, defaultdict, deque
from dataclasses import dataclass, asdict
from copy import deepcopy


from generic import get_file, lines, map_values

Reg = str
Val = Reg | int


@dataclass(frozen=True)
class Set:
    x: Reg
    y: Val


@dataclass(frozen=True)
class Sub:
    x: Reg
    y: Val


@dataclass(frozen=True)
class Mul:
    x: Reg
    y: Val


@dataclass(frozen=True)
class Jnz:
    x: Val
    y: Val


Inst = Set | Sub | Mul | Jnz


def poss_num(s: str) -> str | int:
    try:
        return int(s)
    except ValueError:
        return s


def parse_row(s: str) -> Inst:
    cmd, *xs = s.split()
    class_ = globals()[cmd.capitalize()]
    xs = map(poss_num, xs)
    return class_(*xs)


def parse(s: str) -> list[Inst]:
    return list(map(parse_row, lines(s)))


def interpret_part1(registers: defaultdict[str, int], commands: list[Inst]):
    def get_val(s: str | int) -> int:
        if isinstance(s, int):
            return s
        return registers[s]

    seen = Counter()

    i = 0
    while 0 <= i < len(commands):
        c = commands[i]
        d = type(c)(**map_values(get_val, asdict(c)))
        i += 1
        seen[type(c)] += 1
        ##match type(d):
        if isinstance(d, Set):
            registers[c.x] = d.y

        elif isinstance(d, Sub):
            registers[c.x] -= d.y

        elif isinstance(d, Mul):
            registers[c.x] *= d.y

        elif isinstance(d, Jnz):
            if d.x != 0:
                i += d.y - 1

        else:
            assert False
    return seen


def part1(s: str) -> int:
    instructions = parse(s)
    registers = defaultdict(int)
    return interpret_part1(registers, instructions)[Mul]


def part2(s: str) -> int:
    pass


def main():
    s = get_file(23).strip()
    print(f"{part1(s) = }")
    print(f"{part2(s) = }")


if __name__ == "__main__":
    main()
