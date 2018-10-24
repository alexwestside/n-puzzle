import pytest
from src.puzzle import Puzzle


@pytest.fixture()
def resource_setup(request):
    print("resource_setup")

    def resource_teardown():
        print("resource_teardown")

    request.addfinalizer(resource_teardown)


def test_3x3_1():
    puzzle = Puzzle()
    htype = "m"
    file = "test_3x3_1.txt"
    puzzle.read(file)
    puzzle.validate()
    puzzle.get_heuristic_type(htype)
    puzzle.generate(file)
    node = puzzle.solver()
    assert node.grid == node.solved_puzzle


def test_3x3_2():
    puzzle = Puzzle()
    htype = "m"
    file = "test_3x3_2.txt"
    puzzle.read(file)
    puzzle.validate()
    puzzle.get_heuristic_type(htype)
    puzzle.generate(file)
    node = puzzle.solver()
    assert node.grid == node.solved_puzzle


def test_3x3_3():
    puzzle = Puzzle()
    htype = "m"
    file = "test_3x3_3.txt"
    puzzle.read(file)
    puzzle.validate()
    puzzle.get_heuristic_type(htype)
    puzzle.generate(file)
    node = puzzle.solver()
    assert node.grid == node.solved_puzzle


def test_3x3_4():
    puzzle = Puzzle()
    htype = "m"
    file = "test_3x3_4.txt"
    puzzle.read(file)
    puzzle.validate()
    puzzle.get_heuristic_type(htype)
    puzzle.generate(file)
    node = puzzle.solver()
    assert node.grid == node.solved_puzzle


def test_3x3_5():
    puzzle = Puzzle()
    htype = "m"
    file = "test_3x3_5.txt"
    puzzle.read(file)
    puzzle.validate()
    puzzle.get_heuristic_type(htype)
    puzzle.generate(file)
    node = puzzle.solver()
    assert node.grid == node.solved_puzzle


def test_3x3_6():
    puzzle = Puzzle()
    htype = "m"
    file = "test_3x3_6.txt"
    puzzle.read(file)
    puzzle.validate()
    puzzle.get_heuristic_type(htype)
    puzzle.generate(file)
    node = puzzle.solver()
    assert node.grid == node.solved_puzzle


def test_3x3_7():
    puzzle = Puzzle()
    htype = "m"
    file = "test_3x3_7.txt"
    puzzle.read(file)
    puzzle.validate()
    puzzle.get_heuristic_type(htype)
    puzzle.generate(file)
    node = puzzle.solver()
    assert node.grid == node.solved_puzzle


def test_3x3_8():
    puzzle = Puzzle()
    htype = "m"
    file = "test_3x3_8.txt"
    puzzle.read(file)
    puzzle.validate()
    puzzle.get_heuristic_type(htype)
    puzzle.generate(file)
    node = puzzle.solver()
    assert node.grid == node.solved_puzzle


def test_3x3_9():
    puzzle = Puzzle()
    htype = "m"
    file = "test_3x3_9.txt"
    puzzle.read(file)
    puzzle.validate()
    puzzle.get_heuristic_type(htype)
    puzzle.generate(file)
    node = puzzle.solver()
    assert node.grid == node.solved_puzzle


def test_3x3_10():
    puzzle = Puzzle()
    htype = "m"
    file = "test_3x3_10.txt"
    puzzle.read(file)
    puzzle.validate()
    puzzle.get_heuristic_type(htype)
    puzzle.generate(file)
    node = puzzle.solver()
    assert node.grid == node.solved_puzzle


def test_4X4_1():
    puzzle = Puzzle()
    htype = "m"
    file = "test_4X4_1.txt"
    puzzle.read(file)
    puzzle.validate()
    puzzle.get_heuristic_type(htype)
    puzzle.generate(file)
    node = puzzle.solver()
    assert node.grid == node.solved_puzzle


def test_4X4_2():
    puzzle = Puzzle()
    htype = "m"
    file = "test_4X4_2.txt"
    puzzle.read(file)
    puzzle.validate()
    puzzle.get_heuristic_type(htype)
    puzzle.generate(file)
    node = puzzle.solver()
    assert node.grid == node.solved_puzzle


def test_4X4_3():
    puzzle = Puzzle()
    htype = "m"
    file = "test_4X4_3.txt"
    puzzle.read(file)
    puzzle.validate()
    puzzle.get_heuristic_type(htype)
    puzzle.generate(file)
    node = puzzle.solver()
    assert node.grid == node.solved_puzzle


def test_4X4_4():
    puzzle = Puzzle()
    htype = "m"
    file = "test_4X4_4.txt"
    puzzle.read(file)
    puzzle.validate()
    puzzle.get_heuristic_type(htype)
    puzzle.generate(file)
    node = puzzle.solver()
    assert node.grid == node.solved_puzzle


def test_4X4_5():
    puzzle = Puzzle()
    htype = "m"
    file = "test_4X4_5.txt"
    puzzle.read(file)
    puzzle.validate()
    puzzle.get_heuristic_type(htype)
    puzzle.generate(file)
    node = puzzle.solver()
    assert node.grid == node.solved_puzzle

def test_5X5_1():
    puzzle = Puzzle()
    htype = "m"
    file = "test_5X5_1.txt"
    puzzle.read(file)
    puzzle.validate()
    puzzle.get_heuristic_type(htype)
    puzzle.generate(file)
    node = puzzle.solver()
    assert node.grid == node.solved_puzzle


def test_5X5_2():
    puzzle = Puzzle()
    htype = "m"
    file = "test_5X5_2.txt"
    puzzle.read(file)
    puzzle.validate()
    puzzle.get_heuristic_type(htype)
    puzzle.generate(file)
    node = puzzle.solver()
    assert node.grid == node.solved_puzzle


def test_error():
    puzzle = Puzzle()
    file = "test_error.txt"
    with pytest.raises(SystemExit):
        puzzle.read(file)
        puzzle.validate()


def test_error_1():
    puzzle = Puzzle()
    file = "test_error_1.txt"
    with pytest.raises(SystemExit):
        puzzle.read(file)
        puzzle.validate()


def test_error_2():
    puzzle = Puzzle()
    file = "test_error_2.txt"
    with pytest.raises(SystemExit):
        puzzle.read(file)
        puzzle.validate()


def test_error_empty():
    puzzle = Puzzle()
    file = "test_error_empty.txt"
    with pytest.raises(SystemExit):
        puzzle.read(file)
        puzzle.validate()
