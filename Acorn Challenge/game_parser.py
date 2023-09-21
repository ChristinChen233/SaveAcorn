from cells import (Start,End,Air,Wall,Fire,Water,Teleport)

def read_lines(filename): 
    """Read in a file and return the contents as a list of strings."""
    try:
        f = open(filename, "r")
    except FileNotFoundError:
        raise FileNotFoundError("{} does not exist!".format(filename))
        return None
    lines = f.readlines()
    return lines

def if_exclusive_num(ls,a): 
    """This function is used to test if there has 2 "a" in "ls" """
    count = 0
    for t in ls:
        for i in range(len(t)):
            if t[i] == a:
                count += 1
    if count != 2:
        return True   #bad
    return False #good

def parse(lines): 
    """Transform the input into a grid.

    Arguments:
        lines -- list of strings representing the grid

    Returns:
     list -- contains list of lists of Cells
    """
    cells = [Start(), End(), Air(), Wall(), Fire(), Water()]
    (s,e,air,wall,fire,water) = cells # s = start point, e = end point
    cell_ls = ["X","Y"," ","F","*","W","1","2","3","4","5","6","7","8","9"]
    ls = [] #list of lists of Cells
    ls2 = [] #save numbers
    xcounter = 0
    ycounter = 0
    for item in lines:
        ls0 = [] # save each row
        row = item.strip("\n") # delete the symbol "\n"
        for i in range(len(row)):
            if cell_ls.count(row[i]) == 0:
                raise ValueError("Bad letter in configuration file: {}.".format(row[i]))
                return None
            elif row[i] == "X":
                xcounter += 1
                ls0.append(s)
            elif row[i] == "Y":
                ycounter += 1
                ls0.append(e)
            elif row[i] == " ":
                ls0.append(air)
            elif row[i] == "F":
                ls0.append(fire)
            elif row[i] == "*":
                ls0.append(wall)
            elif row[i] == "W":
                ls0.append(water)
            elif row[i].isnumeric:
                tc = Teleport(row[i]) # tc = Teleport cells 
                ls2.append(tc.display) # save numbers (string)
                ls0.append(tc)
        ls.append(ls0)
    if xcounter != 1:
        raise ValueError("Expected 1 starting position, got {}.".format(xcounter))
        return None
    if ycounter != 1:
        raise ValueError("Expected 1 ending position, got {}.".format(ycounter))
        return None
    for num in ls2:
        shouldbreak = if_exclusive_num(lines, num)
        if shouldbreak:
            raise ValueError("Teleport pad {} does not have an exclusively matching pad.".format(num))
            return None
    return ls
