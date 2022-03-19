# sorting visualizer: one-file application
import sys
import pygame
import random
pygame.init() # initialize pygame


#------------- config.py: Start-------------#

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
FPS = 60

BACKGROUND_COLOR = pygame.Color("#333333")

RECTANGLE_COLORS = [pygame.Color("#29639e"),
                    pygame.Color("#ca212c"), 
                    pygame.Color("#ca372c"), 
                    pygame.Color("#21ca7d"),
                    pygame.Color("#b4ca21"),
                    pygame.Color("#ca21ab"),
                    pygame.Color("#dfb4d7"),
                    pygame.Color("#e13a05"),
                    pygame.Color("#e1d705"),
                    pygame.Color("#05e1c9")] 

NUMBER_OF_RECTANGLES = 100

#------------- config.py: End-------------#


# main window
window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('sorting vizualizer')
app_icon = pygame.image.load('logo.png')
pygame.display.set_icon(app_icon)

# Set fps
clock = pygame.time.Clock() 

# functions
def generate_rectangle_heights(number_of_rectangles):
    """generate list of random values which will be used as heights for the rectangles

    Args:
        number_of_rectangles (int): desired number of rectangles to be drawn

    Returns:
        list: list of random height values
    """

    heights_list = []
    for _ in range(number_of_rectangles):
        height = random.randint(200,600)
        heights_list.append(height)
    return heights_list


def draw_rectangles(window, screen_width, screen_height, number_of_rectangles, heights_list, color_list):
    """draw rectangles onto the screen

    Args:
        window (Pygame Window Object): application's main display surface
        screen_width (int): display surface width
        screen_height (int): display surface height
        number_of_rectangles (int)
        heights_list (list): 
        color_list (list):
    """
    rect_x = 0

    for i,height in enumerate(heights_list):
        rectangle_width = round(screen_width / number_of_rectangles, ndigits=10)
        rectangle_height = screen_height - height
        color = color_list[i % len(color_list)]
        pygame.draw.rect(window, color, (rect_x,height,rectangle_width,rectangle_height))
        rect_x += rectangle_width


# create list upon init
heights_list = generate_rectangle_heights(NUMBER_OF_RECTANGLES)

# main loop
while True:
    window.fill(BACKGROUND_COLOR)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                # shuffle
                heights_list = generate_rectangle_heights(NUMBER_OF_RECTANGLES)
                draw_rectangles(window, SCREEN_WIDTH, SCREEN_HEIGHT, NUMBER_OF_RECTANGLES, heights_list, RECTANGLE_COLORS)

        if event.type == pygame.MOUSEWHEEL:
            if event.y == 1:
                NUMBER_OF_RECTANGLES += 5
                heights_list = generate_rectangle_heights(NUMBER_OF_RECTANGLES)
                draw_rectangles(window, SCREEN_WIDTH, SCREEN_HEIGHT, NUMBER_OF_RECTANGLES, heights_list, RECTANGLE_COLORS)
            elif event.y == -1:
                NUMBER_OF_RECTANGLES -= 5
                heights_list = generate_rectangle_heights(NUMBER_OF_RECTANGLES)
                draw_rectangles(window, SCREEN_WIDTH, SCREEN_HEIGHT, NUMBER_OF_RECTANGLES, heights_list, RECTANGLE_COLORS)
    
    draw_rectangles(window, SCREEN_WIDTH, SCREEN_HEIGHT, NUMBER_OF_RECTANGLES, heights_list, RECTANGLE_COLORS)

    # set fps frequency
    clock.tick(FPS) # to adjust for excecution speed
    pygame.display.update()