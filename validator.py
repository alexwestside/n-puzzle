from errors import Errors
from io import StringIO
import re


class Validator(Errors):
    def __init__(self):
        Errors.__init__(self)
        self.list_puzzle = []
        self.matrix = []

    def validate(self):
        self.delete_comments()
        self.parse_input()
        self.current_size()

    def delete_comments(self):
        for line in StringIO(self.raw):
            line = line.strip()
            if '#' in line:
                self.list_puzzle.append(re.search('(.*)#', line).groups()[0])
            else:
                self.list_puzzle.append(line)
        self.list_puzzle = list(filter(None, self.list_puzzle))

    def parse_input(self):
        for line in self.list_puzzle:
            try:
                self.matrix.append(list(map(lambda x: int(x), line.split())))
            except Exception as e:
                self.critical("invalid numbers format: " + str(e))

    def current_size(self):
        size_line = self.matrix.pop(0)
        try:
            if len(size_line) != 1:
                self.critical(str(IndexError))
            self.size = int(size_line[0])
        except Exception as e:
            self.critical("invalid puzzle size format" + str(e))
        if self.size < 2:
            print(self.size)
            self.critical("puzzle size should be >= 2")
