import pygame
import MapGenerator2_0
import numpy as np
from mpl_toolkits.basemap import Basemap
import sqlite3
import matplotlib.pyplot as plt
#self.m = Basemap(resolution='h',projection='merc', llcrnrlat=45.73, urcrnrlat=47.9, llcrnrlon=5.85, urcrnrlon=10.58)

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
        self.left_most_long, self.bot_most_lat = 5.85,45.73
        self.lat_range = 47.9-45.73
        self.long_range = 10.58-5.85
        self.pixel_per_long_degree = self.screen_x / self.long_range
        self.pixel_per_lat_degree = self.screen_y / self.lat_range
        self.screen.blit(self.background, (0,0))
        self.testVertex2 = Vertex(100,100,blue,5.85,45.73)
        self.testVertex = Vertex(10,10,red,8.539183,47.36865)
        self.screen.blit(self.testVertex2.image, self.convert_coordinates(self.testVertex2))
        self.screen.blit(self.testVertex.image, self.convert_coordinates(self.testVertex))

        self.main_loop()

    def convert_coordinates(self,vertex):
        x = ((vertex.long - self.left_most_long) * self.pixel_per_long_degree)
        y = (-1)*(((vertex.lat - self.bot_most_lat) * self.pixel_per_lat_degree) - self.screen_y)
        if x == self.screen_x: x = x-10
        else: x = x-5
        if y == self.screen_y: y = y - 10
        return x,y
    def main_loop(self):
        while self.game_running:
            for event in pygame.event.get():

                # if event is of type quit then
                # set running bool to false
                if event.type == pygame.QUIT:
                    self.game_running = False
            pygame.display.flip()

class Vertex(pygame.sprite.Sprite):
    def __init__(self,width,height,color,long,lat):
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.long, self.lat = long, lat





game = MainGame()
