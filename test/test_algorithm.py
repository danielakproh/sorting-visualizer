import unittest
from src import bubble_sort



class TestSortingAlgorithm(unittest.TestCase):

    test_inputs = [
        [38, 8, 10, 43, 6, 90, 71, 22, 47, 63],   
        [69, 73, -20, 31, 61, -26, 57, 76, 7, 23],
        [59, 54, 68, 91, 51, 85, 63, 42, 62],        
        [0, 86, -55, -29, -82, -71, 31, 70, 45, 14, -3, 43, 90, 21]
    ]

    expected_outputs = [
        [6, 8, 10, 22, 38, 43, 47, 63, 71, 90],
        [-26, -20, 7, 23, 31, 57, 61, 69, 73, 76],
        [42, 51, 54, 59, 62, 63, 68, 85, 91],
        [-82, -71, -55, -29, -3, 0, 14, 21, 31, 43, 45, 70, 86, 90]
    ]

    def test_bubble_sort(self):
        for i in range(len(self.test_inputs)):
            sorted_list = bubble_sort(self.test_inputs[i])
            self.assertEqual(sorted_list, self.expected_outputs[i])
        bubble_sort([-34, 5, 12, True])
        bubble_sort([])


if __name__ == "__main__":
    unittest.main()
        