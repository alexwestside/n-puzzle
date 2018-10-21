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

    def read(self, args):
        try:
            with open(args.file, 'r') as file:
                self.raw = file.read()
        except Exception as e:
            self.critical_error("Input error: " + str(e))

    def print(self, node=None):
        if node is None:
            print("Heuristic type: {}".format(self.get_heuristic_name()))
            print("Puzzle size: {}".format(self.size))
            print("Puzzle shape:")
        else:
            print('\nSolution is:')
            self.matrix_puzzle = node.grid
        max_width = len(str((self.size * self.size) - 1))
        for line in self.matrix_puzzle:
            ln = ""
            for val in line:
                ln += f" {val: <{max_width}} "
            print(ln)

    def solver(self):
        node = Node(None, self.matrix_puzzle, self.size, 0, self.solved_puzzle, self.heuristics_type)

        start_set = []
        heapq.heappush(start_set, (node.FSCORE, node))

        end_set = {}
        # complex_in_time = 0
        # complex_in_size = 0

        while start_set:
            node = heapq.heappop(start_set)[1]
            # complex_in_time += 1
            end_set[(str(node.grid))] = None
            if node.solved() is True:
                return node
                # print_report(current_node, solution_sequence, complex_in_time,
                #              complex_in_size, start_time)
                # sys.exit(0)
            # if verbose:
            #     print(current_node)
            solutions = node.get_child_nods()
            clean_solutions = list(filter(lambda x: str(x.grid) not in end_set, solutions))

            # complex_in_size += len(clean_solutions)

            for curr_node in clean_solutions:
                heapq.heappush(start_set, (curr_node.FSCORE, curr_node))

        self.common_error("Does not exist any solution")
        return None
