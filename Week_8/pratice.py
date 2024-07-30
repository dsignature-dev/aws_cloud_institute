import unittest


def add(x, y):
    return x + y


class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(7, 5), 10)

    def test_add_negative(self):
        self.assertEqual(add(-2, -2), -4)


if __name__ == '__main__':
    unittest.main()
