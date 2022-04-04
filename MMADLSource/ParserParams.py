from __future__ import annotations

from argparse import Namespace
from enum import Enum


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
    def create(args: Namespace) -> ParserParams:
        filename, type, target_platform, style, output =\
             args.input, args.type, args.platform, args.style, args.output

        t = ParserParams.TYPE.ALGORITHM
        p = ParserParams.TARGET_PLATFORM.TEX
        s = ParserParams.STYLE.DOUBLE

        if type == ParserParams._algorithm or type is None:
            t = ParserParams.TYPE.ALGORITHM
        elif type == ParserParams._fragment:
            t = ParserParams.TYPE.FRAGMENT
        elif type == ParserParams._expression:
            t = ParserParams.TYPE.EXPRESSION
        else:
            assert(False)

        if target_platform == ParserParams._tex or target_platform is None:
            p = ParserParams.TARGET_PLATFORM.TEX
        elif target_platform == ParserParams._html:
            p = ParserParams.TARGET_PLATFORM.HTML
        else:
            assert(False)

        if style == ParserParams._double or style is None:
            s = ParserParams.STYLE.DOUBLE
        elif style == ParserParams._python:
            s = ParserParams.STYLE.PYTHON
        else:
            assert(False)

        return ParserParams(filename, output, t, p, s)

    @property
    def filename(self) -> str:
        return self._filename

    @property
    def output(self) -> str:
        return self._output_file

    @property
    def type(self) -> TYPE:
        return self._type

    @property
    def target(self) -> TARGET_PLATFORM:
        return self._target_platform

    @property
    def style(self) -> STYLE:
        return self._style

    def __init__(self, filename: str, output: str, type: TYPE, target_platform: TARGET_PLATFORM, style: STYLE) -> None:
        self._filename = filename
        self._output_file = output
        self._type = type
        self._target_platform = target_platform
        self._style = style
