import unittest
from main import Tester_mind


class TestGit(unittest.TestCase):


    def testNoRepositories(self):
        self.assertEqual(Tester_mind('ReddyJ'), 'No repositories created', 'No repositories created')

    def testNoUser(self):
        self.assertEqual(Tester_mind('Sheddgsdvjadg'), 'Failed to retrieve data!')

    def testUser(self):
        self.assertEqual(Tester_mind('Pranay'), [('Spoon-Knife', 5), ('tipster', 6)])


if __name__ == '_main_':
    print('Running unit tests')
    unittest.main()