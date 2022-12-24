
import pygame
import numpy as np
from mpl_toolkits.basemap import Basemap
import sqlite3
import matplotlib.pyplot as plt

class main_game():
    def __init__(self):
        self.x_screen_size = 1080
        self.y_screen_size = 1000
        self.font = None
        self.setup()
        self.main_loop()


    def setup(self):
        pygame.init()
        self.font = pygame.font.Font("Targa.ttf", 32)
        self.screen = pygame.display.set_mode((self.x_screen_size,self.y_screen_size))
        pygame.display.set_caption('TSP')
        self.MapGen = Map_Generator(2)
        self.map_setup()
        self.setup_GameSession()

    def setup_GameSession(self):
        txt_nr_o_vert = self.font.render("amount of vertices", True, (0,0,0))
        self.screen.blit(txt_nr_o_vert, (50, 50))
        pass

    def map_setup(self):
        # get the default size


        map_img = pygame.image.load("map.png")
        map_img = pygame.transform.scale(map_img, (self.x_screen_size, self.y_screen_size))
        self.mapSprite = Map(map_img,0,0)
        self.mapSprite.draw(self.screen)
        pygame.display.flip()

        #x_map_pos = (self.x_screen_size/2) - (swiss_map_img.get_size()[0]/2)


    def main_loop(self):
        running = True
        while running:
            # Check for event if user has pushed
            # any event in queue
            for event in pygame.event.get():

                # if event is of type quit then
                # set running bool to false
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.flip()

class Map(pygame.sprite.Sprite):
    def __init__(self, image, x,y, rect=None):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def update(self):
        # Update the sprite's position or other attributes here
        pass

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class GameSession():
    def __init__(self):
        self.current_path_length =0;

class Vertex(pygame.sprite.Sprite):
    def __init__(self, lat, long):
        super().__init__()
        self.color = (255, 0, 255)
        self.real_life_position = (lat, long)
        self.img_pos = (np.log(np.tan((lat / 2) + (np.pi / 4))),long)
        self.rect = pygame.Rect(lat, long, 10, 10)
        pygame.draw.rect()

class Path(pygame.sprite.Group):
    def __init__(self):
        super.__init__()
        pass


class Map_Generator():
    def __init__(self, number_of_vertices):
        plt.figure()
        # Set the dimensions of the figure
        plt.figure(figsize=(50, 50))
        self.m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
        self.draw_vertices(number_of_vertices)
        for result in self.results:
            long = result[2]
            lat = result[3]
            x,y = self.m(long, lat)
            self.m.scatter(x, y, marker='o', color='r', zorder=2)
            print(result)
        plt.show()
        # Set the map projection.
        # You can choose from a variety of map projections.
        # Some examples include: 'aeqd', 'moll', 'robin', 'merc'
        # Draw the coastlines
        self.m.drawcoastlines()
        # Draw country boundaries
        self.m.drawcountries()
        # Draw lat/lon grid lines every 30 degrees.
        self.m.drawmeridians(range(-180, 180, 20))
        self.m.drawparallels(range(-90, 90, 20))
        # Convert the lat/lon coordinates to map projection coordinates
        # Save the map as an image file
        plt.savefig('map.png', bbox_inches='tight')



    def draw_vertices(self, number_of_vertices):
        # Connect to the database
        conn = sqlite3.connect('Locations.db')

        # Create a cursor
        cursor = conn.cursor()

        # Select multiple random rows from the table
        cursor.execute("SELECT * FROM Location ORDER BY RANDOM()")

        # Fetch the results
        self.results = cursor.fetchmany(2)
        # Print the results

        # Close the cursor and connection
        cursor.close()
        conn.close()




game = main_game()
