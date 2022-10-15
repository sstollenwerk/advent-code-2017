from collections.abc import Iterator, Callable, Iterable
from typing import TypeVar
from functools import wraps


T = TypeVar("T")
V = TypeVar("V")


def get_file(n: int) -> str:
    dir = "../input/" + str(n).zfill(2) + ".txt"
    with open(dir, "r") as f:
        return f.read()


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


def flatten(c):
    return (a for b in c for a in b)


def lines(s: str) -> list[str]:
    return s.split("\n")
