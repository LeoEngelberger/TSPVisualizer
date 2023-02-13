import pygame

import globals


class Vertex(pygame.sprite.Sprite):
    def __init__(self, color, name, long, lat, player):
        super(Vertex, self).__init__()
        self.globals = globals.Globals._instance
        self.image = pygame.Surface([20, 20])
        self.image.fill(color)
        self.name = name
        self.rect = self.image.get_rect()
        self.rect.width, self.rect.height = (30, 30)
        self.long, self.lat = long, lat
        self.player=player
        self.has_been_visited = False

    def clicked(self):
        print(self.name)
        self.image.fill(self.globals.green)
        self.player.add_vertex_to_path(self)
        self.has_been_visited = True
        if self.globals.main.game_session:
            self.globals.main.game_session.background.blit(self.image, (self.rect.x, self.rect.y))

