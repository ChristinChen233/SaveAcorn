from game import Game
from player import Player
from cells import (Start,End,Air,Wall,Fire,Water,Teleport)
#finish
def test_game1():
    gametest=Game("board_simple.txt")
    gametest.newmove = "w"
    gametest.gameMove()
    gametest.newmove = "a"
    gametest.gameMove()
    gametest.newmove = "s"
    gametest.gameMove()
    assert gametest.movestep == ['w','a','s'],"game.Move function should record every valid movement"
    assert gametest.stepcounter == 3,"game.Move function should count evey valid step"
    print("game1: test function 'gameMove' passed")

def test_game2():
    gametest2 = Game("board_simple.txt")
    player = Player()
    assert player.row == 0,"player.row should initially be 0"
    assert player.col == 0,"player.col should initially be 0"
    player.row = 0
    player.col = 2
    gametest2.set_position(player)
    assert gametest2.row == 0, "game.row should be update to 0"
    assert gametest2.col == 2,"game.col should be update to 2"
    assert gametest2.position.display == "X","the current position is start point" 
    print("game2: test function 'set_position' passed")

def test_player1():
    player2 = Player()
    assert player2.row == 0,"player.row should initially be 0"
    assert player2.col == 0,"player.col should initially be 0"
    assert player2.newrow == 0,"player.newrow should initially be 0"
    assert player2.newcol == 0,"player.newcol should initially be 0"
    player2.move("w")
    assert player2.newrow == -1,"player.newrow should update to -1"
    assert player2.newcol == 0,"player.newcol should still be 0"
    assert player2.row == 0,"player.row should still be 0"
    assert player2.col == 0,"player.col should still be 0"
    player2.move("a")
    assert player2.newrow == 0,"player.newrow should be still be 0"
    assert player2.newcol == -1,"player.newcol should update to -1"
    assert player2.row == 0,"player.row should still be 0"
    assert player2.col == 0,"player.col should still be 0"
    player2.move("s")
    assert player2.newrow == 1,"player.newrow should update to 1"
    assert player2.newcol == 0,"player.newcol should still be 0"
    assert player2.row == 0,"player.row should still be 0"
    assert player2.col == 0,"player.col should still be 0"
    player2.move("d")
    assert player2.newrow == 0,"player.newrow should still be 0"
    assert player2.newcol == 1,"player.newcol should update to 1"
    assert player2.row == 0,"player.row should still be 0"
    assert player2.col == 0,"player.col should still be 0"
    print("player1: function 'move' test case passed")

def test_player2():
    player2 = Player()
    player2.move("d")
    player2.set_position()
    assert player2.row == 0,"player.row should still be 0"
    assert player2.col == 1,"player.col should update to 0"
    print("player2: test function'set_position' test case passed")

def test_cells():
    game3 = Game("board2.txt")
    assert game3.num_water_buckets == 0,"water buckets initially equal 0" 
    (game3.row, game3.col) = (1,3)
    game3.board[game3.row][game3.col].step(game3)
    assert game3.alive == False,"acron die"
    (game3.row, game3.col) = (1,1)
    game3.board[game3.row][game3.col].step(game3)
    assert game3.num_water_buckets == 1,"water buckets update to 1" 
    assert type(game3.board[1][1]) == Air,"water become air"
    (game3.row, game3.col) = (1,3)
    game3.board[game3.row][game3.col].step(game3)
    assert game3.num_water_buckets == 0,"water has been used"
    assert type(game3.board[1][3]) == Air,"fire become air"
    print("test_cell: water and fire, passed")

def test_cells2():
    game3 = Game("board4(tc).txt")
    player3 = Player()
    (game3.row, game3.col) = (1,1)
    game3.board[1][1].step(game3, player3)
    assert (player3.row, player3.col) == (1, 3),"player tele to another teleport cell"
    assert game3.position.display == "1"
    assert (game3.row, game3.col) == (1, 3)
    print("tc cells test case passed")

def run_tests():
    test_game1()
    test_game2()
    test_player1()
    test_player2()
    test_cells()
    test_cells2()

