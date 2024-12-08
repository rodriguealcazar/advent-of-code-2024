import argparse
from collections import Counter


def main(lists: str, part: int):
    with open(lists, "r") as f:
        list_1 = []
        list_2 = []
        for pair in f:
            if pair := pair.strip():
                a, b = pair.split("  ")
                list_1.append(int(a))
                list_2.append(int(b))

    match part:
        case 1:
            total_distance(list_1, list_2)
        case 2:
            total_similarity(list_1, list_2)


def total_distance(list_1: list[int], list_2: list[int]):
    distance = 0
    for a, b in zip(sorted(list_1), sorted(list_2)):
        distance += abs(a - b)
    print(distance)


def total_similarity(list_1: list[int], list_2: list[int]):
    counts = Counter(list_2)
    similarity = 0
    for loc in list_1:
        similarity += loc * counts[loc]

    print(similarity)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i")
    parser.add_argument("--part", "-p", type=int, default=1)
    args = parser.parse_args()

    main(args.input, args.part)
