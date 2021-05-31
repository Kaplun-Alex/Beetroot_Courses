import Math_tests_doctest
import unittest

class OleksaTest(unittest.TestCase):
    def test1(self):
        self.assertTrue(Math_tests_doctest.m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16])
    def test2(self):
        self.assertTrue(Math_tests_doctest.m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90])
    def test3(self):
        self.assertTrue(Math_tests_doctest.m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 202]) # нет 0

if __name__ == '__main__':
    unittest.main()
