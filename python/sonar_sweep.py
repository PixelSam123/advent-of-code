from functools import reduce


def sonar_sweep(input_filepath: str):
    with open(input_filepath) as input:
        input_numbers = tuple(int(line.rstrip()) for line in input.readlines())

        return reduce(
            lambda acc, curr_val: acc + 1 if curr_val[1] > curr_val[0] else acc,
            zip(input_numbers, input_numbers[1:]),
            0,
        )


def sonar_sweep_windowed(input_filepath: str, window_size: int = 1):
    assert window_size >= 1, "Sliding window size must be at least 1"

    with open(input_filepath) as input:
        input_numbers = tuple(int(line.rstrip()) for line in input.readlines())
        input_groups = [
            sum(window) / window_size
            for window in zip(
                *(input_numbers[start_idx:] for start_idx in range(window_size))
            )
        ]

        return reduce(
            lambda acc, curr_val: acc + 1 if curr_val[1] > curr_val[0] else acc,
            zip(input_groups, input_groups[1:]),
            0,
        )


def sonar_sweep_cli():
    from os.path import dirname

    print(sonar_sweep(f"{dirname(__file__)}/../input/sonar_sweep.txt"))


def sonar_sweep_windowed_cli():
    from os.path import dirname

    print(sonar_sweep_windowed(f"{dirname(__file__)}/../input/sonar_sweep.txt", 3))


def main():
    sonar_sweep_cli()
    sonar_sweep_windowed_cli()


if __name__ == "__main__":
    main()
