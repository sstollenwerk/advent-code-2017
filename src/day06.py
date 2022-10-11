from collections.abc import Iterator, Callable, Iterable
import enum
from typing import TypeVar
from itertools import islice, tee
from operator import eq

from generic import get_file, uncurry


T = TypeVar("T")


def argmax(xs: list[T]) -> int:
    return max(enumerate(xs), key=lambda x: x[1])[0]


def step(xs_: tuple[int, ...]):
    xs = list(xs_)
    p = argmax(xs)
    assert max(xs) >= 0
    k = xs[p]
    xs[p] = 0
    for i in range(k):
        xs[(p + i + 1) % len(xs)] += 1
    return tuple(xs)


def iterate(k: T, f: Callable[[T], T]) -> Iterator[T]:
    while True:
        yield k
        k = f(k)


def loop_len(xs: Iterator[T]) -> int:
    a,b_ = tee(xs, 2)
    b = islice(b_, 0, None, 2)
    pairs = zip(a,b)
    posses = (i for i,el in enumerate(pairs) if uncurry(eq)(el) )
    next(posses)
    x,y = next(posses), next(posses)
    return y-x


def part1(s: str) -> int:
    banks = tuple(map(int, s.strip().split()))
    data = set()
    for i, el in enumerate(iterate(banks, step)):
        # print(el)
        if el in data:
            return i
        data.add(el)
    assert False

def part2_functional(s: str) -> int:
    banks = tuple(map(int, s.strip().split()))
    return loop_len(iterate(banks, step))

def part2_imperative(s: str) -> int:

    banks = tuple(map(int, s.strip().split()))
    data = dict()
    for i, el in enumerate(iterate(banks, step)):
        # print(el)
        if el in data.keys():
            return i - data[el]
        data[el] = i
    assert False

def part2(s: str) -> int:
    a = part2_functional(s)
    b = part2_imperative(s)
    assert a == b
    return a

    


def main():
    s = get_file(6)
    print(f"{part1(s)=}")
    print(f"{part2(s)=}")


if __name__ == "__main__":
    main()
