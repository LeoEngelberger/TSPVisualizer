from MenuSrc.Menu import MenuComponent
import pygame
import globals


TEXT = "ipsem laurem"
class MainMenu:
    def __init__(self):
        self.globals = globals.Globals._instance
        background = pygame.transform.scale(pygame.image.load("Assets/backgroundImageMenu.jpg"), self.globals.screen.get_size())
        self.main_component = MenuComponent(background)
        self.main_component.add_button((self.globals.screen_x/12*2, (self.globals.screen_y/6)*5), (self.globals.screen_x/6, 100), "Easy", "Easy" ,self.globals.main.start_game_function, 4,0.1)
        self.main_component.add_button((self.globals.screen_x/12*6, (self.globals.screen_y/6)*5), (self.globals.screen_x/6, 100), "Middle", "Normal", self.globals.main.start_game_function, 7,10)
        self.main_component.add_button((self.globals.screen_x/12*10, (self.globals.screen_y/6)*5), (self.globals.screen_x/6, 100), "Hard", "Hard", self.globals.main.start_game_function, 10,180)
        self.main_component.add_textbox((self.globals.screen_x/12*2, 400),(200,200), "test", "ipsem laurem",alpha=128)