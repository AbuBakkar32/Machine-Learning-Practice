import unittest

from utestfile.file import rmath
from utestfile.file.rname import Rname


# pytest -v --cov=rmath --cov-report=html
# pytest -v --cov=../ --cov-report=html
# pytest -v --cov=./file --cov-report=html


class RmathTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass\n')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass')

    def setUp(self):
        print('setUp')
        self.getName = Rname('Abu', 'Bakkar').getFullName()

    def tearDown(self) -> None:
        print('tearDown\n')
        pass

    def test_addition(self):
        print('test_addition')
        sum = rmath.addition(20, 12)
        self.assertEqual(sum, 32)

    def test_substraction(self):
        print('test_substraction')
        sub = rmath.substract(10, 5)
        self.assertTrue(sub, 5)

    def test_multiplication(self):
        print('test_multiplication')
        mul = rmath.multiplication(50, 5)
        self.assertEqual(mul, 250)

    def test_division(self):
        print('test_division')
        div = rmath.division(20, 10)
        self.assertEqual(div, 2)

    def test_getFullName(self):
        print('test_getFullName')
        self.assertEqual(self.getName, 'abu bakkar', "Sorry same not Same")

    def test_getFullNameLength(self):
        print('test_getFullNameLength')
        self.assertEqual(len(self.getName), 10, "Length Not Same")

    if __name__ == '__main__':
        unittest.main()
