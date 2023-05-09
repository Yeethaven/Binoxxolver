from checker import check
from solver import backtrack
from generator import show

def testCheck():
    grid = [[0, 0, 1, 1],
            [0, 1, 1, 0],
            [1, 0, 0, 1],
            [1, 1, 0, 0]]
    
    assert(check(grid))

    grid = [[1, 0, 1, 1, 0, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [0, 0, 1, 0, 1, 0, 1, 0, 1, 1],
            [1, 0, 0, 1, 1, 0, 1, 1, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
            [1, 0, 1, 0, 1, 1, 0, 1, 0, 0],
            [1, 1, 0, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 1, 1, 0, 0, 1, 0, 1, 1],
            [1, 1, 0, 0, 1, 1, 0, 1, 0, 0],
            [0, 1, 1, 0, 0, 1, 0, 1, 0, 1]]
    
    assert(check(grid))

    grid = [[1, 0, 1, 1, 0, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [0, 0, 1, 0, 1, 0, 1, 0, 1, 1],
            [1, 0, 0, 1, 1, 0, 1, 1, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
            [1, 0, 1, 0, 1, 1, 0, 1, 0, 0],
            [1, 1, 0, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 1, 1, 0, 0, 1, 0, 1, 1],
            [1, 1, 0, 0, 1, 1, 0, 1, 0, 0],
            [1, 1, 0, 0, 1, 1, 0, 1, 0, 1]]
    
    assert(not check(grid))

def testBacktrack():
    grid = [[0, 0, 1, 1],
            [0, 1, 2, 0],
            [1, 0, 2, 1],
            [1, 1, 0, 0]]
    sol =  [[0, 0, 1, 1],
            [0, 1, 1, 0],
            [1, 0, 0, 1],
            [1, 1, 0, 0]]
    assert backtrack(grid) == sol
    

    grid = [[2, 2, 0, 2, 2, 2],
            [2, 0, 1, 1, 0, 2],
            [1, 1, 0, 2, 2, 2],
            [2, 0, 2, 2, 1, 0],
            [2, 2, 1, 0, 0, 1],
            [0, 2, 2, 0, 2, 0]]

    sol = [[1, 0, 0, 1, 0, 1],
            [0, 0, 1, 1, 0, 1],
            [1, 1, 0, 0, 1, 0],
            [1, 0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0, 1],
            [0, 1, 1, 0, 1, 0]]
    
    assert backtrack(grid) == sol

def test_error():
    grid = [[1, 2, 2, 2, 2, 2, 2, 0],
            [0, 2, 0, 2, 2, 2, 1, 2],
            [0, 1, 1, 0, 0, 1, 0, 1],
            [1, 0, 2, 2, 2, 2, 2, 0],
            [1, 1, 2, 2, 1, 2, 2, 2],
            [0, 1, 0, 1, 0, 0, 1, 1],
            [1, 0, 1, 0, 1, 1, 0, 0],
            [0, 1, 2, 2, 0, 1, 2, 2]]
    
    show(grid)
    print("check: " + str(check(grid)))


def main():
    test_error();



if __name__ == "__main__":
    main()