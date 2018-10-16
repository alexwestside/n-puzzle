from time import time


class Timer:
    def __init__(self):
        self.__start_time = time()

    def get_execution_time(self):
        return round(time() - self.__start_time, 3)
