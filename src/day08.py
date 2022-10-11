from operator import eq, lt, le, ne, ge, gt
from collections import defaultdict
from typing import Callable, Iterator
from functools import reduce
from itertools import accumulate

from generic import get_file, T

Register = str
Registers = defaultdict[Register, int]

Instruction = tuple[Register, int, Register, Callable[[int, int], bool], int]


def parse_row(row: str) -> Instruction:
    a, b = row.split("if")
    ax = a.strip().split()
    reg1 = ax[0]
    m = {"inc": 1, "dec": -1}[ax[1]]
    delta = int(ax[2]) * m

    bx = b.strip().split()
    reg2 = bx[0]
    to_comp = int(bx[2])
    comps = {"<": lt, ">": gt, ">=": ge, "<=": le, "==": eq, "!=": ne}
    comp = comps[bx[1]]

    return (reg1, delta, reg2, comp, to_comp)


def parse(s: str) -> list[Instruction]:
    return list(map(parse_row, s.strip().split("\n")))


def interpret_step(r: Registers, command: Instruction) -> Registers:
    registers = r.copy()
    (reg1, delta, reg2, comp, to_comp) = command
    if comp(registers[reg2], to_comp):
        registers[reg1] += delta
    return registers


def part1(s: str) -> int:
    commands = parse(s)
    res = reduce(interpret_step, commands, defaultdict(int))
    return max(res.values())
    # might actually be 0


def part2(s: str) -> int:
    commands = parse(s)
    posses = (
        max(i.values(), default=0)
        for i in accumulate(commands, interpret_step, initial=defaultdict(int))
    )
    return max(posses)


def main():
    s = get_file(8)
    print(f"{part1(s)=}")
    print(f"{part2(s)=}")


if __name__ == "__main__":
    main()
