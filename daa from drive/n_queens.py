# Function to print the board
def print_board(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()
    print()

# Function to check if placing a queen is safe
def is_safe(board, row, col):
    n = len(board)
    
    # Check this column on upper side
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

# Recursive function to solve N-Queens
def solve_nqueens(board, row):
    n = len(board)
    if row >= n:
        print("Final N-Queens solution:")
        print_board(board)
        return True

    for col in range(n):
        if board[row][col] == 0 and is_safe(board, row, col):
            board[row][col] = 1
            if solve_nqueens(board, row + 1):
                return True
            board[row][col] = 0  # backtrack

    return False

# Main program
if __name__ == "__main__":
    n = int(input("Enter the size of the chessboard (n): "))
    board = [[0 for _ in range(n)] for _ in range(n)]

    # Take position of the first queen
    row1 = int(input("Enter row position of first Queen (0-indexed): "))
    col1 = int(input("Enter column position of first Queen (0-indexed): "))
    board[row1][col1] = 1

    # Start solving from the next row
    if not solve_nqueens(board, row1 + 1):
        print("No solution exists for this configuration.")
