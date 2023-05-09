from os import system
from numpy import copy

from generator import generate, show
from solver import backtrack
from checker import check as check_finished


def put(grid, r, c, val):
    valNum = 2
    if val == 'X' or val == 'x':
        valNum = 1
    elif val == 'O' or val == 'o' or val == '0':
        valNum = 0
    else: return False

    if grid[r][c] == 2:
        grid[r][c] = valNum
        return True
    
    return False

def unput(grid, r, c):
    grid[r][c] = 2

def check_solvable(grid):
    grid_copy = copy(grid)
    if backtrack(grid_copy) is None:
        return False
    
    return True

def process_input(input_str):
    # This function processes the input and returns a result
    input_list = input_str.split(' ')
    try:
        r = int(input_list[0])
        c = int(input_list[1])
        val = input_list[2]
    except:
        print("Invalid input!")
        return None
    result = (r-1, c-1, val)
    return result


def game(N, p_empty, lifes):
    grid = generate(N, p_empty)

    while not lifes == 0:
        if(check_finished(grid)):
            system('clear')
            show(grid)
            print("You won! :)")
            return
        
        system('clear')
        show(grid)
        print("\nRemaining lifes: "+str(lifes))

        input_str = input("\nPlease enter input in the form of 'row col val': ")
        input_processed = process_input(input_str)
        if input_processed is None:
            continue

        (r, c, val) = input_processed
        if not put(grid, r, c, val):
            print("Error: One or more illegal inputs!")
        
        if check_solvable(grid) is False:
            lifes -= 1
            print("Wrong! Remaining lifes: "+str(lifes))
            unput(grid, r, c)
        
    
    print("You lost...")



if __name__ == "__main__":
    game(8, 0.4, 3)