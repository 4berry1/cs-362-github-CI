

import unittest
import calc


class testCaseAdd(unittest.TestCase):

    def test_1(self):
        self.assertEqual(calc.add(1, 4), 5)

    def test_2(self):
        self.assertEqual(calc.sub(5, 3), 2)

    def test_3(self):
        self.assertEqual(calc.mult(5, 3), 15)


if __name__ == '__main__':
    unittest.main()
