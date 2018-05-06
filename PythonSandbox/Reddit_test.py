import unittest
from Reddit import Reddit

class Test_Reddit_test(unittest.TestCase):

    def setUp(self):
        self.reddit = Reddit()
        return super().setUp()

    def test_connect_as_read(self):
        self.reddit.open_reddit_read()
        self.assertTrue(self.reddit.is_read_only())

    def test_connect_as_write(self):
        self.reddit.open_reddit_write()
        self.assertFalse(self.reddit.is_read_only())

    def test_returns_generator(self):
        self.reddit.open_reddit_read()
        top_submissions = 5
        sut = self.reddit.top_submissions('u_hansknecht', top_submissions)
        count = 0
        for submission in sut:
            count += 1
            print(submission.title)
        self.assertEqual(count, top_submissions, "The top ten submissions were not collected")

if __name__ == '__main__':
    unittest.main()
