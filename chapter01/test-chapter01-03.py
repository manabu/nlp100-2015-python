import unittest
import chapter01_03

class TestCalc(unittest.TestCase):

    def test_03(self):
        self.assertEqual(chapter01_03.execute(
        "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."),
        [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9] )
