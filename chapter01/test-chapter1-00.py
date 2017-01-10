import unittest
import chapter01_00

class TestCalc(unittest.TestCase):

    def test_00(self):
        self.assertEqual(chapter01_00.execute("stressed"), "desserts")
