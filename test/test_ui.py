import unittest
from src import Visualizer

win = Visualizer()


class TestUI(unittest.TestCase):
    def test_display(self):
        # dimensions
        self.assertEqual(win.window_size, win.display.get_size())

    def test_generate_rectangles(self):
        nums = [3, 2.5, 0, -6, 'a', True]
        for num in nums:
            win.generate_rectangle_heights(num)

    def test_draw_rectangles(self):
        heights = win.generate_rectangle_heights(10)
        win.draw_rectangles(win.display, -win.display_width, win.display_height, 10, heights, color_list=None)

        
if __name__ == "__main__":
    unittest.main()
