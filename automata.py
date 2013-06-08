import graphics
from random import randint
from time import sleep
from copy import deepcopy
 
# Config
width = 20
height = 15
iterations = 500
pause_time = 0.1
game = []
display = graphics.SimpleDisplay("Cellular Automata", width, height, autoflush=False)

# Construct the board
for row in range(height):
  game.append([]) # add in a row
  for col in range(width):
    game[row].append(randint(0,5) > 3) # 2/5 chance of starting alive
 
    # Display the game
    if game[row][col]:
      display.plot(col, row, "black")
    else:        
      display.plot(col, row, "white")
 
# Play the game of life
for iteration in range(iterations):
  next_step = deepcopy(game) # copy the game

  # Clear the old iteration from the display
  display.clear()
  
  # Calculate the next iteration of the game
  for row in range(height):
    for col in range(width):
      # Is this cell currently alive?
      living = game[row][col]
 
      # Calculate the number of neighbours living
      # 1 = alive, 0 = dead
      living_neighbours = 0
      # Vertical
      if row+1 < height:
        living_neighbours += game[row+1][col]
      if row-1 >= 0:
        living_neighbours += game[row-1][col]
      # Horizontal
      if col+1 < width:
        living_neighbours += game[row][col+1]
      if col-1 >= 0:
        living_neighbours += game[row][col-1]
      # Diagonal
      if row+1 < height and col+1 < width:
        living_neighbours += game[row+1][col+1]
      if row-1 >= 0 and col+1 < width:
        living_neighbours += game[row-1][col+1]
      if row+1 < height and col-1 >= 0:
        living_neighbours += game[row+1][col-1]
      if row-1 >= 0 and col-1 >= 0:
        living_neighbours += game[row-1][col-1]
 
      # Decide if the cell lives or dies
      if living and ((living_neighbours==2) or (living_neighbours==3)):
        next_step[row][col] = 1 # alive
      elif (not living) and living_neighbours == 3:
        next_step[row][col] = 1 # alive
      else:
        next_step[row][col] = 0 # dead
     
      # Display the game
      if next_step[row][col]:
        display.plot(col, row, "black")
      else:        
        display.plot(col, row, "white")

  # Update the display and show it for a little while
  display.update()
  display.pause(pause_time)
 
  # Update the game
  game = next_step
