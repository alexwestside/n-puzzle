from src.timer import Timer
from src.generator import Generator
from src.validator import Validator
from src.heuristics import Heuristics
from src.node import Node
import heapq
import os


class Puzzle(Timer, Generator, Validator, Heuristics):
    def __init__(self):
        self.moves = 0
        Timer.__init__(self)
        Heuristics.__init__(self)
        Generator.__init__(self)
        Validator.__init__(self)

    def read(self, file):
        if os.path.isfile(file) is False:
            print(file)
            self.critical_error("Object is not a file")

        try:
            with open(file, 'r') as f:
                self.raw = f.read()
                if len(self.raw) == 0:
                    self.critical_error("file is empty")
        except Exception as e:
            self.critical_error("Input error: " + str(e))

    def print(self, node=None):
        if node is None:
            print("Heuristic type: {}".format(self.get_heuristic_name()))
            print("Puzzle size: {}".format(self.size))
            print("Puzzle shape:")
        else:
            self.matrix_puzzle = node.grid
        max_width = len(str((self.size * self.size) - 1))
        for line in self.matrix_puzzle:
            ln = ""
            for val in line:
                ln += f" {val: <{max_width}} "
            print(ln)
        print()

    def solver(self):
        node = Node(None, self.matrix_puzzle, self.size, 0, self.solved_puzzle, self.heuristics_type)
        start_set = []
        heapq.heappush(start_set, (node.FSCORE, node))
        end_set = {}

        while start_set:
            self.complex_in_time += 1
            node = heapq.heappop(start_set)[1]
            end_set[(str(node.grid))] = None
            if node.solved() is True:
                return node
            solutions = node.get_child_nods()
            clean_solutions = list(filter(lambda x: str(x.grid) not in end_set, solutions))
            self.complex_in_size += len(clean_solutions)
            for curr_node in clean_solutions:
                heapq.heappush(start_set, (curr_node.FSCORE, curr_node))
        self.common_error("Does not exist any solution")

    def count_moves(self, node, path=False):
        solution_path = []
        current_node = node
        while current_node is not None:
            solution_path.append(current_node)
            self.moves += 1
            current_node = current_node.parent
        if path is True:
            print('Moves to solution:')
            for node in reversed(solution_path):
                self.print(node)

    def output_required(self):
        print(f'Complexity in time -> : {self.complex_in_time} cycles')
        print(f'Complexity in size -> : {self.complex_in_size} moves')
        print(f'Number of moves to solution: {self.moves}')
        print(f'Execution time: {self.get_execution_time()} ms')