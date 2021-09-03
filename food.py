import pygame
from random import randint
from globals import *

class Food:
    def __init__(self, x, y, radius = TILE_SIZE//3, color = WHITE):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.coords = []
        self.exist = False

    # Get all of the available coordinates on the grid
    def init_coords(self):
        x, y = 2, TILE_SIZE+2
        for row in range(TILE_COUNT):
            y += TILE_SIZE
            for col in range(TILE_COUNT):
                self.coords.append([x + col*TILE_SIZE, y])

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

    # Select a random coord from the list
    def get_next_coords(self):
        idx = randint(0, len(self.coords) - 1)
        return self.coords[idx][0] + TILE_SIZE // 2, self.coords[idx][1] + TILE_SIZE // 2
    
    # Sets the next coordinates for the food
    def set_coords(self):
        self.x, self.y = self.get_next_coords() 

    # Checks if the next placement of the food does not collide with the snake
    def check_valid_placement(self, snake):
        for tile in snake.body:
            tile_x, tile_y = tile.get_coords()
            if (tile_x <= self.x and self.x <= tile_x + TILE_SIZE):
                if (tile_y <= self.y and self.y <= tile_y + TILE_SIZE):
                    return False 
        return True

    def exists(self):
        return self.exist

    def flip_exists(self):
        self.exist = not self.exist

    # Gets the coords of the top-left corner of the tile that the food is in
    def get_coords(self):
        return self.x-TILE_SIZE//2, self.y-TILE_SIZE//2
