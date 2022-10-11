from collections.abc import Iterator, Callable, Iterable
from typing import TypeVar
from itertools import islice, tee

from generic import get_file


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
    pass


def part1(s: str) -> int:
    banks = tuple(map(int, s.strip().split()))
    data = set()
    for i, el in enumerate(iterate(banks, step)):
        # print(el)
        if el in data:
            return i
        data.add(el)
    assert False


def part2(s: str) -> int:
    pass


def main():
    s = get_file(6)
    print(f"{part1(s)=}")
    print(f"{part2(s)=}")


if __name__ == "__main__":
    main()
