import unittest
import chapter01_04
class TestCalc(unittest.TestCase):

    def test_04_word_bigram(self):
        self.assertEqual(chapter01_04.execute("Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."),
        [{"H",0},{"He",3},{"Li",6},{"Be",11},{"B",19},
        {"C",25},{"N",31},{"O",35},{"F",42},{"Ne",52},
        {"Na",56},{"Mi",64},{"Al",70},{"Si",75},{"P",80},
        {"S",86},{"Cl",95},{"Ar",103},{"K",110},{"Ca",115}])
