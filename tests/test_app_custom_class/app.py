#!/usr/bin/env python3

from typing import Annotated
from pathlib import Path

from mycli.command import Parser
from mycli.args_types import PositionalArg


def main() -> None:
    parser = Parser()

    @parser.command
    def fn(
        dir: Annotated[Path, PositionalArg()],
        filename: Annotated[str, PositionalArg()],
    ):
        print(f"Creating '{dir / filename}'")

    parser.parse()


if __name__ == "__main__":
    main()
