from argparse import ArgumentParser




class App:
    def __init__(self, *args):
        pass

    def register_commands(self, *commands):
        self.__commands.extend(commands)
    
    def run(self):
        parser = ArgumentParser()
        sub_parser = parser.add_subparsers(dest="asd")
        for command in self.__commands:
            sub_parser = parser.add_subparsers(command.dest)
            sub_parser
    







if __name__ == "__main__":
    main_parser = ArgumentParser(prog="app", description="Utility to manage chat and history")
    sub_parser = main_parser.add_subparsers(dest="subparser_1", action=MyCliSubParserAction)

    parser_history = sub_parser.add_parser(
        name="history",
        help="Show chat history",
        description="Utility to show chat history"
    )
    parser_history.add_argument("--from", help="From date", default="01.01.2000")
    parser_history.add_argument("--to", help="To date", default="01.01.2020")

    # ======================================================
    # parser_chat = sub_parser.add_parser(
    #     name="chat",
    #     help="Chat with person",
    #     description="Utility to chat with person"
    # )
    # ======================================================
    parser_chat = ArgumentParser(description="Utility to chat with person")
    parser_chat.add_argument("--from", help="From person", default="me")
    parser_chat.add_argument("--to", help="To person", default="you")
    sub_parser.add_parser_obj(name="history", parser=parser_chat, help="Chat with person")


    args = main_parser.parse_args()
    print(args.__dict__)
