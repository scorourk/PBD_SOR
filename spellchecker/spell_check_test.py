import unittest
from spell import SpellChecker
class TestSpellChecker(unittest.TestCase):

    def setUp(self):
        self.spellChecker = SpellChecker()
        self.spellChecker.load_words('spell.words')

    def test_spell_checker(self):
		self.assertTrue(self.spellChecker.check_word('zygotic'))
		self.assertFalse(self.spellChecker.check_words('zygotic mistasdas elementary'))
		self.assertTrue(self.spellChecker.check_words('our first correct sentence'))
		self.assertTrue(self.spellChecker.check_words('Our first correct sentence'))
		self.assertTrue(self.spellChecker.check_words('Our first correct sentence.'))
		self.assertFalse(self.spellChecker.check_words('zygotic mistasdas spelllleeeing elementary'))
		
if __name__ == '__main__':
    unittest.main()
