from game_parser import read_lines
from game_parser import parse
from grid import grid_to_string
from player import Player

#finish
class Game:
    def __init__(self, filename): 
        self.board = parse(read_lines(filename))
        self.newmove = ""
        self.row=0
        self.col=0
        self.movestep = []
        self.stepcounter = 0
        self.num_water_buckets = 0
        self.alive = True
        self.win = False
        self.position = None
        self.num_fire = 0
        
    def gameMove(self): #call this when valid move
        self.movestep.append(self.newmove)
        self.stepcounter += 1

    def set_position(self, player):
        """ Update player position in game"""
        self.position = self.board[player.row][player.col]
        self.row = player.row
        self.col = player.col

    def game_for_solver(self, move):
        """ This function is for solver to record movement for game object"""
        if move == "w":
            self.newmove = "w"
        if move == "a":
            self.newmove = "a"
        if move == "s":
            self.newmove = "s"
        if move == "d":
            self.newmove = "d"
        if move == "e":
            self.newmove = "e"
        self.gameMove()
