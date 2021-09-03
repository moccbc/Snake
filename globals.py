import pygame

# Global Variables
TILE_COUNT = 20 

# The value for WIDTH should satisfy 
# (WIDTH - 4) % TILE_COUNT == 0
# This is to make the tiles evenly aligned on the screen
WIDTH = 904
TILE_SIZE = (WIDTH-4)//TILE_COUNT
HEIGHT = TILE_SIZE * 2 + WIDTH
TITLE_WIDTH = WIDTH*20 // 100
TITLE_HEIGHT = HEIGHT*10 // 100
BTN_TEXT_SIZE = WIDTH*9 // 100

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
NAVY = (39, 53, 91)
LIGHT_NAVY = (109, 126, 174)
RED = (255, 0, 0)
LIGHT_GREY = (176, 176, 176)
DARK_GREY = (80, 80, 80)

FPS = 60 

# Window
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))