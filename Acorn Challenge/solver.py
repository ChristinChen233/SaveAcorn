from game import Game
from game_parser import read_lines
from grid import (grid_to_string,findpoint,findpoint3, find_for_mark)
from player import Player
from cells import (Start,End,Air,Wall,Fire,Water,Teleport)
import sys
            
def valiad2(game, x, y, mark, visited):
    if x >= 0 and y >= 0 and x < len(game.board) and y < len(game.board[0]):
        if ((mark[x][y] != 0 and type(game.board[x][y]) != Fire) or \
            (type(game.board[x][y]) == Fire and game.num_water_buckets >= 1)) \
             and  (mark[x][y], game.num_water_buckets) not in visited:
            return True
        return False
    return False

def copy_game(game, filename):
    new = Game(filename)
    new.board = list(game.board)
    new.movestep = list(game.movestep)
    new.stepcounter = game.stepcounter
    new.num_water_buckets = game.num_water_buckets
    new.alive = game.alive
    new.win = game.win
    return new

if __name__ == "__main__":
    solution_found = False
    if len(sys.argv) <= 2:
        print("Usage: python3 solver.py <filename> <mode>")
        sys.exit()
    else:
        (a, filename, mode) = sys.argv
        try:
            game=Game(filename)
        except FileNotFoundError as e:
            print (e)
            sys.exit()
        except ValueError as e:
            print (e)
            sys.exit()
        (row,col)=findpoint(game.board, "X")
        # Made a 2-D arrary called mark , to record thr parent cell of each cell and 
        # judge if this node has been visited.
        mark = []
        marks=1
        for i in range(len(game.board)):
            row0 = []
            for j in range(len(game.board[i])):
                if type(game.board[i][j]) != Wall:
                    row0.append(marks)
                    marks += 1
                else:
                    row0.append(0)
            mark.append(row0)
        current=(row, col) # save current cell
        ls = [current] # save cells need to be visited
        visited = [] # save visited cells
        dictionaries = {} # dictionaries save {key(current cell) : value(current game)}
        dictionaries[ mark[row][col] ] = game
        counter = 0
        while True:
            counter += 1
            if type(game.board[row][col]) == End:
                solution_found = True
                break
            if counter>10000:
                break
            if ls == []:
                break
            if mode == "DFS":
                current = ls[-1]
                ls.pop()
            if mode =="BFS":
                current = ls[0]
                ls.pop(0)
            row = current[0]
            col = current[1]
            parent = dictionaries[mark[row][col]]
            count = 4
            if valiad2(parent, row-1, col, mark, visited): # if up can go
                new_game = copy_game(parent, filename)
                new_game.game_for_solver("w")
                if type(parent.board[row-1][col]) == Teleport:
                    (x, y) = findpoint3(game.board, game.board[row-1][col].display, row-1, col)
                    ls.append( (x, y) )
                    dictionaries[ mark[x][y] ] = new_game
                else:
                    new_game.board[row-1][col].solver(new_game, row-1, col) # do something on current cell
                    ls.append( (row-1, col) )
                    dictionaries[ mark[row-1][col] ] = new_game
                count -=1
            if valiad2(parent, row, col+1, mark, visited): # if right can go
                new_game = copy_game(parent, filename)
                new_game.game_for_solver("d")
                if type(parent.board[row][col+1]) == Teleport:
                    (x, y) = findpoint3(game.board, game.board[row][col+1].display, row, col+1)
                    ls.append( (x, y) )
                    dictionaries[ mark[x][y] ] = new_game
                else:
                    new_game.board[row][col+1].solver(new_game, row, col+1) # do something on current cell
                    ls.append( (row, col+1) ) 
                    dictionaries[ mark[row][col+1] ] = new_game
                count -=1
            if valiad2(parent, row+1, col, mark, visited): # if down can go
                new_game = copy_game(parent, filename)
                new_game.game_for_solver("s")
                if type(parent.board[row+1][col]) == Teleport:
                    (x,y) = findpoint3(game.board, game.board[row+1][col].display, row+1, col)
                    ls.append( (x, y) )
                    dictionaries[ mark[x][y] ] = new_game
                else:
                    new_game.board[row+1][col].solver(new_game, row+1, col) # do something on current cell
                    ls.append( (row+1, col) )
                    dictionaries[ mark[row+1][col] ] = new_game
                count -=1
            if valiad2(parent, row, col-1, mark, visited): # if left can go
                new_game = copy_game(parent, filename)
                new_game.game_for_solver("a")
                if type(parent.board[row][col-1]) == Teleport:
                    visited.append((mark[row][col], parent.num_water_buckets))
                    (x, y) = findpoint3(game.board, game.board[row][col-1].display, row, col-1)
                    ls.append( (x, y) )
                    dictionaries[ mark[x][y] ] = new_game
                else:
                    new_game.board[row][col-1].solver(new_game, row, col-1) # do something on current cell
                    ls.append( (row, col-1) )
                    dictionaries[ mark[row][col-1] ] = new_game
                count -=1
            if count == 4 and type(parent.board[row][col]) == Teleport:
                parent.game_for_solver("e")
                (x, y) = findpoint3(game.board, game.board[row][col].display, row, col)
                ls.append( (x, y) )
                dictionaries[ mark[x][y] ] = parent
            visited.append((mark[row][col], parent.num_water_buckets))

    if solution_found:
        way = dictionaries[marks-1].movestep
        if len(way) == 1:
            print("Path has 1 move.")
            print("Path: {}".format(way[0]))
        else:
            print("Path has {} moves".format(len(way)))
            print("Path: ",end="")
            for i in range(len(way)-1):
                print(way[i], end=", ")
            print(way[-1])
    else:
        print("There is no possible path.")
