import pygame

class sMap(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load('map.png').convert()