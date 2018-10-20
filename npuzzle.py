from argparser import ArgParser
from puzzle import Puzzle


def main():
    puzzle.print()
    # if puzzle.solver() is not None:
        # puzzle.print()


if __name__ == '__main__':
    puzzle = Puzzle()
    args = ArgParser().parse()

    if args.file and args.size:
        puzzle.common_error("flag --file and --size must be specify separately")

    if args.size and (args.size < 2 or args.size == 0):
        puzzle.critical_error("size should be >= 2")

    if args.file:
        puzzle.read(args)
        puzzle.validate()
        puzzle.is_solvable()
    else:
        if args.size:
            puzzle.size = args.size
        puzzle.generate()

    puzzle.get_heuristic_type(args.htype)

    main()
