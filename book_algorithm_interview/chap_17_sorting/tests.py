import unittest
from book_algorithm_interview.chap_17_sorting.models import Sorting


class TestSorting(unittest.TestCase):

    def test_bubble_sort(self):
        instance = Sorting()
        instance.random_array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        arr = instance.bubble_sort()
        self.assertEqual(arr, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_merge_sort(self):
        arr = [7, 1, 4, 3, 8, 5, 6, 9, 2]
        arr = Sorting.merge_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_quick_sort(self):
        arr = [7, 1, 4, 3, 8, 5, 6, 9, 2]
        arr = Sorting.quick_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5, 6, 7, 8, 9])


if __name__ == '__main__':
    unittest.main()

