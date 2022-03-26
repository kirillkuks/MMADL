import sys
sys.path.append('..')

from MMADLTranslator import MMADLTranslator

from LaTeXTranslator.MMADLTranslatorTexVisitor import MMADLTranslatorTexVisitor


class MMADLTranslatorTex(MMADLTranslator):
    def __init__(self, path_to_source) -> None:
        super().__init__(path_to_source)

        self.visitor = MMADLTranslatorTexVisitor()

