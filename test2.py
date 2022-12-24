import pygame
import MapGenerator2_0
import numpy as np
from mpl_toolkits.basemap import Basemap
import sqlite3
import matplotlib.pyplot as plt



class MainGame():
    def __init__(self):
        self.window_divider = 5
        pygame.init()
        self.screen = pygame.display.set_mode((1920, 1080))
        self.screen_x, self.screen_y = self.screen.get_size()
        self.game_window_size = (self.screen_x/self.window_divider*4,self.screen_y/self.window_divider*4)

        self.game_session_surface= pygame.Surface((self.screen_x/5,self.screen_y))
        self.game_session_surface= self.game_session_surface.convert()
        self.game_session_surface.fill((0,0,250))
        self.screen.blit(self.game_session_surface,(0,0))

        self.game_surface = pygame.Surface(self.game_window_size)
        self.game_surface = self.game_surface.convert()
        self.game_surface = pygame.transform.scale(pygame.image.load("map.png"), self.game_window_size)
        self.screen.blit(self.game_surface, (self.screen_x/self.window_divider,0))

        test_vertex = Vertex((255,255,255),100,100)
        self.game_session_surface.blit(test_vertex.image,test_vertex.rect)
        pygame.display.flip()

        self.ui_surface = pygame.Surface((self.screen_x, self.screen_y / 5))
        self.ui_surface = self.ui_surface.convert()
        self.ui_surface.fill((0,250,0))
        self.screen.blit(self.ui_surface, (0,(self.screen_y / 5) * 4))


        pygame.display.flip()
        self.game_running = True
        self.main_loop()

    def main_loop(self):
        while self.game_running:
            for event in pygame.event.get():

                # if event is of type quit then
                # set running bool to false
                if event.type == pygame.QUIT:
                    self.game_running = False
            pygame.display.flip()


class Vertices(pygame.sprite.Group):
    def __init__(self):
        pass

class Vertex(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()


    def get_img_pos(self):
        pass

game = MainGame()
