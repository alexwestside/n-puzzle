from timer import Timer
from generator import Generator
from validator import Validator
from heuristics import Heuristics


class Puzzle(Timer, Generator, Validator, Heuristics):
    def __init__(self):
        self.__timer = Timer.__init__(self)
        Heuristics.__init__(self)
        Generator.__init__(self)
        Validator.__init__(self)

    def read(self, args):
        try:
            with open(args.file, 'r') as file:
                self.raw = file.read()
        except Exception as e:
            self.critical("Input error: " + str(e))

    def print(self):
        print("Current heuristic type: {}".format(self.get_heuristic_name()))
        print("Current puzzle size: {}".format(self.size))
        print("Current puzzle shape:")
        max_width = len(str((self.size * self.size) - 1))
        for line in self.matrix_puzzle:
            ln = ""
            for val in line:
                ln += f" {val: <{max_width}} "
            print(ln)
