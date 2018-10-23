from .errors import Errors
from io import StringIO
import re


class Validator(Errors):
    def __init__(self):
        Errors.__init__(self)
        self.lines_puzzle = []
        self.matrix_puzzle = []
        self.list_puzzle = []
        self.inversions = 0

    def validate(self):
        self.delete_comments()
        self.parse_input()
        self.current_size()
        self.check_len_lines()

    def check_len_lines(self):
        curr_len = len(self.matrix_puzzle[0])
        for line in self.matrix_puzzle:
            if len(line) != curr_len:
                self.critical_error("invalid puzzle format")

    def delete_comments(self):
        for line in StringIO(self.raw):
            line = line.strip()
            if '#' in line:
                self.lines_puzzle.append(re.search('(.*)#', line).groups()[0])
            else:
                self.lines_puzzle.append(line)
        self.lines_puzzle = list(filter(None, self.lines_puzzle))

    def parse_input(self):
        for line in self.lines_puzzle:
            try:
                self.matrix_puzzle.append(list(map(lambda x: int(x), line.split())))
            except Exception as e:
                self.critical_error("invalid numbers format: " + str(e))

    def current_size(self):
        size_line = self.matrix_puzzle.pop(0)
        try:
            if len(size_line) != 1:
                self.critical_error(str(IndexError))
            self.size = int(size_line[0])
        except Exception as e:
            self.critical_error("invalid puzzle size format" + str(e))
        if self.size < 2:
            self.critical_error("puzzle size should be >= 2")

    def count_inversions(self):
        for i in range(self.size ** 2 - 1):
            for j in range(i, self.size ** 2):
                if self.list_puzzle[i] and self.list_puzzle[j] and self.list_puzzle[i] > self.list_puzzle[j]:
                    self.inversions += 1

    def count_row_without_zero(self):
        for i, row in reversed(list(enumerate(self.matrix_puzzle))):
            if 0 in row:
                return self.size - i
