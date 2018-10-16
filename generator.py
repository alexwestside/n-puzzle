import random


class Generator:
    """ Class Generator provide methods to help generate random variant of SOLVABLE puzzle """

    def __init__(self):
        self.size = 3
        self.steps = 500
        self.shape = f"{self.size}\n"
        self.puzzle = []
        self.puzzle_numbers = []

    def generate(self):
        random.seed()
        self.generate_solved_puzzle()
        for i in range(self.steps):
            self.custom_swap()
        self.reshape_puzzle()
        return self.shape.strip()

    def generate_solved_puzzle(self):
        m, n = self.size, self.size
        k, l, val = 0, 0, 0
        self.puzzle_numbers = [i for i in range(1, m * n)]
        self.puzzle_numbers.append(0)
        self.puzzle = [[0 for _ in range(m)] for _ in range(m)]

        while k < m and l < n:
            for i in range(l, n):
                self.puzzle[k][i] = self.puzzle_numbers[val]
                val += 1
            k += 1

            for i in range(k, m):
                self.puzzle[i][n - 1] = self.puzzle_numbers[val]
                val += 1
            n -= 1

            if k < m:
                for i in range(n - 1, (l - 1), -1):
                    self.puzzle[m - 1][i] = self.puzzle_numbers[val]
                    val += 1
                m -= 1

            if l < n:
                for i in range(m - 1, k - 1, -1):
                    self.puzzle[i][l] = self.puzzle_numbers[val]
                    val += 1
                l += 1

    def custom_swap(self):
        zx, zy = self.zero_coord()
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
        self.puzzle[zx][zy] = self.puzzle[sx][sy]
        self.puzzle[sx][sy] = 0

    def reshape_puzzle(self):
        for row in self.puzzle:
            for item in row:
                self.shape += str(item) + ' '
            self.shape += '\n'

    def zero_coord(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.puzzle[i][j] == 0:
                    return i, j
