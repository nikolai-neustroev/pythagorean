import unittest

from src.pythagorean_theorem import hypotenuse


class TestHypotenuse(unittest.TestCase):
    def test_valid_input(self):
        c = hypotenuse(3.0, 4.0)
        self.assertEqual(c, 5.0)

    def test_a_negative(self):
        with self.assertRaises(ValueError):
            c = hypotenuse(-3.0, 4.0)

    def test_b_negative(self):
        with self.assertRaises(ValueError):
            c = hypotenuse(3.0, -4.0)

    def test_a_zero(self):
        with self.assertRaises(ValueError):
            c = hypotenuse(0.0, 4.0)

    def test_b_zero(self):
        with self.assertRaises(ValueError):
            c = hypotenuse(3.0, 0.0)


if __name__ == '__main__':
    unittest.main()
