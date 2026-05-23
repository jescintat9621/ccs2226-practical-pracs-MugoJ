import pygame
import sys

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WIDTH = 640
HEIGHT = 640

def draw_board(screen, board):
    n = len(board)
    square_size = WIDTH // n

    for row in range(n):
        for col in range(n):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * square_size, row * square_size, square_size, square_size))
            
            if board[col] == row:
                pygame.draw.circle(screen, RED, (col * square_size + square_size // 2, row * square_size + square_size // 2), square_size // 3)

def visualize_solution(board):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("N-Queens Visualization")
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(WHITE)
        draw_board(screen, board)
        pygame.display.flip()
        
    pygame.quit()
    sys.exit()

# Example: Using the solution we found earlier
example_board = [1, 3, 5, 7, 2, 0, 6, 4]
visualize_solution(example_board)