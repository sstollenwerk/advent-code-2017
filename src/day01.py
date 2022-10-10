from itertools import pairwise
from operator import eq
from collections.abc import Iterator, Callable, Iterable
from typing import TypeVar
from functools import wraps

from generic import get_file

T = TypeVar("T")
V = TypeVar("V")


def uncurry(f: Callable[..., V]) -> Callable[[Iterable[T]], V]:
    """
    inspired by Haskell's uncurry
    https://hackage.haskell.org/package/base-4.17.0.0/docs/Prelude.html#v:uncurry
    """
    ##@wraps
    # Inclusion of wraps causes crash
    # AttributeError: 'tuple' object has no attribute '__module__'
    def inner(xs: Iterable[T]) -> V:
        return f(*xs)

    return inner


def ilen(xs: Iterator) -> int:
    return sum(map(lambda x: 1, xs))


def part1(s: str) -> int:
    vals = list(s.strip())
    vals.append(vals[0])
    return ilen(filter(uncurry(eq), pairwise(vals)))


def part2(s: str) -> int:
    pass


def main():
    s = get_file(1)
    print(f"{part1(s)=}")
    print(f"{part2(s)=}")


if __name__ == "__main__":
    main()
