import argparse

from MMADLParser import MMADLParser


def parse_argv() -> MMADLParser.ParserParams:
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('-i', '--input', help='input filename')
    args_parser.add_argument('-t', '--type', help='program type')
    args_parser.add_argument('-p', '--platform', help='target platfoem')
    args_parser.add_argument('-s', '--style', help='output file pseudocode format')

    args = args_parser.parse_args()

    return args if args.input is not None else None


def main(parser_args: argparse.Namespace):
    assert parser_args is not None

    parser = MMADLParser.create(parser_args)

    assert parser is not None

    parser.MMADL_to_temp()


if __name__ == '__main__':
    main(parse_argv())
