from antlr4 import *

from ParserParams import ParserParams

from MMADLTranslator import MMADLTranslator
from MMADLRetranslatorVisitor import MMADLRetranslatorVisitor


class MMADLRetranslator(MMADLTranslator):
    def __init__(self, path_to_source: str, params: ParserParams) -> None:
        super().__init__(path_to_source, params)

        self.visitor = MMADLRetranslatorVisitor(params)
