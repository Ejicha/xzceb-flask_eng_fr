'''Tests'''

import unittest

from translator import english_to_french, french_to_english

class TestFrenchToEnglish(unittest.TestCase):
    '''French to English'''
    def test1(self):
        '''Correct'''
        self.assertEqual(french_to_english("Bonjour"), "Hello")

    def test2(self):
        '''Null'''
        self.assertEqual(french_to_english(" "), " ")

    def test3(self):
        '''Null'''
        self.assertNotEqual(french_to_english(" "), None)


class TestEnglishToFrench(unittest.TestCase):
    '''English to French'''
    def test1(self):
        '''Correct'''
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test2(self):
        '''Null'''
        self.assertEqual(english_to_french(" "), " ")

    def test3(self):
        '''Null'''
        self.assertNotEqual(french_to_english(" "), None)

if __name__ == "__main__":
    unittest.main()
