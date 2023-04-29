from random import sample

# "dumb" backtracking
def backtrack(grid):
    assert grid is not None # if this fails, something has gone wrong

    empty = findEmpty(grid)
    if empty is None:
        return grid
    (r, c) = empty

    # randomization for a bit more "creativity"
    for val in sample([0, 1], 2):
        # apply candidate
        grid[r][c] = val
        # check candidate
        if not check(grid):
            grid[r][c] = 2
            continue
        
        solution = backtrack(grid)
        if solution is not None:
            return solution
        
        grid[r][c] = 2


    return None
 

# finds the next empty square and returns it as (row, col) tuple
def findEmpty(grid):
    size = len(grid)
    for r in range(size):
        for c in range(size):
            if grid[r][c] == 2:
                return (r, c)
    
    return None

# checks if a grid is still solvable
def check(grid):
    size = len(grid)

    # check rows
    for row in grid:
         if not checkRow(row): return False

    # check columns
    for i in range(size):
        col = [row[i] for row in grid]
        if not checkRow(col): return False

    return True

# checks if a row is still solvable
def checkRow(row):
        curXs, curOs, amtXs, amtOs, amt2s = 0, 0, 0, 0, 0
        finished = True
        for square in row:
            if (square == 1):
                amtXs += 1
                curXs += 1
                curOs = 0
            elif (square == 0):
                amtOs += 1
                curOs += 1
                curXs = 0
            else:
                amt2s += 1
                curOs = 0
                curXs = 0
                finished = False

            # more than 2 in a row
            if curXs > 2 or curOs > 2:
                 return False 
        
        if finished and amtOs != amtXs:
            return False
        
        # if there are more Xs than Os + empties, it's insolvable
        elif amtOs + amt2s < amtXs or amtXs + amt2s < amtOs:
            return False
        
        return True


def solve_doubles(grid):
    #TODO
    return


# human-like solving: checking for doubles
def step_doubles(grid):
    # TODO: findEmpty will always return the first empty square,
    #       so if it can't be filled step_doubles will always attempt
    #       to fill the same square
    square = findEmpty(grid)
    if square is None:
        return True
    
    return doubles(square)


# checks a square for adjacent doubles
# returns the number it set the square to, or None if it can't find doubles
def doubles(square, grid):
    size = len(grid)
    (r, c) = square
    row = grid[r]

    # check the previous entries in the row
    if c >= 2:
        prev2, prev1 = row[c-2], row[c-1]
        if prev1 == prev2 and not prev1 == 2:
            grid[r][c] = 1 - prev1
            return 1 - prev1
    
    # check the following entries in the row
    if c <= size - 2:
        next2, next1 = row[c+2], row[c+1]
        if next1 == next2 and not next1 == 2:
            grid[r][c] = 1 - next1
            return 1 - next1


    col = [cur_row[c] for cur_row in grid]

    # check the previous entries in the column
    if r >= 2:
        prev2, prev1 = col[r-2], col[r-1]
        if prev1 == prev2 and not prev1 == 2:
            grid[r][c] = 1 - prev1
            return 1 - prev1
    
    # check the following entries in the column
    if r <= size - 2:
        next2, next1 = col[r+2], col[r+1]
        if next1 == next2 and not next1 == 2:
            grid[r][c] = 1 - next1
            return 1 - next1

    return None