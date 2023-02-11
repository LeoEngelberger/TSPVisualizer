import pygame

import MainMenu
import globals

import MenuSrc.Menu as menu
import GameObjects.Player as player
import GameSession as GS

# self.m = Basemap(resolution='h',projection='merc', llcrnrlat=45.73, urcrnrlat=47.9, llcrnrlon=5.85, urcrnrlon=10.58)
pygame.init()

class MainGame:
    def __init__(self):
        self.globals = globals.Globals()
        self.globals.set_main(self)
        self.main_menu = MainMenu.MainMenu()
        self.game_session = None
        self.main_loop()

    def main_loop(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()

                elif self.globals.menu_is_enabled:
                    self.main_menu.main_component.update(event)

                else:
                    self.game_session.update(event)

            pygame.display.update()
            self.globals.clock.tick(60)

    def start_game_function(self, amount_of_vertices):
        self.globals.amount_of_vertices = amount_of_vertices
        self.switch_screen()

    def switch_screen(self):
        if not self.game_session:
            self.globals.menu_is_enabled = False
            del self.main_menu
            self.main_menu = None
            self.game_session = GS.GameSessionClass(self.globals.amount_of_vertices)

        else:
            del self.game_session
            self.game_session = None
            self.globals.menu_is_enabled = True
            self.main_menu = MainMenu.MainMenu()

        pygame.display.update()







game = MainGame()
