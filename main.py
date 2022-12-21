import pygame

class main_game():
    def __init__(self):
        self.x_screen_size = 1080
        self.y_screen_size = 800
        self.setup()
        self.main_loop()

    def setup(self):
        pygame.init()
        self.map_setup()

    def map_setup(self):
        # get the default size
        self.screen = pygame.display.set_mode((self.x_screen_size,self.y_screen_size))

        pygame.display.set_caption('TSP')
        self.screen.fill((42, 157, 143))

        swiss_map_img = pygame.image.load("suisse46.png").convert()
        print(swiss_map_img.get_size())
        x_map_pos = (self.x_screen_size/2) - (swiss_map_img.get_size()[0]/2)
        self.screen.blit(swiss_map_img,(x_map_pos,0))
        pygame.display.flip()

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


game = main_game()
