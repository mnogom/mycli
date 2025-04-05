from argparse import ArgumentParser, _SubParsersAction, ArgumentError, _


class MyCliSubParserAction(_SubParsersAction):
    def add_parser_obj(self, name: str, parser: ArgumentParser, **kwargs):
        """
        Note: This is a modified version of the original add_parser method
              for register existing ArgumentParser
        """
        # set prog from the existing prefix
        if kwargs.get('prog') is None:
            kwargs['prog'] = '%s %s' % (self._prog_prefix, name)

        aliases = kwargs.pop('aliases', ())

        if name in self._name_parser_map:
            raise ArgumentError(self, _('conflicting subparser: %s') % name)
        for alias in aliases:
            if alias in self._name_parser_map:
                raise ArgumentError(
                    self, _('conflicting subparser alias: %s') % alias)

        # create a pseudo-action to hold the choice help
        if 'help' in kwargs:
            help = kwargs.pop('help')
            choice_action = self._ChoicesPseudoAction(name, aliases, help)
            self._choices_actions.append(choice_action)

        # create the parser and add it to the map
        self._name_parser_map[name] = parser

        # make parser available under aliases also
        for alias in aliases:
            self._name_parser_map[alias] = parser

        return parser
