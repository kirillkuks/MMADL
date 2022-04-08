import argparse
import codecs

from antlr4 import *

from MMADLPreParser import MMADLPreParser
from MMADLRetranslator import MMADLRetranslator
from MMADLTranslator import MMADLTranslator

from LaTeXTranslator.MMADLTranslatorTex import MMADLTranslatorTex
from HTMLTranslator.MMADLTranslatorHTML import MMADLTranslatorHTML


def parse_argv() -> argparse.Namespace:
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('-i', '--input', help='input filename')
    args_parser.add_argument('-o', '--output', help='input filename')
    args_parser.add_argument('-t', '--type', help='program type')
    args_parser.add_argument('-p', '--platform', help='target platform')
    args_parser.add_argument('-s', '--style', help='output file pseudocode format')

    args = args_parser.parse_args()

    return args if args.input is not None else None


def main(parser_args: argparse.Namespace):
    if parser_args is None:
        print("Please set input file. Commands:\n"
              "-i, --input: input file\n"
              "-o, --output: output file\n"
              "-p, --platform: target platform\n"
              "-s, --style: output file pseudocode format")
        return

    parser = MMADLPreParser.create(parser_args)

    if parser is None:
        print("Please set input file. Commands:\n"
              "-i, --input: input file\n"
              "-o, --output: output file\n"
              "-p, --platform: target platform\n"
              "-s, --style: output file pseudocode format")
        return

    temp_code = parser.MMADL_to_temp()

    with codecs.open('temp1.mmadlt', 'w', 'utf_8') as f:
        f.write(temp_code)

    if parser_args.platform is not None and parser_args.platform == "html":
        retranslator = MMADLTranslatorHTML('temp1.mmadlt')
    else:
        retranslator = MMADLTranslatorTex('temp1.mmadlt')
    code = retranslator.translate()
    print(code)

    if parser_args.output is not None:
        with codecs.open(parser_args.output, 'w', 'utf_8') as f:
            f.write(code)


if __name__ == '__main__':
    main(parse_argv())
