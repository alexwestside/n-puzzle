from errors import Errors
from io import StringIO
import re


class Validator(Errors):
    def __init__(self, raw):
        self.error = Errors.__init__(self)
        self.raw = raw
        self.list = []

    def validate(self):
        self.list = self.delete_comments()
        self.parse_input()

    def delete_comments(self):
        res = []
        for line in StringIO(self.raw):
            line = line.strip()
            if '#' in line:
                res.append(re.search('(.*)#', line).groups()[0])
            else:
                res.append(line)
        return list(filter(None, res))

    def parse_input(self):
        matrix = []
        for line in self.list:
            try:
                matrix.append(list(map(lambda x: int(x), line.split())))
            except ValueError:
                self.error.critical("invalid numbers format")
        return matrix

    def get_size(self):
        try:
            if len(size_row) != 1:
                raise IndexError
            size = int(size_row[0])
        except (IndexError, ValueError) as e:
            self.error.critical("invalid puzzle size format")
        if size < 2:
            self.error.critical("puzzle size should be >= 2")
        return size
