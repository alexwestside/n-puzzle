from argparser import ArgParser
from puzzle import Puzzle


def main():
    puzzle.validate()
    pass


if __name__ == '__main__':
    puzzle = Puzzle()
    args = ArgParser().parse()

    if args.file and args.size:
        puzzle.common("")

    if args.size and (args.size < 2 or args.size == 0):
        puzzle.critical("")

    if args.file:
        puzzle.read(args)
    else:
        if args.size:
            puzzle.size = args.size
        puzzle.generate()

    print(puzzle.raw)

    main()
