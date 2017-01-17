import unittest
import chapter01_07

class TestCalc(unittest.TestCase):

    def test_07_1(self):
        self.assertEqual(chapter01_07.execute("x","y","z"),"x時のyはz")
    def test_07_2(self):
        self.assertEqual(chapter01_07.execute(12,"気温",22.4),"x時のyはz")
