from random import sample
from itertools import product

from solver import backtrack
from checker import check


# generates a grid of size N x N. @empty is the percentage of empty squares
def generate(N, percent_empty):
    grid = generate_full(N)
    amt_empty = round(N**2 * percent_empty)

    # generate a tuple (r, c) for every square, then choose amt_empty at random
    empty_squares = sample(list(product(range(N), repeat=2)), k=amt_empty)
    for (r, c) in empty_squares:
        grid[r][c] = 2

    return grid    


# generates a fully solved grid of size N x N
def generate_full(N):
    grid = [[2 for j in range(N)] for i in range(N)]
    backtrack(grid)
    assert check(grid) # should never fail
    return grid


# displays a grid nicely
def show(grid):
    N = len(grid)
    print("    ", end = '')
    for c in range(N):
        print(str(c+1)+"  ", end = '')
    print("\n")

    for r in range(N):
        print(str(r+1) + "   ", end = '')
        row = grid[r]
        for square in row:
            if square == 0:
                print('O', end = '')
            elif square == 1:
                print('X', end = '')
            else:
                print('-', end = '')
            
            print("  ", end = '')
        print("")

