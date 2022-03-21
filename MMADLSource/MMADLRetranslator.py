from antlr4 import *

from MMADLTranslator import MMADLTranslator
from MMADLRetranslatorVisitor import MMADLRetranslatorVisitor


class MMADLRetranslator(MMADLTranslator):
    def __init__(self, path_to_source) -> None:
        super().__init__(path_to_source)

        self.visitor = MMADLRetranslatorVisitor()
