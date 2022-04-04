import sys
sys.path.append('..')

from ParserParams import ParserParams
from MMADLTranslator import MMADLTranslator

from LaTeXTranslator.MMADLTranslatorTexVisitor import MMADLTranslatorTexVisitor


class MMADLTranslatorTex(MMADLTranslator):
    def __init__(self, path_to_source: str, params: ParserParams) -> None:
        super().__init__(path_to_source, params)

        self.visitor = MMADLTranslatorTexVisitor(params)

