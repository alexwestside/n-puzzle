from timer import Timer
from generator import Generator
from validator import Validator
from heuristics import Heuristics
from node import Node
import heapq


class Puzzle(Timer, Generator, Validator, Heuristics):
    def __init__(self):
        self.__timer = Timer.__init__(self)
        Heuristics.__init__(self)
        Generator.__init__(self)
        Validator.__init__(self)
        # Node.__init__(self)

    def read(self, args):
        try:
            with open(args.file, 'r') as file:
                self.raw = file.read()
        except Exception as e:
            self.critical_error("Input error: " + str(e))

    def print(self):
        print("Heuristic type: {}".format(self.get_heuristic_name()))
        print("Puzzle size: {}".format(self.size))
        print("Puzzle shape:")
        max_width = len(str((self.size * self.size) - 1))
        for line in self.matrix_puzzle:
            ln = ""
            for val in line:
                ln += f" {val: <{max_width}} "
            print(ln)

    def solver(self):
        node = Node(None, self.matrix_puzzle, self.size, 0, self.s, self.heuristics_type)

        start_set = []
        heapq.heappush(start_set, (node.FSCORE, node))

        end_set = {}
        # complex_in_time = 0
        # complex_in_size = 0

        while start_set:
            current_node = heapq.heappop(start_set)[1]
            # complex_in_time += 1
            end_set[(str(current_node.grid))] = None
            if current_node.solved is True:
                return current_node
                # print_report(current_node, solution_sequence, complex_in_time,
                #              complex_in_size, start_time)
                # sys.exit(0)
            # if verbose:
            #     print(current_node)
            solutions = current_node.get_all_children()
            clean_solutions = list(filter(lambda x: str(x.grid) not in end_set, solutions))

            # complex_in_size += len(clean_solutions)

            for candidate in clean_solutions:
                heapq.heappush(start_set, (candidate.F, candidate))

        self.common_error("Does not exist any solution")
        return None
