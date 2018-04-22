import unittest
from exceptional import convert

class Test_exceptional_test(unittest.TestCase):
    def test_Numbers_convert(self):
        self.assertEqual(convert('5'), 5, "The number did not convert")
    def test_error_raised(self):
        self.assertRaises(ValueError, convert, "test")

if __name__ == '__main__':
    unittest.main()
