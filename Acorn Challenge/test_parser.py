from game_parser import parse
from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)
from game_parser import read_lines
from game_parser import if_exclusive_num

def change_to_string(grid):
    str1 = ''
    for t in grid:
        str2 = ''
        for j in t:
            str2 += j.display
        str1 += str2+"\n"
    return str1

def test_parse1():
    assert change_to_string(parse(read_lines("board_simple.txt"))) == "**X**\n*   *\n**Y**\n","parse() should return lists of list of cells"
    print("parser1: possitive case passed")

def test_parse2():
    try:
        assert parse(read_lines("bad_letter.txt")) == None
    except ValueError as e:
        assert print(e) == print("Bad letter in configuration file: s.")
    try:
        assert parse(read_lines("2end_points.txt")) == None
    except ValueError as e:
        assert print(e) == print("Expected 1 ending position, got 2.")
    try:
        assert parse(read_lines("2start_points.txt")) == None
    except ValueError as e:
        assert print(e) == print("Expected 1 starting position, got 2.")
    try:
        assert parse(read_lines("no-matching_tc.txt")) == None
    except ValueError as e:
        assert print(e) == print("Teleport pad 2 does not have an exclusively matching pad.")
    print("parser2: bad maps passed")

def run_tests():
    test_parse1()
    test_parse2()
