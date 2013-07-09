import copy
import graphics

number_of_iterations = 100
display_pause_time = 100

grid = [[1,0,0,1,1,0,0,1,1,1,0,0,1,0,0,1,1,0,0,1],[0,0,1,1,0,0,0,0,1,0,0,0,0,0,0,1,0,1,1,0],[0,0,1,1,0,0,1,1,0,0,0,0,0,1,0,1,0,1,0,1],[0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,1,0,1,0,0],[0,1,0,0,0,1,1,0,1,1,1,0,1,1,1,0,0,1,1,1],[0,0,0,0,1,0,0,0,1,1,0,0,0,1,0,1,0,1,1,1],[0,0,1,1,1,0,1,0,0,0,1,1,1,0,0,0,0,1,1,1],[0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,1,1,0,0,0],[1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,0],[1,1,0,1,1,0,0,0,0,1,0,0,0,0,1,0,1,1,0,0],[1,0,1,1,0,0,0,0,1,0,1,0,1,1,0,0,1,1,1,0],[1,0,1,1,0,0,0,1,1,0,0,1,0,0,1,0,0,0,0,1],[1,1,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,1,1,0],[0,0,0,0,0,1,1,0,0,1,0,1,0,0,0,0,1,1,0,0],[1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0]]

display = graphics.SimpleDisplay("2D Cellular Automaton", len(grid[0]), len(grid), autoflush=False)

# For each iteration...
for iteration in range(number_of_iterations):
    # Keep a copy of the previous iteration
    previous_grid = copy.deepcopy(grid)
    
    # For each cell in the grid...
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            cell = grid[row][column]

            # Display the cells
            if cell == 1:
                display.plot(column, row, "black")
            else:
                display.plot(column, row, "white")

            # Count the number of living neighbours in the previous_grid
            living_neighbours = 0
            for r in [row-1, row, row+1]:
                for c in [column-1, column, column+1]:
                    # Check the neighbours are in bounds and are not the cell itself
                    if r > 0 and r < len(grid) and \
                       c > 0 and c < len(grid[0]) and \
                       not(r is row and c is column):
                        neighbour = previous_grid[r][c]
                        if neighbour == 1:
                            living_neighbours += 1

            # Update the state of the cell
            if cell == 1:
                if living_neighbours == 2 or living_neighbours == 3:
                    grid[row][column] = 1
                else:
                    grid[row][column] = 0
            else:
                if living_neighbours == 3:
                    grid[row][column] = 1
                else:
                    grid[row][column] = 0

    display.update()
    display.pause(display_pause_time)
    
display.begin()
