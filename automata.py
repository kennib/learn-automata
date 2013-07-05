import copy
import graphics

number_of_iterations = 10
display_pause_time = 1000

grid = [[1,0,0,1,1,0,0,1,1,1,0,0,1,0,0,1,1,0,0,1],[0,0,1,1,0,0,0,0,1,0,0,0,0,0,0,1,0,1,1,0],[0,0,1,1,0,0,1,1,0,0,0,0,0,1,0,1,0,1,0,1],[0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,1,0,1,0,0],[0,1,0,0,0,1,1,0,1,1,1,0,1,1,1,0,0,1,1,1],[0,0,0,0,1,0,0,0,1,1,0,0,0,1,0,1,0,1,1,1],[0,0,1,1,1,0,1,0,0,0,1,1,1,0,0,0,0,1,1,1],[0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,1,1,0,0,0],[1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,0],[1,1,0,1,1,0,0,0,0,1,0,0,0,0,1,0,1,1,0,0],[1,0,1,1,0,0,0,0,1,0,1,0,1,1,0,0,1,1,1,0],[1,0,1,1,0,0,0,1,1,0,0,1,0,0,1,0,0,0,0,1],[1,1,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,1,1,0],[0,0,0,0,0,1,1,0,0,1,0,1,0,0,0,0,1,1,0,0],[1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0]]

display = graphics.SimpleDisplay("2D Cellular Automaton", len(grid[0]), len(grid), scale=30)

alive = 1
dead = 0

# For each iteration...
for iteration in range(number_of_iterations):

  # Keep a copy of the previous iteration
  previous_grid = copy.deepcopy(grid)

  # For each cell in the grid...
  for row, row_of_cells in enumerate(grid):
    for column, cell in enumerate(row_of_cells):
        
      # Display the cell
      if cell is alive:
        display.plot(column, row, "black")
      else:
        display.plot(column, row, "white")

      # Count the number of living neighbours
      living_neighbours = 0
      for r in [row-1, row, row+1]:
        for c in [column-1, column, column+1]:
          if r > 0 and r < len(grid) and \
             c > 0 and c < len(grid[0]) and \
             not(r is row and c is column):
            neighbour = previous_grid[r][c]
            if neighbour is alive:
                living_neighbours += 1

      # Determine if the cell is living or dead in this iteration
      if cell is alive:
        if living_neighbours is 2 or living_neighbours is 3:
          grid[row][column] = alive
        else:
          grid[row][column] = dead
      else:
        if living_neighbours is 3:
          grid[row][column] = alive
        else:
          grid[row][column] = dead

  
  display.pause(display_pause_time)
