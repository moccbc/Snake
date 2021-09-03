from textbox import *

class Button(TextBox):
    def __init__(self, center, colors, text, font):
        super().__init__(center, colors, [(2, 10), (0, 2), (0,0)], text, font, 2)
        self.pressed = False
        self.lower_offset = (0, self.bg_height*10//100)

    def check_click(self, func):
        mouse_pos = pygame.mouse.get_pos()
        if self.bg_upper_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
                self.upper_offset = self.lower_offset
            else:
                if self.pressed:
                    func()
                    self.pressed = False
                    self.upper_offset = (0,0)
