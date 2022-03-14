# Generated from MMADL.g4 by ANTLR 4.9
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\3")
        buf.write("\f\b\1\4\2\t\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\2\2\3\3\3\3")
        buf.write("\2\2\2\13\2\3\3\2\2\2\3\5\3\2\2\2\5\6\7s\2\2\6\7\7y\2")
        buf.write("\2\7\b\7g\2\2\b\t\7t\2\2\t\n\7v\2\2\n\13\7{\2\2\13\4\3")
        buf.write("\2\2\2\3\2\2")
        return buf.getvalue()


class MMADLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NAME = 1

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'qwerty'" ]

    symbolicNames = [ "<INVALID>",
            "NAME" ]

    ruleNames = [ "NAME" ]

    grammarFileName = "MMADL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


