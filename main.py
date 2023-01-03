import pygame
import pygame_menu
from pygame_menu import themes
import MapGenerator2_0
import numpy as np
from mpl_toolkits.basemap import Basemap
import sqlite3
import matplotlib.pyplot as plt

# self.m = Basemap(resolution='h',projection='merc', llcrnrlat=45.73, urcrnrlat=47.9, llcrnrlon=5.85, urcrnrlon=10.58)

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

pygame.init()
screen_x, screen_y = 1920,1080
screen = pygame.display.set_mode((screen_x,screen_y))


class Main_Menu():
    def __init__(self):
        self.font = pygame.font.Font('Targa.ttf', 64)
        self.is_enabled = True
        self.items = [("start game", self.start_game),("set difficulty", self.set_difficulty)]
        self.home_menu = pygame_menu.Menu("Problem des Handelsreisenden", screen_x, screen_y, theme=themes.THEME_SOLARIZED)
        self.home_menu.add.button("Play", self.start_game)
        self.home_menu.add.selector("Difficulty: ", [("Hard", 26), ("Easy",2)], onchange=self.set_difficulty())

    def set_difficulty(self):
        pass

    def start_game(self):
        self.is_enabled = False


class GameSession():
    def __init__(self):
        self.game_running = True
        self.amount_of_vertices = 10

        self.setup_screen()
        self.setup_map()
        #self.main_loop()

    def setup_screen(self):
        self.background = pygame.transform.scale(pygame.image.load("map.png"), screen.get_size())

    def setup_map(self):
        self.left_most_long, self.bot_most_lat = 5.85, 45.73
        self.lat_range = 47.9 - 45.73
        self.long_range = 10.58 - 5.85
        self.pixel_per_long_degree = screen_x / self.long_range
        self.pixel_per_lat_degree = screen_y / self.lat_range
        screen.blit(self.background, (0, 0))
        self.Vertices = pygame.sprite.Group()
        self.load_in_vertices()

    def load_in_vertices(self):
        conn = sqlite3.connect('Locations.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Location")
        Location = cursor.fetchmany(self.amount_of_vertices)
        for place in Location:
            temp_vert = Vertex(red, place[1], place[2], place[3])
            self.Vertices.add(temp_vert)
            screen.blit(temp_vert.image, self.convert_coordinates(temp_vert))
        cursor.close()
        conn.close()

    def convert_coordinates(self, vertex):
        x = ((vertex.long - self.left_most_long) * self.pixel_per_long_degree)
        y = (-1) * (((vertex.lat - self.bot_most_lat) * self.pixel_per_lat_degree) - screen_y)
        if x == screen_x:
            x = x - 10
        else:
            x = x - 5
        if y == screen_y: y = y - 10
        vertex.rect.x, vertex.rect.y = (x,y)
        return x, y

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                print(mouse_pos)
                for i, t_Vertex in enumerate(self.Vertices):
                    if t_Vertex.rect.collidepoint(mouse_pos):
                        print(t_Vertex.name)
                # if event is of type quit then
                # set running bool to false
            if event.type == pygame.QUIT:
                self.game_running = False

            pygame.display.flip()



class Main_Game():
    def __init__(self):
        self.main_menu = Main_Menu()
        self.game_session = None
        self.main_loop()

    def main_loop(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()

                if self.main_menu.is_enabled:
                    self.main_menu.home_menu.update(events)
                    self.main_menu.home_menu.draw(screen)

                else:
                    if not self.game_session:
                        self.game_session = GameSession()
                    self.game_session.update(events)

                pygame.display.update()

class Vertex(pygame.sprite.Sprite):
    def __init__(self, color, name, long, lat):
        super(Vertex, self).__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(color)
        self.name = name
        self.rect = self.image.get_rect()
        self.rect.width, self.rect.height = (30,30)
        self.long, self.lat = long, lat



main_menu = Main_Menu()
game = Main_Game()
