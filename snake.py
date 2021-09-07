import pygame
import copy
from globals import *

class SnakeTile:
    def __init__(self, x, y, color, dir):
        self.x = x
        self.y = y
        self.color = color
        self.dir = dir

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, TILE_SIZE, TILE_SIZE))

    # Sets the next position of the tile
    def move(self):
        if self.dir == "right":
            self.x += TILE_SIZE
        elif self.dir == "left":
            self.x -= TILE_SIZE
        elif self.dir == "up":
            self.y -= TILE_SIZE
        elif self.dir == "down":
            self.y += TILE_SIZE

    def get_coords(self):
        return self.x, self.y

class Snake:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.body = [SnakeTile(start_x, start_y, RED, "right")]
        self.bodyPrev = []
        self.cool_down = 10 
        self.timer = self.cool_down 

    # Sets the direction of the head of the snake
    def change_dir(self, dir):
        self.body[0].dir = dir

    # Sets the next direction of the rest of the tiles in the snake
    def propagate_dir_change(self):
        for i in range(len(self.body)-1, 0, -1):
            self.body[i].dir = self.body[i-1].dir

    # Draws the snake on to the window
    def draw(self, window):
        for tile in self.body:
            tile.draw(window)

    # Draws the snake in the previous position on to the window
    def drawPrev(self, window):
        for tile in self.bodyPrev:
            tile.draw(window)

    # Sets the next x, y positions that the tiles should be at
    def move(self):
        # Saving the old body for when the player loses
        self.bodyPrev = copy.deepcopy(self.body)
        for tile in self.body:
            tile.move()
        if len(self.body) > 1:
            self.propagate_dir_change()

    # Adds a tile to the end of the snake in the opposite direction
    # that the last tile of the snake is moving
    def add_tile(self):
        last_tile = self.body[len(self.body)-1]
        x, y = last_tile.x, last_tile.y
        if last_tile.dir == "right":
            x -= TILE_SIZE
        elif last_tile.dir == "left":
            x += TILE_SIZE
        elif last_tile.dir == "up":
            y += TILE_SIZE
        elif last_tile.dir == "down":
            y -= TILE_SIZE
        self.body.append(SnakeTile(x, y, WHITE, last_tile.dir))

    def get_coords(self):
        return self.body[0].get_coords()

    # Checks to see if the head of the snake collided with the body
    def body_collision(self):
        if len(self.body) > 1:
            for tile in self.body[1:]:
                if self.body[0].get_coords() == tile.get_coords():
                    # print("Collided with own body!")
                    return True
        return False

    # Checks to see if the head of the snake collided with any of the walls
    def wall_collision(self):
        head_x, head_y = self.body[0].get_coords() 
        if (head_x < 2 or head_x + TILE_SIZE > WIDTH - 2):
            # print("Collided with left or right wall!")
            return True
        if (head_y < 2 * TILE_SIZE + 1 or head_y + TILE_SIZE > HEIGHT-2):
            # print("Collided with top or bottom wall!")
            return True
        return False

    def collision(self):
        return self.body_collision() or self.wall_collision()

    # Resets the snake to the original
    def reset(self):
        self.body.clear()
        self.bodyPrev.clear()
        self.timer = self.cool_down
        self.body.append(SnakeTile(self.start_x, self.start_y, RED, "right"))