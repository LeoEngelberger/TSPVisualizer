import pygame
import sqlite3
import GameObjects.Player as player
import globals
import GameObjects.Vertex as vert


class GameSessionClass:
    def __init__(self, number_of_vertices, player):
        self.Vertices = None
        self.pixel_per_lat_degree = None
        self.pixel_per_long_degree = None
        self.long_range = None
        self.lat_range = None
        self.bot_most_lat = None
        self.left_most_long = None
        self.background = None
        self.game_running = True
        self.globals = globals.Globals._instance
        self.amount_of_vertices = number_of_vertices

        self.player = player
        self.setup_screen()
        self.setup_map()
        self.player.set_nodes(self.Vertices)

    def setup_screen(self):
        self.background = pygame.transform.scale(pygame.image.load("map.png"), self.globals.screen.get_size())

    def setup_map(self):
        self.left_most_long, self.bot_most_lat = 5.85, 45.73
        self.lat_range = 47.9 - 45.73
        self.long_range = 10.58 - 5.85
        self.pixel_per_long_degree = self.globals.screen_x / self.long_range
        self.pixel_per_lat_degree = self.globals.screen_y / self.lat_range
        self.globals.screen.blit(self.background, (0, 0))
        self.Vertices = pygame.sprite.Group()
        self.load_in_vertices()

    def load_in_vertices(self):
        conn = sqlite3.connect('Locations.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Location")
        Location = cursor.fetchmany(self.amount_of_vertices)
        for place in Location:
            temp_vert = vert.Vertex(self.globals.red, place[1], place[2], place[3], self.player)
            self.Vertices.add(temp_vert)
            self.globals.screen.blit(temp_vert.image, self.convert_coordinates(temp_vert))
        cursor.close()
        conn.close()

    def convert_coordinates(self, vertex):
        x = ((vertex.long - self.left_most_long) * self.pixel_per_long_degree)
        y = (-1) * (((vertex.lat - self.bot_most_lat) * self.pixel_per_lat_degree) - self.globals.screen_y)
        if x == self.globals.screen_x:
            x = x - 10
        else:
            x = x - 5
        if y == self.globals.screen_y: y = y - 10
        vertex.rect.x, vertex.rect.y = (x, y)
        return x, y

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                print(mouse_pos)
                for i, t_Vertex in enumerate(self.Vertices):
                    if t_Vertex.rect.collidepoint(mouse_pos):
                        t_Vertex.clicked()
                # if event is of type quit then
                # set running bool to false
            if event.type == pygame.QUIT:
                self.game_running = False

