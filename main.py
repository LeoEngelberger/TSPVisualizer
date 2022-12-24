import pygame
import MapGenerator2_0
import numpy as np
from mpl_toolkits.basemap import Basemap
import sqlite3
import matplotlib.pyplot as plt

red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)

class MainGame():
    def __init__(self):
        self.game_running = True
        self.window_divider = 5
        pygame.init()
        self.screen = pygame.display.set_mode((1920, 1080))
        self.screen_x, self.screen_y = self.screen.get_size()

        self.background = pygame.transform.scale(pygame.image.load("map.png"), self.screen.get_size())
        self.screen.blit(self.background, (0,0))

        self.main_loop()


    def main_loop(self):
        while self.game_running:
            for event in pygame.event.get():

                # if event is of type quit then
                # set running bool to false
                if event.type == pygame.QUIT:
                    self.game_running = False
            pygame.display.flip()




game = MainGame()
