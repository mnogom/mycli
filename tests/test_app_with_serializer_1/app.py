#!/usr/bin/env python3

from typing import Annotated
import json

from mycli.parser import Parser
from mycli.args_types import NamedArg, PositionalArg


def main() -> None:
    parser = Parser()

    def dict_from_json(raw_json):
        return json.loads(raw_json)

    positional_arg = PositionalArg(serializer=dict_from_json)
    named_arg = NamedArg(aliases=["-a"], serializer=dict_from_json)

    @parser.command
    def fn(
        obj_1: Annotated[dict, positional_arg],
        obj_2: Annotated[dict, named_arg],
    ):
        obj_1.update(obj_2)
        print(obj_1)

    parser.parse()


if __name__ == "__main__":
    main()
