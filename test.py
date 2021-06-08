

import unittest
import calc


class testCaseAdd(unittest.TestCase):

    def test_1(self):
        self.assertEqual(calc.add(1, 4), 5)


if __name__ == '__main__':
    unittest.main()
