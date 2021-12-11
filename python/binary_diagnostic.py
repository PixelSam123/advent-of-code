from collections import Counter


def binary_diagnostic(input_filepath: str):
    with open(input_filepath) as input:
        lines = tuple(line.rstrip() for line in input.readlines())
        transformed_lines = zip(*(tuple(line) for line in lines))

        gamma_rate_list = []
        epilson_rate_list = []

        for transformed_line in transformed_lines:
            bit_and_frequencies = Counter(transformed_line).most_common()

            (most_common_bit, _) = bit_and_frequencies[0]
            (least_common_bit, _) = bit_and_frequencies[-1]

            gamma_rate_list.append(most_common_bit)
            epilson_rate_list.append(least_common_bit)

        return int("".join(gamma_rate_list), 2) * int("".join(epilson_rate_list), 2)


def binary_diagnostic_cli():
    from os.path import dirname

    print(binary_diagnostic(f"{dirname(__file__)}/../input/binary_diagnostic.txt"))


def main():
    binary_diagnostic_cli()


if __name__ == "__main__":
    main()
