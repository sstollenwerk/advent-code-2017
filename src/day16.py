from dataclasses import dataclass
from string import ascii_lowercase
from functools import partial
from collections.abc import Callable

from generic import get_file, T

# Would want to use Rust-style enums
@dataclass(frozen=True)
class Spin:
    n: int


@dataclass(frozen=True)
class Exchange:
    a: int
    b: int


@dataclass(frozen=True)
class Partner:
    a: str
    b: str


Command = Spin | Exchange | Partner


def parse_row(s: str) -> Command:
    c, *rest_ = list(s)
    rest = "".join(rest_)
    parts = rest.split("/")
    match c:
        case "s":
            return Spin(int(rest))
        case "x":
            return Exchange(*map(int, parts))
        case "p":
            return Partner(*parts)

        case _:
            raise ValueError(c)


def parse(s: str) -> list[Command]:
    return list(map(parse_row, s.split(",")))


def interpret(commands: list[Command], xs_: list[str]) -> list[str]:
    xs = xs_.copy()
    for c in commands:
        if isinstance(c, Partner):
            c = Exchange(xs.index(c.a), xs.index(c.b))

        if isinstance(c, Exchange):
            xs[c.a], xs[c.b] = xs[c.b], xs[c.a]
        elif isinstance(c, Spin):
            k = -1 * c.n
            xs = xs[k:] + xs[:k]
    return xs


def part1(s: str) -> str:
    chars = list(ascii_lowercase[:16])
    commands = parse(s)
    return "".join(interpret(commands, chars))


def step(f: Callable[[T], T], k: T, steps: int) -> T:
    orig = k
    for i in range(steps):
        if i and k == orig:
            return step(f, k, (steps - i) % i)
        k = f(k)
    return k


def part2(s: str) -> str:
    chars = list(ascii_lowercase[:16])
    commands = parse(s)

    reordered = interpret(commands, chars)
    b = interpret(commands, reordered)

    re1 = [reordered.index(i) for i in chars]
    re2 = [b.index(i) for i in reordered]
    # re1 != re2 . not currect way of doing this

    f = partial(interpret, commands)

    return "".join(step(f, chars, 1000000000))


def main():
    s = get_file(16).strip()
    print(f"{part1(s) = }")
    print(f"{part2(s) = }")


if __name__ == "__main__":
    main()
