from copy import deepcopy


class Node:

    def __init__(self, parrent, grid, n, gvalue, solved_puzzle, heuristic_func):
        self.heuristic_func = heuristic_func
        self.solved_puzzle = solved_puzzle
        self.parent = parrent
        self.grid = grid
        self.GVALUE = gvalue
        self.HVALUE = None
        self.FSCORE = None
        self.zx = 0
        self.zy = 0
        self.n = n
        self.compute()

    def __eq__(self, node):
        return self.FSCORE == node.FSCORE

    def solved(self):
        return True if self.grid == self.solved_puzzle else False

    def new_node(self, x, y):
        new_grid = self.swap_target(x, y)
        node = Node(self, new_grid, self.n, self.GVALUE + 1, self.solved_puzzle, self.heuristic_func)
        return node

    def swap_target(self, target_x, target_y):
        target_value = self.grid[target_x][target_y]
        new_grid = deepcopy(self.grid)
        new_grid[self.zx][self.zy] = target_value
        new_grid[target_x][target_y] = 0
        return new_grid

    def get_child_nods(self):
        child_nods = []
        if self.zx != 0:
            child_nods.append(self.new_node(self.zx - 1, self.zy))
        if self.zx != self.n - 1:
            child_nods.append(self.new_node(self.zx + 1, self.zy))
        if self.zy != 0:
            child_nods.append(self.new_node(self.zx, self.zy - 1))
        if self.zy != self.n - 1:
            child_nods.append(self.new_node(self.zx, self.zy + 1))
        return child_nods

    def compute(self):
        self.HVALUE = self.heuristic_func(self.grid, self.n, self.solved_puzzle)
        self.FSCORE = self.HVALUE + self.GVALUE
        self.define_zero_coords()

    def define_zero_coords(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.grid[i][j] == 0:
                    self.zx, self.zy = i, j
                    return
