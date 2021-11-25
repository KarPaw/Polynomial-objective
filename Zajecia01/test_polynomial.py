import unittest

from Polynomial import Polynomial

class TestPolynomial(unittest.TestCase):

    def setUp(self):
        self.w1 = Polynomial([1, 2, 3, 5])      # 1*x^3 + 2*x^2 + 3*x + 5
        self.w2 = Polynomial(5, 2, 1)           #         5*x^2 + 2*x + 1
        self.w3 = Polynomial(self.w1)

    def test_coefficients(self):
        self.assertEqual([5, 3, 2, 1], self.w1.coefficients)
        self.assertEqual([1, 2, 5], self.w2.coefficients)
        self.assertEqual([5, 3, 2, 1], self.w3.coefficients)
        c = self.w3.coefficients
        c.append(7)
        self.assertEqual([5, 3, 2, 1], self.w3.coefficients)

    def test_init(self):
        args = [1, 2, 3, 5]
        w = Polynomial(args)
        args.append(7)
        self.assertEqual([5, 3, 2, 1], w.coefficients)

    def test_str(self):
        self.assertEqual("x^3 + 2x^2 + 3x + 5", str(self.w1))
        self.assertEqual("5x^2 + 2x + 1", str(self.w2))

    def test_add(self):
        w3 = self.w2 + self.w1
        self.assertEqual([6, 5, 7, 1], w3.coefficients)
        w3 = self.w1 + self.w2
        self.assertEqual([6, 5, 7, 1], w3.coefficients)

    def test_sub(self):
        w3 = self.w2 - self.w1
        self.assertEqual([-4, -1, 3, -1], w3.coefficients)
        w4 = self.w1 - self.w2
        self.assertEqual([4, 1, -3, 1], w4.coefficients)


if __name__ == '__main__':
        unittest.main()
