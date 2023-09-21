# SaveAcorn
The fantastic maze game saving the poor acorn!

# Game Description
You are helping our poor acorn to walk out the maze safely. On your way, bravely extinguish the fire using water drop you collected, and make use of the same number cells to perform space jumps to shorten the journey.
- Use W A S D to move
- Use solver.py DFS/BFS to output the solution.
- You can make your own map your_map.txt, the cells are crresponded to different marks
  |Cell chracter|Meaning|
  |-|------------------------------|
  |A|Player cell (stands for Acorn)|
  |''|Air cell (space bar)|
  |X|Starting cell|
  |Y|Ending/Coal cell|
  |*|Wall cells|
  |1,2,3,4,5,6,7,8,0|Teleport cells. These numbers will come in pairs. On stepping onto the cell, you enter the cell '1', you teleport to the other '1'. Values greater than 9 will not be given. Note: 0 is not a valid teleport pad!|
  |W|A water bucket cell. On stepping onto the cell, the player gains a water bucket.|
  |F|A fire obstacle that you cannot pass unless you have a water bucket.|
  
