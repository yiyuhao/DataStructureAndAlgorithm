import unittest
from t import quick_sort


class TestQsort(unittest.TestCase):
    def test_common(self):
        lst = [3, 2, 1]
        self.assertEqual(quick_sort(lst), [1, 2, 3])


if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestQsort)
    unittest.TextTestRunner().run(test_suite)

