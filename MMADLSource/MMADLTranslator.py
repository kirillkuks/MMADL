from select import select
from antlr4 import *

from ANTLR.MMADLLexer import MMADLLexer
from ANTLR.MMADLParser import MMADLParser

from MMADLTranslatorVisitor import MMADLTranslatorVisitor


class MMADLTranslator:
    def __init__(self, path_to_source) -> None:
        self.lexer = MMADLLexer(FileStream(path_to_source, encoding='utf_8_sig'))
        self.tree = MMADLParser(CommonTokenStream(self.lexer)).mmadl()
        self.visitor = MMADLTranslatorVisitor()

    def translate(self) -> str:
        self.visitor.visit(self.tree)
        
        return self.visitor.get_code()
