# Visualizer class file

import sys
import random
import pygame

# initialize pygame
pygame.init()

class Visualizer:
    # screen attributes
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 700
    FPS = 60
    BACKGROUND_COLOR = pygame.Color("#333333")

    # fonts
    ARIAL_20 = pygame.font.Font("font/arialbd.ttf", 20)
    ARIAL_30 = pygame.font.Font("font/arialbd.ttf", 30)

    # colors
    WHITE = pygame.Color("#ffffff")
    RED = pygame.Color("#d14d54")
    WARNING_ORANGE = pygame.Color("#e3b226")
    RECTANGLE_COLORS = [pygame.Color("#4d6dd1"), # 
                        pygame.Color("#294ab3"), #
                        pygame.Color("#3d4d7f")  #
                        ] 
    # other           
    elapsed_time = 0
    number_of_rectangles = 65

    RUNNING = True
    IS_SORTING = False
    UPDATE_TIMER = False
    DISPLAY_MENU = False

    # algorithm params
    algorithm = None
    algorithm_name_display = None
    sorting_algorithm_generator = None

    def __init__(self):
        self.display_width = self.SCREEN_WIDTH
        self.display_height = self.SCREEN_HEIGHT
        self.window_size = (self.display_width, self.display_height)
        self.setup_ui(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
    
    def setup_ui(self, display_width, display_height):
        """setup main application window

        Args:
            display_width (int)
            display_height (int)
        """
        self.display = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption('sorting vizualizer ~ by Daniel A.')
        app_icon = pygame.image.load('logo.png')
        pygame.display.set_icon(app_icon)
        return True
    
    
    
    def position_text(self, display, font, text, color, pos_x, pos_y):
        """quick & easy way to position text onto main display in a single call

        Args:
            display (pygame.Surface): application's main display surface
            font (pygame.Surface): pygame font
            text (str): text to blit
            color (pygame.Color)
            pos_x (int): text surface's topleft x position, if None is passed, text will be centered
            pos_y (int): text surface's topleft y position
        """
        text = font.render(text, 1, color)
        if pos_x is None:
            pos_x = self.display_width/2 - text.get_width()/2
        display.blit(text, (pos_x, pos_y))
        return text

    
    def display_algorithm_menu(self, display):
        """display algorithm selection menu

        Args:
            display (pygame.Surface): application's main display surface
        """

        display.fill(self.BACKGROUND_COLOR)
        self.position_text(self.display, self.ARIAL_30, "1: Bubble Sort", self.WHITE, None, self.display_height/2 - 100)
        self.position_text(self.display, self.ARIAL_30, "2: Quick Sort", self.WHITE, None, self.display_height/2)
        self.position_text(self.display, self.ARIAL_30, "3: Merge Sort", self.WHITE, None, self.display_height/2 + 100)
        self.position_text(self.display, self.ARIAL_30, "B: Back", self.RED, 10, 10)

    def display_app_info(self, algorithm_name, runtime):
        """display useful information to the user

        Args:
            display (pygame.Surface)
            algorithm_name (str): the name of the sorting algorithm
            runtime (int): the total time of execution
        """
        # controls
        self.position_text(self.display, self.ARIAL_20, "R: shuffle", self.WHITE, self.display_width - 320, 10)
        self.position_text(self.display, self.ARIAL_20, "Q: quit application", self.WHITE, self.display_width - 320, 40)
        self.position_text(self.display, self.ARIAL_20, "L: algorithms list", self.WHITE, self.display_width - 320, 70)
        self.position_text(self.display, self.ARIAL_20, "SCROLL UP: more rectangles", self.WHITE, self.display_width - 320, 100)
        self.position_text(self.display, self.ARIAL_20, "SCROLL DOWN: less rectangles", self.WHITE, self.display_width - 320, 130)

        # simulation data
        self.position_text(self.display, self.ARIAL_20, f"Algorithm: {algorithm_name}", self.WHITE, 20, 10)
        self.position_text(self.display, self.ARIAL_20, f"Runtime: {runtime} s", self.WHITE, 20, 40)
        self.position_text(self.display, self.ARIAL_20, f"Number of rectangles: {self.number_of_rectangles}", self.WHITE, 20, 70)
        self.position_text(self.display, self.ARIAL_20, "1) Press L to select algorithm", self.WARNING_ORANGE, None, 10)
        self.position_text(self.display, self.ARIAL_20, "2) Press Space to sort!", self.WARNING_ORANGE, None, 40)
        
    def generate_rectangle_heights(self, number_of_rectangles):
        """generate list of random values which will be used as heights for the rectangles

        Args:
            number_of_rectangles (int): desired number of rectangles to be drawn

        Returns:
            list: list of random height values
        """
        self.heights_list = []
        try:
            for _ in range(number_of_rectangles):
                height = random.randint(200,600)
                self.heights_list.append(height)
        except TypeError:
            print("number of rectangles should be integer value")
        return self.heights_list
        
    def draw_rectangles(self, display, screen_width, screen_height, number_of_rectangles, heights_list, color_list):
        """draw rectangles onto the screen

        Args:
            display (pygame.Surface): application's main display surface
            screen_width (int): display surface width
            screen_height (int): display surface height
            number_of_rectangles (int)
            heights_list (list) 
            color_list (list)
        """
        if color_list is None:
            # default
            color_list = [pygame.Color("#4d6dd1"), # 
                        pygame.Color("#294ab3"), #
                        pygame.Color("#3d4d7f")  #
                        ]
        rect_x = 0

        try:
            for i,height in enumerate(heights_list):
                rectangle_width = round(screen_width / number_of_rectangles, ndigits=10)
                rectangle_height = screen_height - height
                color = color_list[i % len(color_list)]
                pygame.draw.rect(display, color, (rect_x,height,rectangle_width,rectangle_height))
                rect_x += rectangle_width
        except TypeError:
            print("Verify that all arguments are of the correct type")
        
    def update_display(self):
        """udpate text data and any change regarding the rectangles such has how many to draw and changes in position
        """
        self.display_app_info(self.algorithm_name_display, runtime=round(self.elapsed_time, 3))
        self.draw_rectangles(self.display, self.display_width, self.display_height, self.number_of_rectangles, self.heights_list, self.RECTANGLE_COLORS)