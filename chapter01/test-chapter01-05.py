import unittest
import chapter01_05
class TestCalc(unittest.TestCase):


    def test_05_word_bigram(self):
        self.assertEqual(chapter01_05.word_bigram("I am an NLPer"),
        [["I","am"],["am","an"],["an","NLPer"]])
    def test_05_character_bigram(self):
        self.assertEqual(chapter01_05.charcter_bigram("I am an NLPer"),
        ["I "," a","am","m "," a","an","n "," N","NL","LP","Pe","er"])
