from antlr4 import *

import codecs
import subprocess
import os
import time

from ANTLR.MMADLLexer import MMADLLexer
from ANTLR.MMADLParser import MMADLParser

from ParserParams import ParserParams
from MMADLTranslatorVisitor import MMADLTranslatorVisitor


class MMADLTranslator:
    def __init__(self, path_to_source: str, params: ParserParams) -> None:
        self.lexer = MMADLLexer(FileStream(path_to_source, encoding='utf_8_sig'))
        self.tree = MMADLParser(CommonTokenStream(self.lexer)).mmadl()
        self.visitor = MMADLTranslatorVisitor(params)

        self.output_file = params.output

    def translate(self) -> str:
        self.visitor.visit(self.tree)
        
        return self.visitor.get_code()

    def save(self, filename: str = None, generate_pdf: bool = False) -> None:
        output = self.output_file if filename is None else filename

        with codecs.open(output, 'w', 'utf_8') as f:
            f.write(self.visitor.code)

        if generate_pdf:
            ind = output.rfind('\\')
            work_dir = os.getcwd()

            if ind != -1:
                os.chdir(work_dir + '\\' + output[:ind])
                output = output[(ind + 1):]

            cmd = ['pdflatex',\
                    '-interaction',\
                    'nonstopmode',\
                     output]
            proc = subprocess.Popen(cmd)
            proc.communicate()

            assert proc.returncode == 0

            time.sleep(5)

            self._delete_latex_files(os.getcwd())

            os.chdir(work_dir)

    def _delete_latex_files(self, dir: str) -> None:
        for file in os.listdir(dir):
            if file.split('.')[-1].lower() not in ['tex', 'pdf', 'txt', 'mmadl']:
                os.remove(file)
