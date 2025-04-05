#!/usr/bin/env python3

from typing import Annotated

from mycli.command import Parser
from mycli.args_types import PositionalArg


class Calculator:
    def __init__(self, *values: int) -> None:
        self.__values = values

    @classmethod
    def from_string(cls, s: str) -> "Calculator":
        return cls(*[int(v) for v in s.split(",")])

    def sum(self) -> int:
        return sum(self.__values)


def main() -> None:
    parser = Parser()

    obj_arg = PositionalArg(serializer=Calculator.from_string)

    @parser.command
    def fn(obj: Annotated[Calculator, obj_arg]):
        assert isinstance(obj, Calculator)
        print(obj.sum())

    parser.parse()


if __name__ == "__main__":
    main()
