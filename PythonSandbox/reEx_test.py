import unittest
from reEx import reExMatch 

class Test_reEx_test(unittest.TestCase):
    def test_A(self):
        self.assertEqual(None, reExMatch("something", r"\d"))
    def test_match(self):
        self.assertEqual("1", reExMatch("10", r"\d")[0])

if __name__ == '__main__':
    unittest.main()
