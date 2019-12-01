# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 10:55:40 2019

@author: sebst
"""

import unittest

from CA_1743573_spellchecker import SpellChecker

class TestSpellChecker(unittest.TestCase):
    
    def test_read_book(self):
        self.testSpell = SpellChecker()
        self.assertEqual(len(self.testSpell.read_book("fr.txt")), 4002)
        
    def test_english_profanities(self):
        self.testSpell = SpellChecker()
        self.testSpell.prepare_profanities("eng")
        self.assertTrue(self.testSpell.is_a_profanity("fuck"))
        self.assertFalse(self.testSpell.is_a_profanity("python"))
        
    def test_french_profanities(self):
        self.testSpell = SpellChecker()
        self.testSpell.prepare_profanities("fr")
        ### test if merde is an ok word
        self.assertTrue(self.testSpell.is_a_profanity("merde"))
        self.assertFalse(self.testSpell.is_a_profanity("merdxe_alors"))
 
    def test_valid_english_word(self):
        self.testSpell = SpellChecker()
        self.testSpell.load_words("eng")
        self.assertTrue(self.testSpell.check_word("hello"))
        self.assertFalse(self.testSpell.check_word("depouiller"))
        
    def test_valid_french_word(self):
        self.testSpell = SpellChecker()
        self.testSpell.load_words("fr")
        self.assertTrue(self.testSpell.check_word("paris"))
        self.assertFalse(self.testSpell.check_word("elaborate"))
        
        
if __name__ == '__main__':
    unittest.main()
        
        