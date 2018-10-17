from errors import Errors
from io import StringIO
import re


class Validator(Errors):
    def __init__(self):
        self.error = Errors.__init__(self)
        self.lines_puzzle = []
        self.matrix_puzzle = []
        self.list_puzzle = []
        self.inversions = 0

    def validate(self):
        self.delete_comments()
        self.parse_input()
        self.current_size()

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
                self.critical("invalid numbers format: " + str(e))

    def current_size(self):
        size_line = self.matrix_puzzle.pop(0)
        try:
            if len(size_line) != 1:
                self.critical(str(IndexError))
            self.size = int(size_line[0])
        except Exception as e:
            self.critical("invalid puzzle size format" + str(e))
        if self.size < 2:
            self.critical("puzzle size should be >= 2")

    def is_solvable(self):
        for row in self.matrix_puzzle:
            self.list_puzzle.extend(row)
        print(self.list_puzzle)
        self.count_inversions()
        if self.size & 1 == 0:  # "EVEN"
            blank_row = self.get_blank_row()
            if blank_row % 2 == 0 and self.inversions % 2 == 0:
                self.error.common("puzzle is not solvable")
        else:
            if self.inversions & 1 == 0:
                self.error.common("puzzle is not solvable")
        print('Puzzle is solvable')

    def count_inversions(self):
        for i in range(self.size ** 2 - 1):
            for j in range(i, self.size ** 2):
                if self.list_puzzle[i] and self.list_puzzle[j] and self.list_puzzle[i] > self.list_puzzle[j]:
                    self.inversions += 1

    def get_blank_row(self):
        for i, row in reversed(list(enumerate(self.matrix_puzzle))):
            if 0 in row:
                return self.size - i