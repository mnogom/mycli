from argparse import ArgumentParser
from dataclasses import dataclass
from typing import Any
import inspect

from mycli.args_types import ArgProtocol, PositionalArg, NamedArg, FlagArg
from mycli._subparser_action import MyCliSubParserAction


class Command:
    def __init__(
        self,
        name: str,
        description: str | None = None,
        help: str | None = None,
    ) -> None:
        self.__function = None
        self.__args: list[ArgProtocol] = []

        self.__name = name
        self.__description = description
        self.__help = help

        self.__subcommands: dict[str, "Command"] = None

    def register_arg(self, arg: ArgProtocol) -> None:
        if not isinstance(arg, ArgProtocol):
            raise Exception(f"Unknown argument type {arg}")
        self.__args.append(arg)

    def __call__(self, func) -> None:
        self.__function = func

    @staticmethod
    def __register_args(parser: ArgumentParser, args: list[ArgProtocol]) -> ArgumentParser:
        for arg in args:
            if isinstance(arg, PositionalArg):
                parser.add_argument(*arg.dash_names, type=arg.type)
            elif isinstance(arg, NamedArg):
                parser.add_argument(*arg.dash_names, type=arg.type, dest=arg.name)
            elif isinstance(arg, FlagArg):
                parser.add_argument(*arg.dash_names, action=arg.action)
        return parser

    @property
    def _parser(self) -> ArgumentParser:
        parser = ArgumentParser(description=self.__description )

        if self.__function:
            parameters = inspect.signature(self.__function).parameters
            for parameter_name, parameter_options in parameters.items():
                arg_info = parameter_options.annotation.__metadata__[0]

                if isinstance(arg_info, PositionalArg):
                    args = (parameter_name,)
                    kwargs = {
                        "type": parameter_options.annotation.__origin__
                    }

                elif isinstance(arg_info, NamedArg):
                    args = (*arg_info.dash_names,)
                    kwargs = {
                        "dest": parameter_name,
                        "type": parameter_options.annotation.__origin__
                    }
                    if parameter_options.default is not inspect.Parameter.empty:
                        kwargs["default"] = parameter_options.default
                        kwargs["required"] = False
                    else:
                        kwargs["required"] = True

                elif isinstance(arg_info, FlagArg):
                    args = (*arg_info.dash_names,)
                    kwargs = {
                        "dest": parameter_name,
                        "action": arg_info.action
                    }

                parser.add_argument(*args, **kwargs)
            print(parser.parse_args())
        return parser

    def include_subcommand(self, name: str, subcommand: "Command") -> None:
        if self.__subcommands is None:
            self.__subcommands = {}
        self.__subcommands[name] = subcommand

    def parse(self) -> None:  # noqa: C901

        if self.__subcommands:
            subparser = self._parser.add_subparsers(dest="unknown", action=MyCliSubParserAction)
            for name, subcommand in self.__subcommands.items():
                subparser.add_parser_obj(name, subcommand._parser)

        args = self._parser.parse_args()
        if self.__function is not None:
            self.__function(**args.__dict__)
