import pygame
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

class main_game():
    def __init__(self):
        self.x_screen_size = 1080
        self.y_screen_size = 800
        self.font = None
        self.setup()
        self.main_loop()

    def setup(self):
        pygame.init()
        self.font = pygame.font.Font("Targa.ttf", 32)
        self.screen = pygame.display.set_mode((self.x_screen_size,self.y_screen_size))
        pygame.display.set_caption('TSP')
        self.map_setup()
        self.setup_GameSession()

    def setup_GameSession(self):
        txt_nr_o_vert = self.font.render("amount of vertices", True, (0,0,0))
        self.screen.blit(txt_nr_o_vert, (50, 50))
        pass

    def map_setup(self):
        # get the default size

        self.screen.fill((42, 157, 143))

        map_img = pygame.image.load("map.png").convert()
        self.mapSprite = Map(map_img,0,0)
        self.map_surface = pygame.Surface((map_img.get_size()[0], map_img.get_size()[1]))

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
        self.rect = image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        pygame.draw.rect(self.image, rect=pygame.Rect(0, 0, 1080, 750),color=(0,0,0))

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



game = main_game()
