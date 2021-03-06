from src.argparser import ArgParser
from src.puzzle import Puzzle


def run():
    puzzle = Puzzle()
    args = ArgParser().parse()

    if args.file and args.size:
        puzzle.common_error("flag --file and --size must be specify separately")

    if args.size and (args.size < 2 or args.size == 0):
        puzzle.critical_error("size should be >= 2")

    if args.file:
        puzzle.read(args.file)
        puzzle.validate()
    else:
        if args.size:
            puzzle.size = args.size

    puzzle.get_heuristic_type(args.htype)
    puzzle.generate(args.file)
    puzzle.print()
    node = puzzle.solver()
    puzzle.count_moves(node, args.path)
    print('\nSolution is:')
    puzzle.print(node=node)
    puzzle.output_required()
