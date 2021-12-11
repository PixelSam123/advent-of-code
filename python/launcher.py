from binary_diagnostic import binary_diagnostic
from dive import dive, dive_aimed
from sonar_sweep import sonar_sweep, sonar_sweep_windowed
from os.path import dirname


def print_underlined(text: str, underline_char: str = "-"):
    print(text)
    print(underline_char * len(text))


def exit_launcher(print_exit_msg: bool = True):
    if print_exit_msg:
        print("Exiting...")
    exit()


def help_launcher():
    commands_and_info: list[tuple[str, str]] = [
        ("binarydiagnostic", "Binary Diagnostic"),
        ("dive", "Dive"),
        ("diveaimed", "Dive Aimed"),
        ("sonarsweep", "Sonar Sweep"),
        ("sonarsweepwindowed", "Sonar Sweep Windowed"),
        ("help", "Help"),
        ("exit", "Exit"),
    ]
    longest_command_len = max(len(command) for (command, _) in commands_and_info)

    print(f"{len(commands_and_info)} commands")

    for (command, info) in commands_and_info:
        print(f"{command.ljust(longest_command_len)} - {info}")


def main():
    print_underlined("FADHsquared's Advent of Code Answer Launcher (Python)")
    print("Type 'help' for a list of commands. Exit with 'exit' or Ctrl+C")

    commands = {
        "binarydiagnostic": binary_diagnostic,
        "dive": dive,
        "diveaimed": dive_aimed,
        "sonarsweep": sonar_sweep,
        "sonarsweepwindowed": sonar_sweep_windowed,
        "help": help_launcher,
        "exit": exit_launcher,
    }

    while True:
        try:
            input_command = input("> ")
        except KeyboardInterrupt:
            print("\nExiting...")
            exit_launcher(False)

        try:
            commands[input_command]()
        except KeyError:
            print("Command not found. Type 'help' for a list of commands")


if __name__ == "__main__":
    main()
