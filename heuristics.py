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

    def manhattan(self):
        pass

    def linear_manhattan(self):
        pass

    def linear_corner_manhattan(self):
        pass

    def linear_corner_misplaced_manhattan(self):
        pass
