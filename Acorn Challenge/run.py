from game import Game
from game_parser import read_lines
from grid import (grid_to_string,findpoint)
from player import Player
from cells import (Start,End,Air,Wall,Fire,Water,Teleport)
import os
import sys
#finish
if len(sys.argv) <= 1:
    print("Usage: python3 run.py <filename> [play]")
    sys.exit()
else:
    play = False
    if len(sys.argv) == 3:
        (a, filename, b) = sys.argv
        play = True
    if len(sys.argv) == 2:
        (a, filename) = sys.argv
    player = Player()
    try:
        game = Game(filename)
    except FileNotFoundError as e:
        print(e)
        sys.exit()
    except ValueError as e:
        print(e)
        sys.exit()
    if play:
        os.system("clear")
    (player.row, player.col)=findpoint(game.board, "X") # put the player at start point
    print(grid_to_string(game.board, player))# print current game board with plaer
    while game.alive:
        if game.win:
            break
        game.num_water_buckets = player.num_water_buckets
        move = input("\nInput a move: ")
        move = move.strip()
        move = move.lower()
        game.newmove = move # save new movements
        if play:
            os.system("clear")
        if move == "q":
            print("\nBye!")
            break # Quit the game
        elif move == "w" or move == "a" or move == "s" or move == "d":
            player.move(move) # player new row,col change by player row,col
            try:
                new_position = game.board[player.newrow][player.newcol]
            except IndexError:
                print(grid_to_string(game.board, player)) # print current game board with plaer
                print() 
                print("You walked into a wall. Oof!")
                continue
            if player.newcol < 0 or player.newrow < 0 or player.newcol >= len(game.board[player.newrow]) \
            or player.newrow >= len(game.board) or type(game.board[player.newrow][player.newcol]) == Wall:
                #Player new position is on wall or out of bound
                print(grid_to_string(game.board, player)) # print current game board with plaer
                print() 
                print("You walked into a wall. Oof!")
                continue
            if ( player.newrow < 0 or player.newcol < 0 or player.newcol >= len(game.board[player.newrow])-1\
                 or player.newrow >= len(game.board)-1 ) and type(game.board[player.newrow][player.newcol]) == Air:
                 # Player new position is on air wall or out of bound
                    print(grid_to_string(game.board, player)) # print current game board with plaer
                    print() 
                    print("You walked into a wall. Oof!")
            else:
                player.set_position() # valid move, update player position
                game.set_position(player) # valid move, update player position in game
                if type(game.position)==Teleport:
                    game.position.step(game, player) # position has changed
                    print(grid_to_string(game.board, player)) # print current game board with plaer
                    print()
                    print("Whoosh! The magical gates break Physics as we know it and opens a wormhole through"\
                           " space and time.")
                else:
                    game.position.step(game)
                    player.num_water_buckets = game.num_water_buckets # upgrade num_water_buckets in player
                    print(grid_to_string(game.board, player)) # print current game board with plaer
                    if type(game.position) == Fire or type(game.position) == Water:
                        print()
                        print(game.position.word) # print sentence out
        elif move == "e":
            if type(game.board[player.row][player.col]) == Teleport:
                    # teleport back
                 game.board[player.row][player.col].step(game, player)
                 print(grid_to_string(game.board, player))
                 print()
                 print("Whoosh! The magical gates break Physics as we know it and opens"\
                   " a wormhole through space and time.")
            else:
                print(grid_to_string(game.board, player))
                game.gameMove()
        else: # Invalid input
            print(grid_to_string(game.board, player)) # print current game board with plaer
            print()
            print("Please enter a valid move (w, a, s, d, e, q).")

    if game.win: # win
        s1="\nYou conquer the treacherous maze set up by the Fire Nation and reclaim the Honourable "
        s2="Furious Forest Throne, restoring your hometown back to its former glory of rainbow and "\
        "sunshine! Peace reigns over the lands.\n"
        print()
        print(s1+s2)
        if game.stepcounter == 1:
            print("You made 1 move.")
            print("Your move: {}".format(game.movestep[0]))
        else:
            print("You made {} moves.".format(game.stepcounter))
            print("Your moves: ", end="")
            for i in range(len(game.movestep)-1):
                print(game.movestep[i], end=", ")
            print(game.movestep[-1])
        print("\n=====================\n====== YOU WIN! =====\n=====================")

    if not game.alive: #acorn die
        print()
        print("The Fire Nation triumphs! The Honourable Furious Forest is reduced "\
             "to a pile of ash and is scattered to the winds by the next storm... You have been roasted.\n")
        if game.stepcounter == 1:
            print("You made 1 move.")
            print("Your move: {}".format(game.movestep[0]))
        else:
            print("You made {} moves.".format(game.stepcounter))
            print("Your moves: ", end="")
            for i in range(len(game.movestep)-1):
                print(game.movestep[i], end=", ")
            print(game.movestep[-1])
        print("\n=====================\n===== GAME OVER =====\n=====================")
