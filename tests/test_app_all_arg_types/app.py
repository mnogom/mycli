#!/usr/bin/env python3

from typing import Annotated

from mycli.parser import Parser
from mycli.args_types import PositionalArg, NamedArg, FlagArg


def main() -> None:
    parser = Parser(description="Send a message")

    message_arg = PositionalArg(description="Message to send")
    address_arg = PositionalArg(description="Address to send to")
    from_arg = NamedArg(["--from", "-f"], description="From address")
    loud_arg = FlagArg(
        ["--loud", "-l"], action=lambda: True, description="Be loud"
    )

    @parser.command
    def fn(
        msg: Annotated[str, message_arg],
        address: Annotated[str, address_arg],
        from_: Annotated[str, from_arg] = "Konstantin",
        loud: Annotated[bool, loud_arg] = False,
    ):
        if loud:
            msg = msg.upper()
        output = f"Send to {address}: {msg}"
        if from_:
            output = f"{output} from {from_}"
        print(output)

    parser.parse()


if __name__ == "__main__":
    main()
