import pygame
import os

from globals import *
from game import *
from textbox import *
from utils import *
from button import *

def create_buttons():
    button_font = pygame.font.Font(os.path.join("assets", "fonts", "PolandCannedIntoFuture-OxE3.ttf"), BTN_TEXT_SIZE)
    button_texts = ["START", "HIGHSCORES", "QUIT"]
    button_coord = (WIDTH/2, HEIGHT*60//100)
    colors = (BLACK, DARK_GREY, LIGHT_GREY)
    buttons = []
    offset = 0
    for text in button_texts:
        button_label = button_font.render(text, 1, BLACK)
        dist = (button_label.get_rect().height + button_label.get_rect().height*50//100)
        buttons.append(Button(button_coord, colors, text, button_font))
        button_coord = add_tuples(button_coord, (0, dist))
        offset += 1 
    return buttons[0], buttons[1], buttons[2]

def menu():
    run = True
    clock = pygame.time.Clock()
    dynamic_offset = (0,0)
    increase = True
    ticks = 0
    cool_down = 10 

    # Parameters for the title
    title_font = pygame.font.Font(os.path.join("assets", "fonts", "PolandCannedIntoFuture-OxE3.ttf"), TITLE_WIDTH)
    title_pos = (WIDTH//2, HEIGHT*30//100)
    title_colors = (BLACK, DARK_GREY, LIGHT_GREY)
    title_offset_percents = [(2, 10), (-2, 2), (0,0)]
    title = TextBox(title_pos, title_colors, title_offset_percents, "SNAKE", title_font)

    # Create the buttons
    start_button, high_score_button, quit_button = create_buttons()

    def redraw_window():
        # Draw the background
        WINDOW.fill(NAVY)
        title.draw(WINDOW, dynamic_offset)
        start_button.draw(WINDOW)
        start_button.check_click(game)
        high_score_button.draw(WINDOW)
        high_score_button.check_click(game)
        quit_button.draw(WINDOW)
        quit_button.check_click(quit)
        pygame.display.update()

    while(run):
        clock.tick(FPS)
        redraw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        if ticks == cool_down:
            if increase:
                dynamic_offset = add_tuples(dynamic_offset, (0,1))
            else:
                dynamic_offset = add_tuples(dynamic_offset, (0,-1))
            if dynamic_offset[1] == 0 or dynamic_offset[1] == 5:
                increase = not increase
            ticks = 0
        else:
            ticks += 1
