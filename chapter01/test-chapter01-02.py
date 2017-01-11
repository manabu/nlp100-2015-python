import unittest
import chapter01_02

class TestCalc(unittest.TestCase):

    def test_02(self):
        self.assertEqual(chapter01_02.execute("パトカー", "タクシー"), "パタトクカシーー")
