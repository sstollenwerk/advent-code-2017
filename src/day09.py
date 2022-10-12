import re
from ast import literal_eval


from generic import get_file


def clean(s: str) -> str:
    vals = list(s)
    in_garbage = False
    for i, c in enumerate(vals):
        if c == "<":
            in_garbage = True
        if in_garbage and c == "!":
            vals[i] = None
            vals[i + 1] = None
        if c == ">":
            in_garbage = False
    return "".join(filter(bool, vals))


def clean_reg(s: str) -> str:
    p = re.compile("!.")
    r = str(p.sub("", s))
    assert r == clean(s)
    return r
    # apparently all '!' are contained in garbage.
    # Wasn't sure if that was the case


def remove_garbage(s: str) -> str:
    while "<" in s:
        a = s.find("<")
        b = s.find(">")
        s = s[:a] + s[b + 1 :]
    return s


def score(xs, current=1):
    return current + sum(score(i, current + 1) for i in xs)


def part1(s: str) -> int:
    data = remove_garbage(clean_reg(s))
    groups = literal_eval(data.replace("{", "[").replace("}", "]").replace("[,", "["))
    print(groups)

    return score(groups)


def part2(s: str) -> int:
    pass


def main():
    s = get_file(9).strip()
    print(f"{part1(s)=}")
    print(f"{part2(s)=}")


if __name__ == "__main__":
    main()
