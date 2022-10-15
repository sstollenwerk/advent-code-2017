from collections import defaultdict
from dataclasses import dataclass, replace, asdict

from generic import get_file, lines, map_values

Reg = str
Val = Reg | int


@dataclass(frozen=True)
class Snd:
    x: Val


@dataclass(frozen=True)
class Set:
    x: Reg
    y: Val


@dataclass(frozen=True)
class Add:
    x: Reg
    y: Val


@dataclass(frozen=True)
class Mul:
    x: Reg
    y: Val


@dataclass(frozen=True)
class Mod:
    x: Reg
    y: Val


@dataclass(frozen=True)
class Rcv:
    x: Val


@dataclass(frozen=True)
class Jgz:
    x: Val
    y: Val


Inst = Snd | Set | Add | Mul | Mod | Rcv | Jgz


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


def interpret(registers: defaultdict[str, int], commands: list[Inst]) -> int:
    seen = None

    def get_val(s: str | int) -> int:
        if isinstance(s, int):
            return s
        return registers[s]

    i = 0
    while 0 <= i < len(commands):
        c = commands[i]
        d = type(c)(**map_values(get_val, asdict(c)))
        i += 1
        ##match type(d):
        if isinstance(d, Snd):
            r = d.x
            seen = r
            ##yield r
        elif isinstance(d, Set):
            registers[c.x] = d.y

        elif isinstance(d, Add):
            registers[c.x] += d.y

        elif isinstance(d, Mul):
            registers[c.x] *= d.y

        elif isinstance(d, Mod):
            registers[c.x] %= d.y

        elif isinstance(d, Rcv):
            if c.x != 0:
                return seen

        elif isinstance(d, Jgz):
            if d.x > 0:
                i += d.y - 1

        else:
            print(registers)
            print(c, d)
            assert False


def parse(s: str) -> list[Inst]:
    return list(map(parse_row, lines(s)))


def part1(s: str) -> int:
    instructions = parse(s)
    registers = defaultdict(int)
    return interpret(registers, instructions)


def part2(s: str) -> int:
    pass


def main():
    s = get_file(18).strip()
    print(f"{part1(s) = }")
    print(f"{part2(s) = }")


if __name__ == "__main__":
    main()
