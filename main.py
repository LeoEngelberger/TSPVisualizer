import pygame
import pygame_menu
from pygame_menu import themes
import MapGenerator2_0
import numpy as np
from mpl_toolkits.basemap import Basemap
import sqlite3
import matplotlib.pyplot as plt

import MainMenu as menu
import GameObjects.Player as player
import GameSession as GS
import globals

# self.m = Basemap(resolution='h',projection='merc', llcrnrlat=45.73, urcrnrlat=47.9, llcrnrlon=5.85, urcrnrlon=10.58)
pygame.init()

class MainGame:
    def __init__(self):
        self.globals = globals.Globals()
        self.main_menu = menu.MainMenu()
        self.game_session = None
        self.player = player.PlayerClass()
        self.main_loop()

    def main_loop(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()

                if self.globals.menu_is_enabled:
                    self.main_menu.home_menu.update(events)
                    self.main_menu.home_menu.draw(self.globals.screen)

                else:
                    if not self.game_session:
                        amount_of_vertices = self.main_menu.selector.get_value()[0][1]
                        self.game_session = GS.GameSessionClass(amount_of_vertices, self.player)
                    self.game_session.update(events)

                pygame.display.update()



game = MainGame()
