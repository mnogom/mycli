#!/usr/bin/env python3

from typing import Annotated
from argparse import ArgumentParser


from mycli.command import Command
from mycli.args_types import PositionalArg, NamedArg, FlagArg
from mycli.actions import Actions
from mycli._subparser_action import MyCliSubParserAction



def main() -> None:

    # main_parser = ArgumentParser(description="main_parser_description")
    # main_parser.add_argument("-H", "--headers", dest="headers", default="", action="store", help="argument_headers_help")

    # sub_parser = main_parser.add_subparsers(dest="verb", action=MyCliSubParserAction, help="get")

    # get_parser = ArgumentParser(description="Get http")
    # get_parser.add_argument("--follow-redirects", help="Follow redirects", default=False, action="store_true")
    # get_parser.add_argument("--host", help="Host", default="localhost")
    # get_parser.add_argument("--port", dest="port", help="Port", default=80)
    # get_parser.add_argument(dest="uri", help="URI")
    # sub_parser.add_parser_obj("get", get_parser)

    # sub_parser_get = get_parser.add_subparsers(dest="options", action=MyCliSubParserAction, help="proxy")

    # proxy_parser = ArgumentParser(description="Proxy http")
    # proxy_parser.add_argument("--proxy-host", help="Host", default="localhost")
    # proxy_parser.add_argument("--proxy-port", help="Port", default=80)
    # sub_parser_get.add_parser_obj("proxy", proxy_parser)

    # vpn_parser = ArgumentParser(description="VPN http")
    # vpn_parser.add_argument("--vpn-host", help="Host", default="localhost")
    # vpn_parser.add_argument("--vpn-port", help="Port", default=80)
    # sub_parser_get.add_parser_obj("vpn", vpn_parser)

    # args = main_parser.parse_args()
    # print(args.__dict__)
    
    command = Command(name="main_parser_description")
    header_arg = NamedArg(dash_names=["-H", "--headers"])
    command.register_arg(header_arg)

    command_get = Command(name="get")
    uri_arg = PositionalArg()
    follow_redirects_arg = FlagArg(dash_names=["--follow-redirects", "-f"], action=Actions.STORE_TRUE)
    host = NamedArg(dash_names=["--host"])
    port = NamedArg(dash_names=["--port"])

    @command_get
    def get(
        uri: Annotated[str, uri_arg],
        headers: Annotated[str, header_arg],
        host: Annotated[str, host] = "localhost",
        follow_redirects: Annotated[bool, follow_redirects_arg] = False,
        port: Annotated[int, port] = 80,
    ):
        print(f"{uri = }")
        print(f"{headers = }")
        print(f"{follow_redirects = }")
        print(f"{host = }")
        print(f"{port = }")

    # command_get.parse()

    command.include_subcommand(name="get", subcommand=command_get)
    command.parse()


    # app = App(main_command=command)
    # app.run()



if __name__ == "__main__":
    main()



# ./main.py --headers "{foo: bar}" get --follow-redirect --host http://google.com


# ┌────┐ ┌───────────────────┐ ┌─────┐ ┌────┐ ┌────────────┐ ┌────────────────┐ ┌──────────────────┐
#  chat   --user "Konstantin"   --log   send   "My message"   --to "Alexander"   --insert-signature
# └┬───┘ └┬──────────────────┘ └┬────┘ └┬───┘ └┬───────────┘ └┬───────────────┘ └┬─────────────────┘
#  │      │                     │       │      │              │                  └── subcommand's flag
#  │      │                     │       │      │              └── subcommand's named argument with value
#  │      │                     │       │      └── subcommand's positional argument
#  │      │                     │       └── subcommand name
#  │      │                     └── command's flag
#  │      └── command's named argument with value
#  └── command name