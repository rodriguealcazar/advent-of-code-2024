import argparse

def main(reports: str):
    with open(reports, "r") as f:
        safe = 0
        for levels in f:
            levels = levels.strip().split(" ")
            if is_safe(levels):
                safe += 1
        print(safe)

def is_safe(levels: list[int]) -> bool:
    prev = None
    for i in range(1, len(levels)):
        diff = int(levels[i]) - int(levels[i - 1])
        if not prev:
            prev = diff
        if not (1 <= abs(diff) <= 3) or diff * prev < 0:
            return False
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i")
    args = parser.parse_args()

    main(args.input)
