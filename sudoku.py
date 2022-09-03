def find_next_empty(puzzle):
    # find the next row, col on the puzzle that's not filled yet -> replace with -1
    # return row, col tuple (or (None, None), if there is none)

    # keep in mind that we are using 0-8 for our indices
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    
    return None, None # if no spaces in the puzzle are empty (-1)

def is_valid(puzzle, guess, row, col):
    # figure out whether the guess at the row/col of the puzzle is a valid guess
    # return True if valid, False otherwise

    # let's start with the row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # now the col
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # and then the square
    # this is tricky, but we want to get where the 3x3 square starts
    # and iterate over the 3 values in the row/col
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    # if we get here, these checks pass
    return True

def solve_sudoku(puzzle):
    # solve sudoku using backtracking
    # our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # rturn whether a solution exists
    # mutates puzzle to be the solution (if solution exists)

    # step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # step 1.1: if there's nowhere left, then we're done because we only allowed valid inputs
    if row is None:
        return None

    # step 2: if there is a place to put a number, then make a guess between 1 and 9
    for guess in range(1, 10):
        # step 3: check if this is valid guess
        if is_valid(puzzle, guess, row, col):
            # step 3.1: if this is valid, then place that guess on the puzzle
            puzzle[row][col] = guess

            # now recurse using this puzzle
            # step 4: recursively call our function
            if solve_sudoku(puzzle):
                return True

        # step 5: if not valid or if our guess does not solve the puzzle,
        # then we need to backtrack and try new number
        puzzle[row][col] = -1 # reset the guess

    # step 6: if none of the numbers that we try work,
    # then this puzle is unsolvable
    return False

if __name__ == "__main__":
    example_board = [
        [],
        [],
        [],
        
        [],
        [],
        [],
        
        [],
        [],
        []
    ]

    print(solve_sudoku(example_board))
    print(example_board)