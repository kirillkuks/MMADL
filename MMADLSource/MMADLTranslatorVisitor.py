from ParserParams import ParserParams

from ANTLR.MMADLVisitor import MMADLVisitor

class MMADLTranslatorVisitor(MMADLVisitor):
    def __init__(self, params: ParserParams) -> None:
        super().__init__()

        self.params: ParserParams = params

        self.code: str = ''

    def get_code(self) -> str:
        return self.code
