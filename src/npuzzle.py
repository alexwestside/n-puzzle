from src.argparser import ArgParser
from src.puzzle import Puzzle


def main():
    puzzle.generate(args.file)
    puzzle.print()
    node = puzzle.solver()
    puzzle.print(node=node)
    print(f'Execution time: {puzzle.get_execution_time()} ms')
    print(f'Time complexity -> : {puzzle.complex_in_time} cycles')
    print(f'Size complexity -> : {puzzle.complex_in_size} moves')


if __name__ == '__main__' and __package__:
    puzzle = Puzzle()
    args = ArgParser().parse()

    if args.file and args.size:
        puzzle.common_error("flag --file and --size must be specify separately")

    if args.size and (args.size < 2 or args.size == 0):
        puzzle.critical_error("size should be >= 2")

    if args.file:
        puzzle.read(args)
        puzzle.validate()
        # puzzle.is_solvable()
    else:
        if args.size:
            puzzle.size = args.size

    puzzle.get_heuristic_type(args.htype)

    main()
