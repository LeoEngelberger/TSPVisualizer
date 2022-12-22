import pygame

# Initialize Pygame
pygame.init()

# Get the screen resolution of the main display
info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h

# Set the window dimensions for the main display
main_width = screen_width
main_height = screen_height

# Create the main display surface
main_screen = pygame.display.set_mode((main_width, main_height))

# Set the window dimensions for the second display
second_width = main_width // 2
second_height = main_height // 2

# Create the second display surface
second_screen = pygame.display.set_mode((second_width, second_height))

# Set the window dimensions for the third display
third_width = main_width // 3
third_height = main_height // 3

# Create the third display surface
third_screen = pygame.display.set_mode((third_width, third_height))

# Draw something on the second and third displays
pygame.draw.circle(second_screen, (255, 0, 0), (second_width // 2, second_height // 2), 100)
pygame.draw.circle(third_screen, (0, 255, 0), (third_width // 2, third_height // 2), 50)

# Update the second and third displays
pygame.display.flip()

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