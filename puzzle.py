from timer import Timer
from generator import Generator
from validator import Validator


class Puzzle(Timer, Generator, Validator):
    def __init__(self):
        self.raw = ""
        self.__timer = Timer.__init__(self)
        Generator.__init__(self)
        Validator.__init__(self, self.raw)

    def read(self, args):
        try:
            with open(args.f, 'r') as f:
                self.raw = f.read()
        except Exception as e:
            self.error.critical("Input error: " + str(e))
