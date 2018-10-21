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
        v_conflicts, h_conflicts = self.linear_conflict(grid, n, solved_puzzle)
        manhattan = self.manhattan(grid, n, solved_puzzle)
        linear_conflict = len(h_conflicts) + len(v_conflicts)
        return manhattan + linear_conflict

    def linear_conflict(self, grid, n, solved_puzzle):
        h_conflicts = self.conflict_in_line(grid, solved_puzzle)
        v_resolved, v_unsolved = [[] for _ in range(n)], [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                v_resolved[j].append(solved_puzzle[i][j])
                v_unsolved[j].append(grid[i][j])
        v_conflicts = self.conflict_in_line(v_unsolved, v_resolved)
        return v_conflicts, h_conflicts

    def conflict_in_line(self, solved, unsolved):
        conflicts = []
        for solved_row, unsolved_row in zip(solved, unsolved):
            for n in unsolved_row:
                for m in unsolved_row:
                    if self.check_exist(n, m, solved_row) is True \
                            and (self.check_strength_conflict(n, m, solved_row, unsolved_row) is True or self.check_rev_conflict(n, m, solved_row, unsolved_row) is True):
                        conflicts.append((n, m))
        return conflicts

    @staticmethod
    def check_exist(n, m, solved_row):
        if m in solved_row and n in solved_row:
            return True
        return False

    @staticmethod
    def check_strength_conflict(n, m, solved_row, unsolved_row):
        if (solved_row.index(n) != unsolved_row.index(n)
                and ((unsolved_row.index(n) < unsolved_row.index(m)
                      and solved_row.index(n) > solved_row.index(m)) or (unsolved_row.index(m) < unsolved_row.index(n) and solved_row.index(m) > solved_row.index(n)))):
            return True
        return False

    @staticmethod
    def check_rev_conflict(n, m, solved_row, unsolved_row):
        if (solved_row.index(m) != unsolved_row.index(m)
                and ((unsolved_row.index(m) < unsolved_row.index(n)
                      and solved_row.index(m) > solved_row.index(n)) or (unsolved_row.index(n) < unsolved_row.index(m) and solved_row.index(n) > solved_row.index(m)))):
            return True
        return False

    def linear_corner_manhattan(self, grid, n, solved_puzzle):
        corner_conflicts = self.corner_conflict(grid, n, solved_puzzle)
        vertical_conflicts, horizontal_conflicts = self.linear_conflict(grid, n, solved_puzzle)
        linear_conflict_h = len(horizontal_conflicts) + len(vertical_conflicts)
        xy_linear_conflicts = []
        for conflict in vertical_conflicts:
            xy_linear_conflicts += list(conflict)
        for conflict in horizontal_conflicts:
            xy_linear_conflicts += list(conflict)
        manhattan_h = self.manhattan(grid, n, solved_puzzle)
        h_corner_conflicts = 0
        for conflict in corner_conflicts:
            if all([c not in xy_linear_conflicts for c in conflict]):
                h_corner_conflicts += 2

        return h_corner_conflicts + manhattan_h + linear_conflict_h

    def linear_corner_misplaced_manhattan(self, grid, n, solved_puzzle):
        return self.linear_corner_manhattan(grid, n, solved_puzzle) + self.misplaced_conflict(grid, n, solved_puzzle)

    def misplaced_conflict(self, grid, n, solved_puzzle):
        count = 0
        for n in range(n):
            for k in range(n):
                if grid[n][k] != solved_puzzle[n][k]:
                    count += 1
        return count

    def corner_conflict(self, grid, n, solved_puzzle):
        conflicts = []

        for i in range(n):
            for j in range(n):
                if i == 0 and j == 0:
                    if grid[i][j] != solved_puzzle[i][j] and grid[i][j + 1] == solved_puzzle[i][j + 1] and grid[i + 1][j] == solved_puzzle[i + 1][j]:
                        conflicts.append((grid[i][j + 1], grid[i + 1][j]))
                elif i == 0 and j == n - 1:
                    if grid[i][j] != solved_puzzle[i][j] and grid[i][j - 1] == solved_puzzle[i][j - 1] and grid[i + 1][j] == solved_puzzle[i + 1][j]:
                        conflicts.append((grid[i][j - 1], grid[i + 1][j]))
                elif i == n - 1 and j == n - 1:
                    if grid[i][j] != solved_puzzle[i][j] and grid[i][j - 1] == solved_puzzle[i][j - 1] and grid[i - 1][j] == solved_puzzle[i - 1][j]:
                        conflicts.append((grid[i][j - 1], grid[i - 1][j]))
                elif i == n - 1 and j == 0:
                    if grid[i][j] != solved_puzzle[i][j] and grid[i][j + 1] == solved_puzzle[i][j + 1] and grid[i - 1][j] == solved_puzzle[i - 1][j]:
                        conflicts.append((grid[i][j + 1], grid[i - 1][j]))
        return conflicts
