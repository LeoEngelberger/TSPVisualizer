import pygame
import sqlite3
import GameObjects.Player as player
import globals
import GameObjects.Vertex as vert


class GameSessionClass:
    def __init__(self, number_of_vertices):
        self.globals = globals.Globals._instance

        self.is_game_complete = False
        self.session_running = False

        # specific vars used only for setting up the map and translating
        # between Planar Pixel Space and Long/Lat coordinate system
        self.lat_range, self.long_range = 47.9 - 45.73, 10.58 - 5.85
        self.bot_most_lat, self.left_most_long = 45.73, 5.85
        self.pixel_per_long_degree = self.globals.screen_x / self.long_range
        self.pixel_per_lat_degree = self.globals.screen_y / self.lat_range

        # GameObjects
        self.Vertices = None    # Places to visit
        self.background = None  # will later be showing Map of Switzerland
        self.amount_of_vertices = number_of_vertices    # How many places a Player can visit defined by menu
        self.player = player.PlayerClass(self)  # handles PlayerInput and Interaction
        # Final Setups pf Objects before Play
        self.setup_screen()     # set up the game Interface
        self.load_in_vertices()
        self.player.set_nodes(self.Vertices)    # Inform the Player about the available Places to visit

        self.session_running = True

    # Load in Map of Switzerland & blit it to the screen surface
    def setup_screen(self):
        self.background = pygame.transform.scale(pygame.image.load("map.png"), self.globals.screen.get_size())
        self.globals.screen.blit(self.background, (0, 0))

    # load in Vertices and place them on the map
    def load_in_vertices(self):
        self.Vertices = pygame.sprite.Group()
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
        else: y=y - 10
        vertex.rect.x, vertex.rect.y = (x, y)
        return x, y


    def update(self, event):

        if self.session_running:
            if self.is_game_complete:
                print("worked")

            else:
                if event.type == pygame.MOUSEBUTTONDOWN:

                    for i, t_Vertex in enumerate(self.Vertices):
                        if t_Vertex.rect.collidepoint(event.pos):
                            t_Vertex.clicked()

        else:
            self.globals.main.switch_screen()

