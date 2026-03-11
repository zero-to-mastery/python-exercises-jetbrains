import unittest
from task import slice1, slice2, slice3, slice4, slice5, slice6, slice7, slice8


class TestCase(unittest.TestCase):
    def test_slice1(self):
        self.assertEqual(slice1, "gram",
                        msg="slice1 should extract 'gram' from indices 3 to 6")

    def test_slice2(self):
        self.assertEqual(slice2, "amming",
                        msg="slice2 should extract from index 5 to end: 'amming'")

    def test_slice3(self):
        self.assertEqual(slice3, "Prog",
                        msg="slice3 should extract first 4 characters: 'Prog'")

    def test_slice4(self):
        self.assertEqual(slice4, "g",
                        msg="slice4 should extract the last character: 'g'")

    def test_slice5(self):
        self.assertEqual(slice5, "ming",
                        msg="slice5 should extract last 4 characters: 'ming'")

    def test_slice6(self):
        self.assertEqual(slice6, "Programm",
                        msg="slice6 should extract everything except last 3: 'Programm'")

    def test_slice7(self):
        self.assertEqual(slice7, "gnimmargorP",
                        msg="slice7 should reverse the string: 'gnimmargorP'")

    def test_slice8(self):
        self.assertEqual(slice8, "Pormig",
                        msg="slice8 should extract every 2nd character: 'Pormig'")
