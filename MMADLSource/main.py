import argparse
import codecs

from antlr4 import *

from ParserParams import ParserParams

from MMADLPreParser import MMADLPreParser
from MMADLRetranslator import MMADLRetranslator
from MMADLTranslator import MMADLTranslator

from LaTeXTranslator.MMADLTranslatorTex import MMADLTranslatorTex


def parse_argv() -> argparse.Namespace:
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('-i', '--input', help='input filename')
    args_parser.add_argument('-t', '--type', help='program type')
    args_parser.add_argument('-p', '--platform', help='target platfoem')
    args_parser.add_argument('-s', '--style', help='output file pseudocode format')
    args_parser.add_argument('-o', '--output', help='output file')

    args = args_parser.parse_args()

    return args if args.input is not None else None


def main(parser_args: argparse.Namespace):
    assert parser_args is not None
    params = ParserParams.create(parser_args)

    parser = MMADLPreParser.create(params)

    assert parser is not None

    temp_code = parser.MMADL_to_temp()

    with codecs.open('temp.mmadlt', 'w', 'utf_8') as f:
        f.write(temp_code)

    translator = MMADLTranslatorTex('temp.mmadlt', params)
    # translator = MMADLRetranslator('temp.mmadlt', params)
    # retranslator = MMADLRetranslator('examples\\test.txt')
    code = translator.translate()

    translator.save(generate_pdf=False)

    with codecs.open('examples\\output.txt', 'w', 'utf_8') as f:
        f.write(code)


if __name__ == '__main__':
    main(parse_argv())
