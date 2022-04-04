from __future__ import annotations

from argparse import Namespace

import codecs

from ParserParams import ParserParams


class MMADLGrammar:
    def __init__(self) -> None:
        self._delimiter = ':='

        self._open_definition = '<'
        self._close_definition = '>'

        self._open_declaration = '<\\begin>'
        self._close_declaration = '<\\end>'

    def get_delimiter(self) -> str:
        return self._delimiter

    def get_open_definition(self) -> str:
        return self._open_definition

    def get_close_definition(self) -> str:
        return self._close_definition

    def get_open_declaration(self) -> str:
        return self._open_declaration

    def get_close_declaration(self) -> str:
        return self._close_declaration

    def get_delimiter_size(self) -> int:
        return len(self._delimiter)

    def get_open_definition_size(self) -> int:
        return len(self._open_definition)

    def get_close_definition_size(self) -> int:
        return len(self._close_definition)

    def get_open_declaration_size(self) -> int:
        return len(self._open_declaration)

    def get_close_declaration_size(self)-> int:
        return len(self._close_declaration)


class Rule:
    def __init__(self, left: str, right: str) -> None:
        self._left = left
        self._right = right

    def left(self) -> str:
        return self._left

    def right(self) -> str:
        return self._right

    def set_left(self, left: str) -> None:
        self._left = left

    def set_right(self, right: str) -> None:
        self._right = right

# Обработать ошибки
class MMADLPreParser:
    @staticmethod
    def create(params: ParserParams) -> MMADLPreParser:
        return MMADLPreParser(params) if params is not None else None

    def __init__(self, params: ParserParams) -> None:
        self._params = params

        self._MMADL_code: str = None
        self._MMADL_grammar = MMADLGrammar()
        self._grammar_rules = []

    def MMADL_to_temp(self) -> str:
        with codecs.open(self._params._filename, 'r', 'utf_8_sig') as MMADL_source:
            self._MMADL_code = MMADL_source.read()

        next = self._find_next_rule()
        while next:
            next = self._find_next_rule()

        temp_code = self._build_temp_from_rules()
        return temp_code[len(temp_code) - len(temp_code.lstrip(' \t\r\n')):]

    def _find_next_rule(self) -> bool:
        open_definition_ind = self._MMADL_code.find(self._MMADL_grammar.get_open_definition())
        close_definition_ind = self._MMADL_code.find(self._MMADL_grammar.get_close_definition())
        delimiter_ind = self._MMADL_code.find(self._MMADL_grammar.get_delimiter())
        open_declaration_ind = self._MMADL_code.find(self._MMADL_grammar.get_open_declaration())
        close_declaration_ind = self._MMADL_code.find(self._MMADL_grammar.get_close_declaration())

        if open_definition_ind == \
            close_definition_ind == \
            delimiter_ind == \
            open_declaration_ind == \
            close_declaration_ind == -1: return False

        assert 0 <= open_definition_ind \
                    < close_definition_ind \
                    < delimiter_ind \
                    < open_declaration_ind \
                    < close_declaration_ind

        definition = self._MMADL_code[open_definition_ind
        : close_definition_ind + self._MMADL_grammar.get_close_definition_size()]
        delimiter = self._MMADL_code[delimiter_ind : delimiter_ind + self._MMADL_grammar.get_delimiter_size()]
        declaration = self._MMADL_code[open_declaration_ind + self._MMADL_grammar.get_open_declaration_size()
        : close_declaration_ind]

        definition = self._delete_comment(definition)
        declaration = self._delete_comment(declaration)

        declaration = declaration.lstrip(' \t\r\n').rstrip(' \t\r\n')

        self._grammar_rules.append(Rule(definition, declaration))

        self._MMADL_code = self._MMADL_code[close_declaration_ind + self._MMADL_grammar.get_close_declaration_size():]

        return True

    def _delete_comment(self, s: str) -> str:
        strings = s.split('~')

        res = ''

        for i in range(len(strings) // 2 + 1):
            res += strings[2 * i]

        return res

    def _build_temp_from_rules(self) -> str:
        for i in range(len(self._grammar_rules) - 1, -1, -1):
            for j in range(i):
                right = self._grammar_rules[j].right()
                right = right.replace(self._grammar_rules[i].left(), self._grammar_rules[i].right())
                self._grammar_rules[j].set_right(right)

        return self._grammar_rules[0].right()
