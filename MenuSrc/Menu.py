import pygame
import globals

class MenuComponent:
    def __init__(self, background=None):
        self.globals = globals.Globals._instance
        self.background = pygame.Surface(self.globals.screen_size)

        self.widgets = {}

        if background:
            self.background.blit(background, (0, 0))
        else:
            self.background.fill(self.globals.green)
        self.globals.screen.blit(self.background, (0, 0))

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for name in self.widgets:
                widget = self.widgets[name]
                if widget.imageRect.collidepoint(event.pos):
                    widget.clicked()

    def add_button(self, position, size, name, text ,function, param1 = None):
        if param1:
            new_button = Button(position, size, name, function, text, param1)
        else:
            new_button = Button(position, size, name, function, text)
        self.widgets[name] = new_button




class Widget(pygame.sprite.Sprite):
    def __init__(self, position, size, name, background=None):
        super().__init__()
        self.globals = globals.Globals._instance
        self.position = position
        self.size = size
        self.name = name
        self.id = None
        self.image = pygame.surface.Surface(self.size)
        self.imageRect = self.image.get_rect()

    def show_on_screen(self, background):  # needs to be implemented in subclasses
        self.imageRect.center = self.position

        if background:
            self.image.fill(background)
        else:
            self.image.fill(self.globals.widget_color)




class Button(Widget):
    def __init__(self, position, size, name,function, text=None, param1 = None, background=None):
        self.text, self.shadow_text, self.textRect, self.shadow_text_rect, self.param1 = None, None, None,None, param1
        self.function = function
        super().__init__(position, size, name, background)

        self.show_on_screen(background, text)

    def show_on_screen(self, background, text=None):
        super().show_on_screen(background)
        if text:
            self.text = self.globals.font.render(text, True, self.globals.font_color, None)
            self.shadow_text = self.globals.shadow_font.render(text, True, self.globals.shadow_color, None)

        else:
            self.text = self.globals.font.render("", True, self.globals.white, None)
        self.textRect = self.text.get_rect()
        self.textRect.center = self.image.get_rect().center
        self.shadow_text_rect = self.shadow_text.get_rect()
        self.shadow_text_rect.center = self.image.get_rect().center
        self.image.blit(self.shadow_text, self.shadow_text_rect)
        self.image.blit(self.text, self.textRect)

        self.globals.screen.blit(self.image, self.imageRect.topleft)

    def clicked(self):
        if self.param1:
            self.function(self.param1)
        else:
            self.function()