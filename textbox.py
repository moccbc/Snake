import pygame
from utils import *

class TextBox:
    # Center is a (x, y) pair 
    # Colors is a (text_color, upper_color, lower_color) tuple
    # offset_percent is the amount in percentage that you want the 
    # (text, lower_layer, upper_layer) to be offset from the center by
    # The offset is relative to bg_width by default
    def __init__(self, center, colors, offset_percent, text, font, border_radius=0):
        self.center = center
        self.text_color = colors[0]
        self.lower_color = colors[1]
        self.upper_color = colors[2]
        self.text = text
        self.font = font 
        self.label = font.render(self.text, self.text_color, 1)
        self.bg_width = self.label.get_rect().width + self.label.get_rect().width // len(text) * 2
        self.bg_height = self.label.get_rect().height + self.label.get_rect().height*20//100
        self.bg_upper_rect = pygame.Rect(0, 0, self.bg_width, self.bg_height)
        self.bg_lower_rect = pygame.Rect(0, 0, self.bg_width, self.bg_height)
        self.border_radius = border_radius

        # Offsets are relative to bg_width by default
        self.text_offset = (self.bg_width*offset_percent[0][0]//100, self.bg_height*offset_percent[0][1]//100)
        self.lower_offset = (self.bg_width*offset_percent[1][0]//100,self.bg_width*offset_percent[1][1]//100)
        self.upper_offset = (self.bg_width*offset_percent[2][0]//100,self.bg_width*offset_percent[2][1]//100)
    
    def draw(self, window, dynamic_offset=(0,0)):
        # Set the center of the lower layer
        self.bg_lower_rect.center = add_tuples(self.center, self.lower_offset)
        self.bg_lower_rect.center = add_tuples(self.bg_lower_rect.center, dynamic_offset)

        # Set the center of the upper layer
        self.bg_upper_rect.center = add_tuples(self.center, self.upper_offset)
        self.bg_upper_rect.center = add_tuples(self.bg_upper_rect.center, dynamic_offset)

        # Drawing the lower layer
        pygame.draw.rect(window, self.lower_color, self.bg_lower_rect, border_radius = self.border_radius)

        # Drawing the upper layer
        pygame.draw.rect(window, self.upper_color, self.bg_upper_rect, border_radius = self.border_radius)

        # Setting the center of the text
        text_center = add_tuples(self.center, self.upper_offset)
        text_center = add_tuples(text_center, dynamic_offset)
        text_center = add_tuples(text_center, self.text_offset)

        # Drawing the text
        window.blit(self.label, self.label.get_rect(center = text_center))