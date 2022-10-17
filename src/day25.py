from collections import defaultdict
from pprint import pprint
from generic import get_file, lines

State = str
Value = bool

Delta = int

Steps = int

Read = tuple[State, Value]
Write = tuple[Value, Delta, State]

Transition = dict[Read, Write]

Turing = tuple[Steps, State, Transition]


def parse_section(s: str) -> Transition:
    a, _, b = s.partition(":")

    state = a.split()[-1]
    b = b.replace(":", "")

    parts = b.split("If")[1:]

    res = {}

    for p in parts:
        data_ = [i.split()[-1] for i in lines(p.strip())]

        trans = {"0": False, "1": True, "left": -1, "right": 1}
        data = [trans.get(r, r) for r in data_]
        assert len(data) == 4
        k, *xs = data
        res[(state, k)] = tuple(xs)

    return res


def parse(s: str) -> Turing:
    s = s.replace(".", "")
    a, *xs = s.split("\n\n")

    q, r = lines(a)
    state = q.split()[-1]
    steps = int(r.split()[5])

    t: Transition = dict()
    for p in map(parse_section, xs):
        t |= p

    return (steps, state, t)


def turing(t: Turing) -> int:
    steps, state, trans = t
    tape = defaultdict(bool)

    i = 0
    for _ in range(steps):
        value, delta, state_ = trans[(state, tape[i])]
        tape[i] = value
        i += delta
        state = state_
    return sum(tape.values())


def part1(s: str) -> int:
    return turing(parse(s))


def part2(s: str) -> int:
    pass


def main():
    s = get_file(25).strip()
    print(f"{part1(s) = }")
    print(f"{part2(s) = }")


if __name__ == "__main__":
    main()
