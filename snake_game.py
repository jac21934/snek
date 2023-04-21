import pygame
from snake_board import GameBoard, SnakeSquare, UP, DOWN, LEFT, RIGHT

# Import pygame.locals for easier access to key coordinates

from pygame.locals import (

    K_UP,

    K_DOWN,

    K_LEFT,

    K_RIGHT,

    K_ESCAPE,

    KEYDOWN,

    QUIT,

)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE = (0, 0, 200)
GREEN = (0, 200, 0)
GREY = (100,100,100)

def drawGrid(width, height, blockSize, screen, grid):
 
    for y in range(0, height, blockSize):
        for x in range(0, width, blockSize):

            x_coord = int(x/blockSize)
            y_coord = int(y/blockSize)
            
            square_color = WHITE 
            
            if grid[x_coord][y_coord] == SnakeSquare.APPLE.value:
                square_color = RED
            elif grid[x_coord][y_coord] == SnakeSquare.SNAKE_HEAD.value:
                square_color = BLUE
            elif grid[x_coord][y_coord] == SnakeSquare.SNAKE_BODY.value:
                square_color = GREY
            else:   
                square_color = WHITE 

            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, square_color, rect, 0)

            pygame.draw.rect(screen, BLACK, rect, 1)


def main():

    # Initialize pygame

    pygame.init()
    pygame.display.set_caption('snek')
    # Define constants for the screen width and height

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    BLOCK_SIZE = 20
    FPS = 10

    BOARD_WIDTH = int(SCREEN_WIDTH/BLOCK_SIZE)
    BOARD_HEIGHT = int(SCREEN_HEIGHT/BLOCK_SIZE)

    game_board = GameBoard(BOARD_WIDTH, BOARD_HEIGHT)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # draw first screen
    board = game_board.get_board()
    drawGrid(int(SCREEN_WIDTH), int(SCREEN_HEIGHT), BLOCK_SIZE, screen, board)
    pygame.display.flip()

    # initialize the timing calc
    last_time = pygame.time.get_ticks()

    running = True

    while running:

        # Handle User Input
        for event in pygame.event.get():
            # Did the user click the window close button?
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game_board.change_snake_dir(LEFT)
                elif event.key == pygame.K_RIGHT:
                    game_board.change_snake_dir(RIGHT)
                elif event.key == pygame.K_UP:
                    game_board.change_snake_dir(UP)
                elif event.key == pygame.K_DOWN:
                    game_board.change_snake_dir(DOWN)

        current_time = pygame.time.get_ticks()
        print(current_time, last_time)
        if current_time - last_time > (1000/FPS): 
            # Update the game
            continueGame = game_board.step_snake()

            # If the snake died, start a new game
            if continueGame == False:
                game_board = GameBoard(BOARD_WIDTH, BOARD_HEIGHT)

            # Update the board based on the new step
            board = game_board.get_board()
            drawGrid(int(SCREEN_WIDTH), int(SCREEN_HEIGHT), BLOCK_SIZE, screen, board)

            # Flip the display
            pygame.display.flip()
            last_time = current_time

    # Exit Loop Due to 

    pygame.quit()



if __name__ == "__main__":
    main()