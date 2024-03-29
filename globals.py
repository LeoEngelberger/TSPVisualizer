import pygame


class Globals:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Globals, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.main = None
        self.amount_of_vertices = 4

        self.red = (255, 0, 0,1)
        self.blue = (0, 0, 255,1)
        self.green = (0, 255, 0,1)
        self.white = (255,255,255,1)
        self.black = (0,0,0,1)
        self.widget_color = (24,116,165,0.7)
        self.shadow_color = (135,62,35,0)
        self.font_color = (226,135,67,1)
        self.font = pygame.font.Font('GUI/Targa.ttf', 64)
        self.text_font = pygame.font.Font('GUI/Targa.ttf', 21)
        self.shadow_font = pygame.font.Font('GUI/Targa.ttf', 68)
        self.clock = pygame.time.Clock()

        self.main = None
        self.screen_x, self.screen_y = 1440, 960
        self.screen_size = (self.screen_x, self.screen_y)
        self.screen = pygame.display.set_mode(self.screen_size)
        self.menu_is_enabled = True

    def set_main(self, main):
        self.main = main
