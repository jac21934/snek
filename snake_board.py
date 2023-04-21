
import numpy as np
import random
from enum import Enum, IntEnum

# Define directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Types of squares
class SnakeSquare(IntEnum):
    SNAKE_HEAD = 1
    SNAKE_BODY = 2
    APPLE = 3


class GameBoard():

    def __init__(self, width, height):

        self.board_width = width
        self.board_height = height

        # initialize start of snake in the middle of the board
        self.snake = [(int(self.board_width/2), int(self.board_height/2))]

        # initialize snake direction
        self.snake_direction = UP

        # intialize 
        self.apple = (None,None)
        self.get_new_apple()


    def get_new_apple(self) -> None:
        # generate random x,y coords that are not in the snake 
        x = random.randint(0, self.board_width - 1)  
        y = random.randint(0, self.board_height - 1)   
        while (x,y) in self.snake:
            x = random.randint(0, self.board_width - 1)  
            y = random.randint(0, self.board_height - 1)      
        
        self.apple = (x,y)


    def get_board(self):

        board = np.zeros((self.board_width, self.board_height), dtype=int)

        # place apple
        board[self.apple[0]][self.apple[1]] = SnakeSquare.APPLE

        # place snake
        board[self.snake[0][0]][self.snake[0][1]] = SnakeSquare.SNAKE_HEAD
        if len(self.snake) > 1:
            for s in self.snake[1:]:
                board[s[0]][s[1]] = SnakeSquare.SNAKE_BODY

        return board
    

    def print_board(self) -> None:
        board = self.get_board()
        for y in range(self.board_height):
            line = ""
            for x in range(self.board_width):
               line += str(board[x][y]) + " "
            print(f'{line}')


    def _tuple_addition(self, dir1, dir2) -> tuple:
        return (dir1[0] + dir2[0], dir1[1] + dir2[1])


    def change_snake_dir(self, new_dir):

        # you can't move backwards in snake, so we can never move in
        # the direct opposite of our current direction
        if self._tuple_addition(self.snake_direction, new_dir) != (0,0):
            self.snake_direction = new_dir


    def step_snake(self) -> bool:
        new_loc = self._tuple_addition(self.snake[0], self.snake_direction)
        
        # check for out of bounds
        if new_loc[0] >= self.board_width or new_loc[0] < 0 \
           or new_loc[1] >= self.board_height or new_loc[1] < 0: 
            return False
        
        # check for self collision
        if new_loc in self.snake:
            return False

        # insert next location at the beginning of the snake array
        # if the snake has moved over the apple, do nothing because the
        # snake has grown, if it hasn't remove the end of the snake
        self.snake.insert(0, new_loc)
        if self.snake[0] == self.apple:
            self.get_new_apple()
        else:
            self.snake.pop()

        # If the snake has moved without dieing, return True
        return True



