import random
from copy import deepcopy


class Generator:
    """ Class Generator provide methods to help generate random variant of SOLVABLE puzzle """

    def __init__(self):
        self.size = 3
        self.raw = []
        self.__steps = 500
        self.__shape = ""
        self.__puzzle = []
        self.solved_puzzle = None

    def generate(self, file):
        random.seed()
        self.solved_puzzle = self.__generate_solved_puzzle()
        if file is None:
            self.matrix_puzzle = self.generate_new_puzzle_shape(self.solved_puzzle)

    def generate_new_puzzle_shape(self, puzzle):
        new_puzzle = deepcopy(puzzle)
        for i in range(self.__steps):
            zx, zy = self.__zero_coord(new_puzzle)
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
            new_puzzle[zx][zy] = new_puzzle[sx][sy]
            new_puzzle[sx][sy] = 0
        self.raw = self.__reshape_puzzle(new_puzzle).strip()
        return new_puzzle

    def __generate_solved_puzzle(self):
        m, n = self.size, self.size
        k, l, val = 0, 0, 0
        puzzle_numbers = [i for i in range(1, m * n)]
        puzzle_numbers.append(0)
        puzzle = [[0 for _ in range(m)] for _ in range(m)]

        while k < m and l < n:
            for i in range(l, n):
                puzzle[k][i] = puzzle_numbers[val]
                val += 1
            k += 1

            for i in range(k, m):
                puzzle[i][n - 1] = puzzle_numbers[val]
                val += 1
            n -= 1

            if k < m:
                for i in range(n - 1, (l - 1), -1):
                    puzzle[m - 1][i] = puzzle_numbers[val]
                    val += 1
                m -= 1

            if l < n:
                for i in range(m - 1, k - 1, -1):
                    puzzle[i][l] = puzzle_numbers[val]
                    val += 1
                l += 1
        return puzzle

    def __reshape_puzzle(self, puzzle):
        shape = "{}\n".format(self.size)
        for row in puzzle:
            for item in row:
                shape += str(item) + ' '
            shape += '\n'
        return shape

    def __zero_coord(self, puzzle):
        for n in range(self.size):
            for m in range(self.size):
                if puzzle[n][m] == 0:
                    return n, m
