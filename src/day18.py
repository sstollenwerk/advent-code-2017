from collections import defaultdict, deque
from dataclasses import dataclass, asdict
from copy import deepcopy


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


def interpret_part1(registers: defaultdict[str, int], commands: list[Inst]) -> int:
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
    return interpret_part1(registers, instructions)


def interpret_part2(
    registers: defaultdict[str, int], commands: list[Inst], vals: deque[int]
):
    def get_val(s: str | int) -> int:
        if isinstance(s, int):
            return s
        return registers[s]

    yield
    i = 0
    while 0 <= i < len(commands):
        c = commands[i]
        d = type(c)(**map_values(get_val, asdict(c)))
        i += 1
        ##match type(d):
        if isinstance(d, Snd):
            r = d.x
            yield r
        elif isinstance(d, Set):
            registers[c.x] = d.y

        elif isinstance(d, Add):
            registers[c.x] += d.y

        elif isinstance(d, Mul):
            registers[c.x] *= d.y

        elif isinstance(d, Mod):
            registers[c.x] %= d.y

        elif isinstance(d, Rcv):
            if not vals:
                i -= 1
                yield

            else:
                registers[c.x] = vals.pop()

        elif isinstance(d, Jgz):
            if d.x > 0:
                i += d.y - 1

        else:
            assert False


def part2(s: str) -> int:
    instructions = parse(s)
    registers = defaultdict(int)

    insts = [[], []]

    datas = [deque([]), deque([])]

    comps = []
    for i in range(2):
        r = deepcopy(registers)
        r["p"] = i
        inst = deepcopy(instructions)
        k = i
        comp = interpret_part2(r, inst, datas[i])
        next(comp)

        comps.append(comp)

    while True:
        seen = False
        for i in range(2):
            d = next(comps[i])
            if d is not None:
                insts[1 - i].append(d)
                datas[1 - i].appendleft(d)
                seen = True
        if not seen:
            break
    return len(insts[0])


def main():
    s = get_file(18).strip()
    print(f"{part1(s) = }")
    print(f"{part2(s) = }")


if __name__ == "__main__":
    main()
