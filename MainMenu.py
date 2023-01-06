import pygame
import pygame_menu
from pygame_menu import themes

class MainMenu:
    def __init__(self, screen_x, screen_y):
        self.screen_x, self.screen_y = screen_x, screen_y
        self.font = pygame.font.Font('Targa.ttf', 64)
        self.is_enabled = True
        self.items = [("start game", self.start_game), ("set difficulty", self.set_difficulty)]
        self.home_menu = pygame_menu.Menu("Problem des Handelsreisenden", screen_x, screen_y,
                                          theme=themes.THEME_SOLARIZED)
        self.home_menu.add.button("Play", self.start_game)
        self.selector = self.home_menu.add.selector("Difficulty: ", [("Hard", 10), ("Easy", 3)],
                                                    onchange=self.set_difficulty())

    def set_difficulty(self):
        pass

    def start_game(self):
        self.is_enabled = False

