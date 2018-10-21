from time import time


class Timer:
    def __init__(self):
        self.__start_time = time()
        self.complex_in_time = 0
        self.complex_in_size = 0

    def get_execution_time(self):
        return round(time() - self.__start_time, 3)
