from argparse import ArgumentParser, RawTextHelpFormatter
from .heuristics import heuristics_help


class ArgParser:
    def __init__(self):
        self.parser = ArgumentParser(formatter_class=RawTextHelpFormatter)

    def parse(self):
        self.parser.add_argument('--file', metavar='file_path', help='path to the input file')
        self.parser.add_argument('--htype', metavar='heuristic', default='m', help=heuristics_help)
        self.parser.add_argument('--path', action='store_true', default=False, help='Show solution path')
        self.parser.add_argument('--size', metavar='size', type=int, help='specify puzzle size')
        return self.parser.parse_args()
