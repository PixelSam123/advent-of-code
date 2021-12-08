def dive(input_filepath: str):
    with open(input_filepath) as input:
        dist_x = 0
        depth = 0

        def add_dist_x(x):
            nonlocal dist_x
            dist_x += x

        def add_depth(y):
            nonlocal depth
            depth += y

        def subtract_depth(y):
            nonlocal depth
            depth -= y

        move_mapping = {"forward": add_dist_x, "down": add_depth, "up": subtract_depth}

        for direction, distance in (
            line.rstrip().split(" ") for line in input.readlines()
        ):
            move_mapping[direction](int(distance))

        return dist_x * depth


def main():
    from os.path import dirname

    print(dive(f"{dirname(__file__)}/input.txt"))


if __name__ == "__main__":
    main()
