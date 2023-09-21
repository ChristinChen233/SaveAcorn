from grid import findpoint2

class Start: 
    def __init__(self):
        self.display = 'X'

    def step(self, game):
        game.gameMove()
    
    def solver(self, game, x, y):
        pass

class End: 
    def __init__(self):
        self.display = 'Y'

    def step(self, game):
        game.gameMove()
        game.win = True
    
    def solver(self, game, x, y):
        pass

class Air: 
    def __init__(self):
        self.display = ' '

    def step(self, game):
        game.gameMove()
    
    def solver(self, game, x, y):
        pass

class Wall: 
    def __init__(self):
        self.display = '*'

    def step(self, game):
        pass

class Fire: 
    def __init__(self):
        self.display = 'F'
        self.word = ''

    def step(self, game):
        if game.num_water_buckets >= 1:
            self.word = "With your strong acorn arms, you throw a water bucket at the fire. "\
            "You acorn roll your way through the extinguished flames!"
            game.num_water_buckets -= 1
            game.gameMove()
            game.board[game.row][game.col] = Air() #change extinguished fire into air           
        else:
            self.word = "\nYou step into the fires and watch your dreams disappear :(."
            game.gameMove()
            game.alive = False
    
    def solver(self, game, row, col):
        game.num_water_buckets -= 1
        game.num_fire -= 1
        game.board[row][col] = Air() #change picked water into air

class Water: 
    def __init__(self):
        self.display = 'W'
        self.word=""

    def step(self, game):
        game.num_water_buckets += 1
        game.gameMove() 
        self.word = "Thank the Honourable Furious Forest, you've found a bucket of water!"
        game.board[game.row][game.col] = Air() #change picked water into air
    
    def solver(self, game, row, col):
        game.num_water_buckets += 1
        game.board[row][col] = Air() #change picked water into air
        
class Teleport: 
    def __init__(self,num):
        self.display = num  
        self.word=''

    def step(self, game, player):
        self.word="Whoosh! The magical gates break Physics as we know it and opens a wormhole through"\
        " space and time."
        (row,col) = findpoint2(game.board, self.display, game)
        player.row=row
        player.col=col
        game.set_position(player)
        game.gameMove()

    def solver(self,game, x, y):
        pass
