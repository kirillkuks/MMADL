from ANTLR.MMADLVisitor import MMADLVisitor

class MMADLTranslatorVisitor(MMADLVisitor):
    def __init__(self) -> None:
        super().__init__()

        self.code: str = ''

    def get_code(self) -> str:
        return self.code
