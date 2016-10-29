import unittest
from slackbot import slackpi

class TestSlackBotFunctions(unittest.TestCase):

    def test_ci(self):
        self.assertTrue(True)

    def test_imports(self):
        self.assertTrue(slackpi.imported())

if __name__ == '__main__':
    unittest.main()
