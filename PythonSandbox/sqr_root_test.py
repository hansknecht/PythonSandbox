import unittest
from sqlroot import sqrt

class Test_sqr_root_test(unittest.TestCase):
    def test_root_of_four_is_two(self):
        sqrt_test = sqrt(4.0)
        self.assertEquals(sqrt_test, 2.0, "The number was not equal to 2 it was equal to {}".format(sqrt_test))
    def test_exception_thrown_if_negative(self):
        self.assertRaises(ValueError, sqrt, -1.0)

if __name__ == '__main__':
    unittest.main()
