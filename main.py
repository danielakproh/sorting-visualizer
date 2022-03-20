# SORTING visualizer: main file
import sys
import pygame

from src.visualizer import Visualizer
from src.algorithm import bubble_sort

def main():

    # init app
    app = Visualizer()

    # Set clock
    clock = pygame.time.Clock()

    # init heights list
    heights_list = app.generate_rectangle_heights(app.number_of_rectangles)

    # game loop
    while True:
        if app.IS_SORTING:
            try:
                next(app.sorting_algorithm_generator)
                app.UPDATE_TIMER = True
            except StopIteration:
                app.IS_SORTING = False
                app.UPDATE_TIMER = False

        app.display.fill(app.BACKGROUND_COLOR)
        for event in pygame.event.get():
            # exit app
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_l:
                    app.DISPLAY_MENU = True

                if event.key == pygame.K_r:
                    # shuffle
                    heights_list = app.generate_rectangle_heights(app.number_of_rectangles)
                    app.update_display()

                if event.key == pygame.K_l:
                    app.DISPLAY_MENU = True

                # algorithm selection
                if event.key == pygame.K_1:
                    app.algorithm_name_display = "Bubble Sort"
                    app.algorithm = bubble_sort
                    app.DISPLAY_MENU = False

                if event.key == pygame.K_2:
                    app.algorithm_name_display = "Quick Sort"
                    app.algorithm = bubble_sort # implement quick sort
                    app.DISPLAY_MENU = False

                if event.key == pygame.K_3:
                    app.algorithm_name_display = "Merge Sort"
                    app.algorithm = bubble_sort # implement quick sort
                    app.DISPLAY_MENU = False

            # controls
                if event.key == pygame.K_b:
                    app.DISPLAY_MENU = False

                if event.key == pygame.K_SPACE and not app.IS_SORTING and app.algorithm_name_display != None:
                    app.IS_SORTING = True
                    app.sorting_algorithm_generator = app.algorithm(heights_list)
                    app.elapsed_time = 0
                    app.update_timer = True

            if event.type == pygame.MOUSEWHEEL:
                if event.y == 1 and not app.IS_SORTING:
                    app.number_of_rectangles += 5
                    heights_list = app.generate_rectangle_heights(app.number_of_rectangles)
                    app.update_display()

                elif event.y == -1 and not app.IS_SORTING:
                    app.number_of_rectangles -= 5
                    heights_list = app.generate_rectangle_heights(app.number_of_rectangles)
                    app.update_display()

        app.update_display()

        if app.DISPLAY_MENU:
            app.display_algorithm_menu(app.display)
        
        if app.UPDATE_TIMER:
            app.elapsed_time += round(1 / app.FPS, 3)

        # set fps frequency
        clock.tick(Visualizer.FPS)
        # update screen
        pygame.display.update()

if __name__ == "__main__":
    main()