import unittest

from book_nlp_for_deep_learning.pandas_tutorial.models import Olympic


class OlympicTest(unittest.TestCase):
    mock = Olympic()



    def test_read_wiki(self):
        self.mock.read_wiki()


if __name__ == '__main__':
    unittest.main()