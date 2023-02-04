import pygame


class Globals:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Globals, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.main = None

        self.red = (255, 0, 0)
        self.blue = (0, 0, 255)
        self.green = (0, 255, 0)
        self.font = pygame.font.Font('Targa.ttf', 64)

        self.main = None
        self.screen_x, self.screen_y = 1440, 960
        self.screen_size = (self.screen_x, self.screen_y)
        self.screen = pygame.display.set_mode(self.screen_size)
        self.menu_is_enabled = True

    def set_main(self, main):
        self.main = main
