#!/usr/bin/env python3

from typing import Annotated

from mycli.command import Parser
from mycli.args_types import FlagArg


def main() -> None:
    parser = Parser()

    @parser.command
    def fn(
        foo: Annotated[
            None, FlagArg(["--foo", "-f"], action=lambda: print("bar"))
        ],
    ):
        pass

    parser.parse()


if __name__ == "__main__":
    main()
