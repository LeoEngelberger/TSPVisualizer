from MenuSrc.Menu import MenuComponent
import globals

class MainMenu:
    def __init__(self):
        self.globals = globals.Globals._instance
        self.main_component = MenuComponent()
        self.main_component.add_button((self.globals.screen_x/12*2, (self.globals.screen_y/6)*5), (self.globals.screen_x/6, 100), "Easy", "Easy" ,self.globals.main.start_game_function, 4)
        self.main_component.add_button((self.globals.screen_x/12*6, (self.globals.screen_y/6)*5), (self.globals.screen_x/6, 100), "Middle", "NOrmal", self.globals.main.start_game_function, 7)
        self.main_component.add_button((self.globals.screen_x/12*10, (self.globals.screen_y/6)*5), (self.globals.screen_x/6, 100), "Hard", "Hard", self.globals.main.start_game_function, 10)