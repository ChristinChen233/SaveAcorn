from game import Game
from game_parser import read_lines
from grid import (grid_to_string,findpoint)
from player import Player
from cells import (Start,End,Air,Wall,Fire,Water,Teleport)

def test_grid():
    game = Game("board_simple.txt")
    player = Player()
    assert print(grid_to_string(game.board, player)) == print("A*X**\n*   *\n**Y**\nYou have 0 water buckets.")
    player.num_water_buckets += 1
    assert print(grid_to_string(game.board, player)) == print("A*X**\n*   *\n**Y**\nYou have 1 water bucket.")
    print("grid: positive test cases passed")

def run_tests():
    test_grid()

