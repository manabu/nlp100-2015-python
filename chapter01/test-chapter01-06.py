import unittest
import chapter01_05
import chapter01_06
class TestCalc(unittest.TestCase):


    def test_06_word_bigram(self):
        X = chapter01_05.charcter_bigram("paraparaparadise")
        Y = chapter01_05.charcter_bigram("paragraph")
        union = chapter01_06.union(X,Y)
        intersection = chapter01_06.intersection(X,Y)
        difference_set = chapter01_06.difference_set(X,Y)
        self.assertEqual(X,["pa","ar","ra","ap","pa","ar","ra","ap","pa","ar","ra","ad","di","is","se"])
        self.assertEqual(Y,["pa","ar","ag","gr","ra","ap","ph"])
        self.assertEqual(union,["pa","ar","ra","ap","pa","ar","ra","ap","pa","ar","ra","ad","di","is","se","pa","ar","ag","gr","ra","ap","ph"])
        # TODO
        # self.assertEqual(intersection,)
        self.assertEqual(difference_set,["pa","ar","ra","ap","pa","ar","ra","ad","di","is","se","ag","gr","ph"])
        self.assertTrue("se" in X)
        self.assertFalse("se" in Y)
