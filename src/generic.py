def get_file(n: int) -> str:
    dir = "../input/" + str(n).zfill(2) + ".txt"
    with open(dir, "r") as f:
        return f.read()
