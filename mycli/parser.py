import sys
from typing import get_type_hints

from mycli.args_types import PositionalArg, NamedArg, FlagArg


class Parser:
    def __init__(self, description=None) -> None:
        self.__command = None
        self.__positional_args: list[tuple[str, type, PositionalArg]] = []
        self.__named_args: list[tuple[str, type, NamedArg]] = []
        self.__flag_args: list[tuple[str, type, FlagArg]] = []
        self.__description = description

        self.__help_arg = FlagArg(["--help", "-h"], action=self.__show_help)
        self.__flag_args.append(("", None.__class__, self.__help_arg))

    def command(self, func) -> None:
        self.__command = func
        type_hints = get_type_hints(func, include_extras=True)
        for var, hint in type_hints.items():
            arg_type = hint.__origin__
            arg_notation = hint.__metadata__[0]
            if isinstance(arg_notation, PositionalArg):
                self.__positional_args.append((var, arg_type, arg_notation))
            elif isinstance(arg_notation, NamedArg):
                self.__named_args.append((var, arg_type, arg_notation))
            elif isinstance(arg_notation, FlagArg):
                self.__flag_args.append((var, arg_type, arg_notation))
            else:
                raise Exception(f"Unknown argument type {arg_notation}")

    def __show_help(self) -> None:
        # TODO: kf: Fix typing for arg_notation
        arg_notation: PositionalArg | NamedArg | FlagArg

        help_text = f"{self.__description}\n\n"
        for arg_name, _, arg_notation in self.__positional_args:
            help_text += f"  {arg_name}: {arg_notation.description}\n"  # noqa: E501
        for _, _, arg_notation in self.__named_args:
            help_text += f"  {', '.join(arg_notation.aliases)}: {arg_notation.description}\n"  # noqa: E501
        for _, _, arg_notation in self.__flag_args:
            help_text += f"  {', '.join(arg_notation.aliases)}: {arg_notation.description}\n"  # noqa: E501
        print(help_text)

    @staticmethod
    def __is_positional_arg(cli_arg: str) -> bool:
        return not cli_arg.startswith("-")

    def parse(self) -> None:  # noqa: C901
        if not self.__command:
            raise Exception("No command specified")

        cli_argv = sys.argv[1:]
        func_args = {}

        positional_index = 0

        while len(cli_argv) != 0:
            cli_arg = cli_argv.pop(0)

            if cli_arg in self.__help_arg.aliases:
                self.__help_arg.action()
                return

            if self.__is_positional_arg(cli_arg):
                arg_name, arg_type, arg_notation = self.__positional_args[
                    positional_index
                ]
                if arg_notation.serializer:
                    func_args[arg_name] = arg_notation.serializer(cli_arg)
                else:
                    func_args[arg_name] = arg_type(cli_arg)
                positional_index += 1
                continue

            for arg_name, arg_type, arg_notation in self.__named_args:
                if cli_arg in arg_notation.aliases:
                    if arg_notation.serializer:
                        func_args[arg_name] = arg_notation.serializer(
                            cli_argv.pop(0)
                        )
                    else:
                        func_args[arg_name] = arg_type(cli_argv.pop(0))
                    break

            for arg_name, arg_type, arg_notation in self.__flag_args:
                if cli_arg in arg_notation.aliases:
                    if arg_type is None.__class__:
                        arg_notation.action()
                        func_args[arg_name] = None
                    else:
                        func_args[arg_name] = arg_type(arg_notation.action())
                    break

        self.__command(**func_args)
