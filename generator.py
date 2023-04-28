from random import randint

from solver import backtrack
from checker import check


# generates a grid of size N x N. @empty is the percentage of empty squares
def generate(N, percent_empty):
    grid = generate_full(N)
    empties = round(N**2 * percent_empty)

    # randomly delete squares
    # TODO: this is pretty inefficient; for high empty values the loop could go on and on...
    for _ in range (empties):
        r, c = randint(0, N-1), randint(0, N-1)
        if not grid[r][c] == 2:
            grid[r][c] = 2
        else:
            empties += 1;

    return grid


# generates a fully solved grid of size N x N
def generate_full(N):
    grid = [[2 for j in range(N)] for i in range(N)]
    backtrack(grid)
    assert check(grid) # should never fail
    return grid


# displays a grid nicely
def show(grid):
    for row in grid:
        for square in row:
            if square == 0:
                print('O', end = '')
            elif square == 1:
                print('X', end = '')
            else:
                print('#', end = '')
            
            print("  ", end = '')
        print("")

