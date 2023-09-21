def grid_to_string(grid, player): 
    """Turns a grid and player into a string

    Arguments:
        grid -- list of list of Cells
        player -- a Player with water buckets

    Returns:
        string: A string representation of the grid and player.
    """
    str1 = "" # string representation of the grid and player
    for i in range(len(grid)):
        row = "" # each row
        for j in range(len(grid[i])):
            if i == player.row and j == player.col:
                row += player.display
            else:
                row += grid[i][j].display
        str1 += row+"\n"
    if player.num_water_buckets == 1 :
        str1 += "\nYou have {} water bucket.".format(player.num_water_buckets)
    else:
        str1 += "\nYou have {} water buckets.".format(player.num_water_buckets)
    return str1

def findpoint(grid, symbol): 
    """ find start point or other single point in game board"""
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j].display == symbol:
                return i,j #return row and col

def findpoint2(grid, symbol, game): 
    """ Find another tc"""
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j].display == symbol and (game.row!=i or game.col!=j):
                return i,j

def findpoint3(grid, symbol, row, col):
    """ give a certain coordinate and find another tc in game board"""
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j].display == symbol and (row!=i or col!=j):
                return i,j

def find_for_mark(mark, symbol, game):
    """ give a symbol and find the coordinate of this symbol in 2D-array mark(represent game map)"""
    for i in range(len(game.board)):
        for j in range(len(game.board[i])):
            if mark[i][j] == symbol:
                return i,j
