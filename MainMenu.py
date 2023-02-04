import pygame
import pygame_menu
from pygame_menu import themes
import globals

class MainMenu:
    def __init__(self):
        self.g = globals.Globals._instance

        self.font = self.g.font
        self.items = [("start game", self.start_game), ("set difficulty", self.set_difficulty)]
        self.home_menu = pygame_menu.Menu("Problem des Handelsreisenden", self.g.screen_x, self.g.screen_y,
                                          theme=themes.THEME_SOLARIZED)
        self.home_menu.add.button("Play", self.start_game)
        self.selector = self.home_menu.add.selector("Difficulty: ", [("Hard", 10), ("Easy", 3)],
                                                    onchange=self.set_difficulty())

    def external_update(self, events):
        self.home_menu.update(events)
        if self.g.menu_is_enabled:
            self.home_menu.draw(self.g.screen)


    def set_difficulty(self):
        pass

    def start_game(self):
        self.g.main.switch_screen()

