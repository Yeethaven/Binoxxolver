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

    #check rows
    for row in grid:
         if not checkRow(row): return False

    #check columns
    for i in range(size):
        col = [row[i] for row in grid]
        if not checkRow(col): return False

    return True


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


            if curXs > 2 or curOs > 2:
                 #print("more than 2 in a row!")
                 #print(row)
                 return False 
        
        if finished and amtOs != amtXs:
            #print("amtOs != amtXs")
            #print(row)
            return False
        # if there are more Xs than Os + empties, it's insolvable
        elif amtOs + amt2s < amtXs or amtXs + amt2s < amtOs:
            #print("not enough empties for balance!")
            #print(row)
            return False
        
        return True
