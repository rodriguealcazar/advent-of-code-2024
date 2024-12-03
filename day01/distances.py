import argparse


def main(input):
    with open(input, "r") as f:
        list_1 = []
        list_2 = []
        for pair in f:
            if pair := pair.strip():
                a, b = pair.split("  ")
                list_1.append(int(a))
                list_2.append(int(b))

    distance = 0
    for a, b in zip(sorted(list_1), sorted(list_2)):
        distance += abs(a - b)

    print(distance)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i")
    args = parser.parse_args()

    main(args.input)
