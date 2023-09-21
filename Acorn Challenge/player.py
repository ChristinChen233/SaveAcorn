class Player:
    def __init__(self):
        self.display = 'A'
        self.num_water_buckets = 0
        self.newcol = 0
        self.newrow = 0
        self.col = 0 
        self.row = 0
        
    def move(self, move):
        """ find new player position according to original coordinate and movement""" 
        if move == "w":
            self.newrow = self.row-1
            self.newcol = self.col
        if move == "a":
            self.newcol = self.col-1
            self.newrow = self.row
        if move == "s":
            self.newrow = self.row+1
            self.newcol = self.col
        if move == "d":
            self.newcol = self.col+1
            self.newrow = self.row

    def set_position(self): 
        """ call this function if new movement is valid and update player position"""
        self.row = self.newrow
        self.col = self.newcol
