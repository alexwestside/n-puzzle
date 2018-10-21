heuristics_help = """Defined heuristics functions:
    -> 'm': Manhattan distance heuristic,
    -> 'lm': Linear conflict  + Manhattan distance,
    -> 'lcm': Linear conflict  + Corner conflict  + Manhattan distance,
    -> 'lcmm': Linear conflict  + Corner conflict  + Misplaced  + Manhattan distance
    Default functions: mnh"""


class Heuristics:
    def __init__(self):
        self.heuristics = {
            'm': self.manhattan,
            'lm': self.linear_manhattan,
            'lcm': self.linear_corner_manhattan,
            'lcmm': self.linear_corner_misplaced_manhattan
        }
        self.heuristics_name = {
            'm': "manhattan",
            'lm': "linear_manhattan",
            'lcm': "linear_corner_manhattan",
            'lcmm': "linear_corner_misplaced_manhattan"
        }
        self.heuristics_type = None
        self.heuristics_symbol = None

    def get_heuristic_type(self, htype):
        curr_htype = self.heuristics.get(htype)
        if curr_htype is None:
            print(heuristics_help)
            self.critical_error("no given heuristic function couldn't found")
        self.heuristics_type = curr_htype
        self.heuristics_symbol = htype

    def get_heuristic_name(self):
        return self.heuristics_name.get(self.heuristics_symbol)

    def manhattan(self, grid, n, solved_puzzle):
        solved = {}
        unsolved = {}

        h = 0
        for i in range(n):
            for j in range(n):
                solved[solved_puzzle[i][j]] = (i, j)
                unsolved[grid[i][j]] = (i, j)
        for num, solved_coors in solved.items():
            unsolved_coors = unsolved[num]
            for c in range(2):
                if unsolved_coors[c] < solved_coors[c]:
                    h += solved_coors[c] - unsolved_coors[c]
                else:
                    h += unsolved_coors[c] - solved_coors[c]

        return h

    def linear_manhattan(self, grid, n, solved_puzzle):
        vertical_conflicts, horizontal_conflicts = self.linear_conflict(grid, n, solved_puzzle)
        manhattan_h = self.manhattan(grid, n, solved_puzzle)
        linear_conflict_h = len(horizontal_conflicts) + len(vertical_conflicts)
        return manhattan_h + linear_conflict_h




    def linear_conflict(self, grid, n, solved_puzzle):
        horizontal_conflicts = self.conflict(grid, solved_puzzle)

        vertical_resolved_puzzle = [[] for _ in range(n)]
        vertical_unsolved_puzzle = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                vertical_resolved_puzzle[j].append(solved_puzzle[i][j])
                vertical_unsolved_puzzle[j].append(grid[i][j])

        vertical_conflicts = self.conflict(vertical_unsolved_puzzle, vertical_resolved_puzzle)
        return vertical_conflicts, horizontal_conflicts

    def conflict(self, solved, unsolved):
        conflicts = []
        for solved_row, unsolved_row in zip(solved, unsolved):
            for i in unsolved_row:
                for j in unsolved_row:
                    if j in solved_row and i in solved_row and ((solved_row.index(i) != unsolved_row.index(i) and ((unsolved_row.index(i) < unsolved_row.index(j) and solved_row.index(i) > solved_row.index(j)) or (unsolved_row.index(j) < unsolved_row.index(i) and solved_row.index(j) > solved_row.index(i)))) or (solved_row.index(j) != unsolved_row.index(j) and ((unsolved_row.index(j) < unsolved_row.index(i) and solved_row.index(j) > solved_row.index(i)) or (unsolved_row.index(i) < unsolved_row.index(j) and solved_row.index(i) > solved_row.index(j))))):
                        conflicts.append((i, j))
        return conflicts





    def linear_corner_manhattan(self):
        pass

    def linear_corner_misplaced_manhattan(self):
        pass
