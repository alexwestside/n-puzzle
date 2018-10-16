from time import time


class Timer:
    def __init__(self):
        self.start_time = time()

    def get_execution_time(self):
        return round(time() - self.start_time, 3)
