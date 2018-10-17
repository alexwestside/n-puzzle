import random


class Generator:
    """ Class Generator provide methods to help generate random variant of SOLVABLE puzzle """

    def __init__(self):
        self.size = 3
        self.raw = []
        self.__steps = 500
        self.__shape = ""
        self.__puzzle = []
        self.__puzzle_numbers = []

    def generate(self):
        random.seed()
        self.__generate_solved_puzzle()
        for i in range(self.__steps):
            zx, zy = self.__zero_coord()
            lines = []
            if zx != 0:
                lines.append((zx - 1, zy))
            if zx != self.size - 1:
                lines.append((zx + 1, zy))
            if zy != 0:
                lines.append((zx, zy - 1))
            if zy != self.size - 1:
                lines.append((zx, zy + 1))
            sx, sy = random.choice(lines)
            self.__puzzle[zx][zy] = self.__puzzle[sx][sy]
            self.__puzzle[sx][sy] = 0
        self.__reshape_puzzle()
        self.raw = self.__shape.strip()
        self.matrix_puzzle = self.__puzzle

    def __generate_solved_puzzle(self):
        m, n = self.size, self.size
        k, l, val = 0, 0, 0
        self.__puzzle_numbers = [i for i in range(1, m * n)]
        self.__puzzle_numbers.append(0)
        self.__puzzle = [[0 for _ in range(m)] for _ in range(m)]

        while k < m and l < n:
            for i in range(l, n):
                self.__puzzle[k][i] = self.__puzzle_numbers[val]
                val += 1
            k += 1

            for i in range(k, m):
                self.__puzzle[i][n - 1] = self.__puzzle_numbers[val]
                val += 1
            n -= 1

            if k < m:
                for i in range(n - 1, (l - 1), -1):
                    self.__puzzle[m - 1][i] = self.__puzzle_numbers[val]
                    val += 1
                m -= 1

            if l < n:
                for i in range(m - 1, k - 1, -1):
                    self.__puzzle[i][l] = self.__puzzle_numbers[val]
                    val += 1
                l += 1

    def __reshape_puzzle(self):
        self.__shape = "{}\n".format(self.size)
        for row in self.__puzzle:
            for item in row:
                self.__shape += str(item) + ' '
            self.__shape += '\n'

    def __zero_coord(self):
        for n in range(self.size):
            for m in range(self.size):
                if self.__puzzle[n][m] == 0:
                    return n, m
