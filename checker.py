

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
        curXs, curOs, amtXs, amtOs = 0, 0, 0, 0
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
                print("empty square!")
                return False #empty  square

            if curXs > 2 or curOs > 2:
                 #more than 2 in a row
                 print("more than 2 in a row!")
                 return False 
        
        if amtOs != amtXs:
             print("inequality!")
             return False
        
        return True
