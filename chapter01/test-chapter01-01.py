import unittest
import chapter01_01

class TestCalc(unittest.TestCase):

    def test_01(self):
        self.assertEqual(chapter01_01.execute("パタトクカシーー"), "パトカー")
