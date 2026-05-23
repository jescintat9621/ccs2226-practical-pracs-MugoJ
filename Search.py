import random

def create_board(n):
    return [random.randint(0, n - 1) for _ in range(n)]

def count_threats(board):
    threats = 0
    size = len(board)
    for i in range(size):
        for j in range(i + 1, size):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                threats += 1
    return threats

def find_best_move(board):
    best_board = list(board)
    min_threats = count_threats(board)
    size = len(board)
    
    for i in range(size):
        original_position = board[i]
        for j in range(size):
            if j == original_position:
                continue
            board[i] = j
            current_threats = count_threats(board)
            if current_threats < min_threats:
                min_threats = current_threats
                best_board = list(board)
        board[i] = original_position
        
    return best_board, min_threats

def solve_n_queens(n):
    current_board = create_board(n)
    current_threats = count_threats(current_board)
    
    while current_threats > 0:
        next_board, next_threats = find_best_move(current_board)
        if next_threats >= current_threats:
            # We are stuck, restart with a new random board
            current_board = create_board(n)
            current_threats = count_threats(current_board)
        else:
            current_board = next_board
            current_threats = next_threats
            
    return current_board

# Example for an 8x8 board
solution = solve_n_queens(8)
print("Solution found:", solution)