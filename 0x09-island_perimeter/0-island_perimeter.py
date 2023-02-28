#!/usr/bin/python3
"""Island perimeter computing module"""


def island_perimeter(grid):
    """
    Computes the perimeter of the island described in `grid`.
    """
    height = len(grid)
    width = len(grid[0])
    perimeter = 0
    for row in range(height):
        for col in range(width):
            if grid[row][col] == 1:
                num_neighbors = 0
                if row == 0 or grid[row-1][col] == 0:
                    num_neighbors += 1
                if row == height-1 or grid[row+1][col] == 0:
                    num_neighbors += 1
                if col == 0 or grid[row][col-1] == 0:
                    num_neighbors += 1
                if col == width-1 or grid[row][col+1] == 0:
                    num_neighbors += 1
                perimeter += num_neighbors
    return perimeter
