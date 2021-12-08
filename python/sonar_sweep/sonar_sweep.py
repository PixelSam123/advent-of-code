from functools import reduce


def sonar_sweep(input_filepath: str):
    with open(input_filepath) as input:
        input_numbers = [int(line.rstrip()) for line in input.readlines()]

        return reduce(
            lambda acc, curr_val: acc + 1 if curr_val[1] > curr_val[0] else acc,
            zip(input_numbers, input_numbers[1:]),
            0,
        )


def main():
    from os.path import dirname

    print(sonar_sweep(f"{dirname(__file__)}/input.txt"))


if __name__ == "__main__":
    main()
