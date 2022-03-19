import argparse
import codecs

from MMADLPreParser import MMADLPreParser
from antlr4 import *

from ANTLR.MMADLLexer import MMADLLexer
from ANTLR.MMADLParser import MMADLParser
from ANTLR.MMADLVisitor import MMADLVisitor


def parse_argv() -> argparse.Namespace:
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('-i', '--input', help='input filename')
    args_parser.add_argument('-t', '--type', help='program type')
    args_parser.add_argument('-p', '--platform', help='target platfoem')
    args_parser.add_argument('-s', '--style', help='output file pseudocode format')

    args = args_parser.parse_args()

    return args if args.input is not None else None


def main(parser_args: argparse.Namespace):
    assert parser_args is not None

    parser = MMADLPreParser.create(parser_args)

    assert parser is not None

    temp_code = parser.MMADL_to_temp()

    with codecs.open('temp.txt', 'w', 'utf_8_sig') as f:
        f.write(temp_code)

    lexer = MMADLLexer(FileStream('temp.txt', encoding='utf_8'))
    tokens = CommonTokenStream(lexer)
    print(tokens.tokens)

    parser = MMADLParser(tokens)
    tree = parser.mmadl()

    visitor = MMADLVisitor()
    visitor.visit(tree)


if __name__ == '__main__':
    main(parse_argv())
