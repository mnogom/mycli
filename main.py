from typing import Annotated
from pathlib import Path

from mycli.args_types import PositionalArg, NamedArg, FlagArg
from mycli.parser import Parser


def app_1():
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
        from_: Annotated[str, from_arg] = "localhost",
        loud: Annotated[bool, loud_arg] = False,
    ):
        if loud:
            msg = msg.upper()
        output = f"Send to {address}: {msg}"
        if from_:
            output = f"{output} from {from_}"
        print(output)

    parser.parse()


def app_2():
    parser = Parser()

    @parser.command
    def fn(
        dir: Annotated[Path, NamedArg(["--dir", "-d"])],
        file: Annotated[Path, PositionalArg()],
        force: Annotated[
            bool, FlagArg(["--force", "-f"], action=lambda: True)
        ] = False,
    ):
        if force:
            print(force)
        print(dir.absolute() / file.name)

    parser.parse()


def app_3():
    parser = Parser()

    @parser.command
    def fn(
        foo: Annotated[None, FlagArg(["--foo", "-f"], action=lambda: print("bar"))],
    ): pass

    parser.parse()


if __name__ == "__main__":
    app_3()


# send --address 127.0.0.1 "Hello"
# myapp send --address 127.0.0.1 "Hello"
# myapp chat send --address 127.0.0.1 "Hello"
