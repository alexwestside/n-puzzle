from timer import Timer
from errors import Errors
from generator import Generator


class Puzzle(Errors, Timer, Generator):
    def __init__(self):
        self.raw = ""
        self.error = Errors.__init__(self)
        self.timer = Timer.__init__(self)
        Generator.__init__(self)

    def read(self, args):
        try:
            with open(args.f, 'r') as f:
                self.raw = f.read()
        except Exception as e:
            self.error.critical("Input error: " + str(e))
