import pygame


import Menu as menu
import GameObjects.Player as player
import GameSession as GS
import globals

# self.m = Basemap(resolution='h',projection='merc', llcrnrlat=45.73, urcrnrlat=47.9, llcrnrlon=5.85, urcrnrlon=10.58)
pygame.init()

class MainGame:
    def __init__(self):
        self.globals = globals.Globals()
        self.main_menu = menu.BaseMenuComp()

        self.game_session = None
        self.player = player.PlayerClass()
        self.main_loop()
        self.background = pygame.transform.scale(pygame.image.load("map.png"), self.globals.screen.get_size())


    def main_loop(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()

                if self.main_menu.is_enabled:
                    self.main_menu.update(events)


                else:
                    if not self.game_session:
                        amount_of_vertices = 10               #self.main_menu.selector.get_value()[0][1]
                        self.game_session = GS.GameSessionClass(amount_of_vertices, self.player)
                    self.game_session.update(events)

                pygame.display.update()



game = MainGame()
