import unittest
from task import word_length, separator, masked_password, border, username_length


class TestCase(unittest.TestCase):
    def test_word_length(self):
        self.assertEqual(word_length, 6,
                        msg="word_length should be 6 (length of 'Python')")

    def test_separator(self):
        self.assertEqual(separator, "----------",
                        msg="separator should be '----------' (10 dashes)")

    def test_masked_password(self):
        self.assertEqual(masked_password, "*********",
                        msg="masked_password should be '*********' (9 asterisks for 'secret123')")

    def test_border(self):
        self.assertEqual(border, "=======",
                        msg="border should be '=======' (7 equals signs matching 'Welcome' length)")

    def test_username_length(self):
        self.assertEqual(username_length, 9,
                        msg="username_length should be 9 (length of 'alex_2024')")
