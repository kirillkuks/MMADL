from __future__ import annotations

from argparse import Namespace
from enum import Enum

import codecs


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
class MMADLParser:
    class ParserParams:
        class TYPE(Enum):
            ALGORITHM = 0,
            FRAGMENT = 1,
            EXPRESSION = 2

        class TARGET_PLATFORM(Enum):
            TEX = 0,
            HTML = 1

        class STYLE(Enum):
            DOUBLE = 0,
            PYTHON = 1

        _algorithm: str = 'algorithm'
        _fragment: str = 'fragment'
        _expression: str = 'expression'

        _tex = 'tex'
        _html = 'html'

        _double = 'double'
        _python = 'python'

        @staticmethod
        def create(filename: str, type: str, target_platform: str, style: str) -> MMADLParser.ParserParams:
            t = MMADLParser.ParserParams.TYPE.ALGORITHM
            p = MMADLParser.ParserParams.TARGET_PLATFORM.TEX
            s = MMADLParser.ParserParams.STYLE.DOUBLE

            if type == MMADLParser.ParserParams._algorithm or type is None:
                t = MMADLParser.ParserParams.TYPE.ALGORITHM
            elif type == MMADLParser.ParserParams._fragment:
                t = MMADLParser.ParserParams.TYPE.FRAGMENT
            elif type == MMADLParser.ParserParams._expression:
                t = MMADLParser.ParserParams.TYPE.EXPRESSION
            else:
                assert(False)

            if target_platform == MMADLParser.ParserParams._tex or target_platform is None:
                p = MMADLParser.ParserParams.TARGET_PLATFORM.TEX
            elif target_platform == MMADLParser.ParserParams._html:
                p = MMADLParser.ParserParams.TARGET_PLATFORM.HTML
            else:
                assert(False)

            if style == MMADLParser.ParserParams._double or style is None:
                s = MMADLParser.ParserParams.STYLE.DOUBLE
            elif style == MMADLParser.ParserParams._python:
                s = MMADLParser.ParserParams.STYLE.PYTHON
            else:
                assert(False)

            return MMADLParser.ParserParams(filename, t, p, s)

        def __init__(self, filename: str, type: TYPE, target_platform: TARGET_PLATFORM, style: STYLE) -> None:
            self._filename = filename
            self._type = type
            self._target_platform = target_platform
            self._style = style

    @staticmethod
    def create(args: Namespace) -> MMADLParser:
        params = MMADLParser.ParserParams.create(args.input, args.type, args.platform, args.style)

        return MMADLParser(params) if params is not None else None

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
        print(temp_code)
        return temp_code

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

        self._grammar_rules.append(Rule(definition, declaration))

        self._MMADL_code = self._MMADL_code[close_declaration_ind + self._MMADL_grammar.get_close_declaration_size():]

        return True

    def _build_temp_from_rules(self) -> str:
        for i in range(len(self._grammar_rules) - 1, -1, -1):
            for j in range(i):
                right = self._grammar_rules[j].right()
                right = right.replace(self._grammar_rules[i].left(), self._grammar_rules[i].right())
                self._grammar_rules[j].set_right(right)

        return self._grammar_rules[0].right()
