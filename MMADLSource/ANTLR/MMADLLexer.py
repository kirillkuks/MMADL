# Generated from MMADL.g4 by ANTLR 4.9
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("]\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\5\2\37\n\2\3\2\3\2\3\3\3\3\7\3%\n\3\f\3\16\3")
        buf.write("(\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3")
        buf.write("\16\2\2\17\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\3\2\4\4\2C\\c|\5\2\62;C\\c|\2^\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\3\36\3\2\2\2\5\"\3\2\2\2\7)\3\2\2\2\t/\3\2\2\2\13\66")
        buf.write("\3\2\2\2\r=\3\2\2\2\17C\3\2\2\2\21L\3\2\2\2\23R\3\2\2")
        buf.write("\2\25T\3\2\2\2\27V\3\2\2\2\31X\3\2\2\2\33Z\3\2\2\2\35")
        buf.write("\37\7\17\2\2\36\35\3\2\2\2\36\37\3\2\2\2\37 \3\2\2\2 ")
        buf.write("!\7\f\2\2!\4\3\2\2\2\"&\t\2\2\2#%\t\3\2\2$#\3\2\2\2%(")
        buf.write("\3\2\2\2&$\3\2\2\2&\'\3\2\2\2\'\6\3\2\2\2(&\3\2\2\2)*")
        buf.write("\7K\2\2*+\7p\2\2+,\7r\2\2,-\7w\2\2-.\7v\2\2.\b\3\2\2\2")
        buf.write("/\60\7Q\2\2\60\61\7w\2\2\61\62\7v\2\2\62\63\7r\2\2\63")
        buf.write("\64\7w\2\2\64\65\7v\2\2\65\n\3\2\2\2\66\67\7t\2\2\678")
        buf.write("\7g\2\289\7v\2\29:\7w\2\2:;\7t\2\2;<\7p\2\2<\f\3\2\2\2")
        buf.write("=>\7{\2\2>?\7k\2\2?@\7g\2\2@A\7n\2\2AB\7f\2\2B\16\3\2")
        buf.write("\2\2CD\7e\2\2DE\7q\2\2EF\7p\2\2FG\7v\2\2GH\7k\2\2HI\7")
        buf.write("p\2\2IJ\7w\2\2JK\7g\2\2K\20\3\2\2\2LM\7d\2\2MN\7t\2\2")
        buf.write("NO\7g\2\2OP\7c\2\2PQ\7m\2\2Q\22\3\2\2\2RS\7&\2\2S\24\3")
        buf.write("\2\2\2TU\7.\2\2U\26\3\2\2\2VW\7<\2\2W\30\3\2\2\2XY\7=")
        buf.write("\2\2Y\32\3\2\2\2Z[\7>\2\2[\\\7/\2\2\\\34\3\2\2\2\5\2\36")
        buf.write("&\2")
        return buf.getvalue()


class MMADLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NEWLINE = 1
    STRING = 2
    INPUT = 3
    OUTPUT = 4
    RETURN = 5
    YIELD = 6
    CONTINUE = 7
    BREAK = 8
    MATH_EXPRESSION_SIGN = 9
    COMMA = 10
    COLON = 11
    SEMICOLON = 12
    ASSIGNMENT = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Input'", "'Output'", "'return'", "'yield'", "'continue'", 
            "'break'", "'$'", "','", "':'", "';'", "'<-'" ]

    symbolicNames = [ "<INVALID>",
            "NEWLINE", "STRING", "INPUT", "OUTPUT", "RETURN", "YIELD", "CONTINUE", 
            "BREAK", "MATH_EXPRESSION_SIGN", "COMMA", "COLON", "SEMICOLON", 
            "ASSIGNMENT" ]

    ruleNames = [ "NEWLINE", "STRING", "INPUT", "OUTPUT", "RETURN", "YIELD", 
                  "CONTINUE", "BREAK", "MATH_EXPRESSION_SIGN", "COMMA", 
                  "COLON", "SEMICOLON", "ASSIGNMENT" ]

    grammarFileName = "MMADL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


