import pygame
import pygame_menu
from pygame_menu import themes

import globals


class BaseUICanvas:
    def __init__(self):
        self.is_enabled = True
        self.items = [("start game", self.start_game), ("set difficulty", self.set_difficulty)]
        self.g = globals.Globals._instance
        self.widgets = {}
        self.screen = self.g.screen
        self.screen_x, self.screen_y = self.g.screen_x, self.g.screen_y
        self.add_widget("test",(40,50),(500,80))

    def set_difficulty(self):
        pass

    def start_game(self):
        self.is_enabled = False

    def update(self, events):
        for name in self.widgets:
            self.widgets[name].update_widget()
        for event in events:
            pass


    def add_widget(self, name, pos, size, background=None):
        self.widgets[name] = Widget(pos, size, name, background)



class Widget(pygame.sprite.Sprite):
    def __init__(self, pos, size, name, background=None):
        super().__init__()
        self.g = globals.Globals._instance
        self.image = pygame.Surface([size[0],size[1]])
        self.pos = pos
        self.text = self.g.font.render("test", True, self.g.green, self.g.blue)
        self.textRect = self.text.get_rect()
        self.textRect.center = self.image.get_rect().center
        if background == None:
            self.image.fill(self.g.red)
        else:
            self.image = background


    def update_widget(self):
        self.g.screen.blit(self.image, self.pos)
        self.g.screen.blit(self.text, self.textRect)


class Button(Widget):
    def __init__(self, func):
        super().__init__()
        self.func = func




