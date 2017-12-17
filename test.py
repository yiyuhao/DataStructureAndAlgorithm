import unittest

from t import heap_sort


class HeapSortTest(unittest.TestCase):
    def setUp(self):
        self.heap_sort = heap_sort

    def test_zero(self):
        self.assertEqual(self.heap_sort([]), [])

    def test_one_elem(self):
        self.assertEqual(self.heap_sort([-1]), [-1])

    def test_general(self):
        lst = [9, 8, 7, 6, 5, 5, 4, 5, 3, 2, -1]
        s_lst = [-1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9]
        self.assertEqual(self.heap_sort(lst), s_lst)

    def test_raise(self):
        with self.assertRaises(TypeError):
            self.heap_sort((3, 2, 1))

        with self.assertRaises(TypeError):
            self.heap_sort('1, 2, 3')

        with self.assertRaises(TypeError):
            self.heap_sort(123)

if __name__ == '__main__':
    tests = unittest.defaultTestLoader.loadTestsFromTestCase(HeapSortTest)
    unittest.TextTestRunner().run(tests)
