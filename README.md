# Binoxxolver

This is a (very basic) python tool to create and solve [Binoxxo](https://en.wikipedia.org/wiki/Takuzu) puzzles, also known as Takuzu or Binairo.

### Usage
generating:
`generator.generate(N, percent_empty)` generates a grid of size (N x N), where `percent_empty` dictates what percentage of squares will be left empty (duh).

solving:
`solver.backtrack(grid)` solves the grid passed to it as argument. It does so in-place and also returns the solved grid.

misc:
`generator.show(grid)` displays a grid on std.out, where `#` is used for empty squares.


### How it works
The grid is represented as a 2D list of integers, where '0' stands for 'O', '1' stands for 'X' and '2' stands for "empty".
At the moment, the generator is very dumb - it starts by solving an empty grid vie backtracking, and then removes squares until enough squares are empty.


### Ideas for improvement
 - A more intelligent generator with a better way to set the difficulty than just increasing the amount of empty squares
 - Different solving methods; even the implemented "dumb" backtracking can easily be improved
 - Maybe even a UI for interactively playing the game yourself!
