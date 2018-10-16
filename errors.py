import sys


class Errors:
    def __init__(self):
        pass

    def common(self, msg):
        self.print(msg)
        sys.exit(0)

    def critical(self, msg):
        self.print(msg)
        sys.exit(1)

    @staticmethod
    def print(msg):
        print("Exiting program...{}".format(msg))
