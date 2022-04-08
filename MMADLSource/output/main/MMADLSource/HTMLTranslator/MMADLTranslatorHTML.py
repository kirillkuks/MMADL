import sys
sys.path.append('..')

from MMADLTranslator import MMADLTranslator

from HTMLTranslator.MMADLTranslatorHTMLVisitor import MMADLTranslatorHTMLVisitor

class MMADLTranslatorHTML(MMADLTranslator):
    def __init__(self, path_to_source: str):
        super().__init__(path_to_source)
        self.visitor = MMADLTranslatorHTMLVisitor()
