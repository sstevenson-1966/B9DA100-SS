# -*- coding: utf-8 -*-

# to begin we start with a list of words in a file called spell.words
# we read the file and strip out the file endings
# we are using the profanity library which is available for english by default
# For french I have created a custom list of profanity words manually as the
#     library does not do French profanity words
#
from profanity import profanity
import glob

class SpellChecker(object):

    def __init__(self):
        self.words = []

    ##  I want to check a document/book for profanities.  The book
    ##    uses utf8 as encoding
    def read_book(self, book_name):
        book_lines = open(book_name, encoding = "utf8").readlines()
        return list(map(lambda x: x.strip().lower(), book_lines))
        
    ##  Loading file line by line
    def load_file(self, file_name):
        lines = open(file_name).readlines()
        return list(map(lambda x: x.strip().lower(), lines))

    ##  All valid words in spellchecker go int self.words dictionary
    def load_words(self, language):
        if language == "eng":
            file_name = "engspell.words.txt"
        else:
            file_name = "frspell.words.txt"    

        self.words = self.load_file(file_name)

    ##  Check each word to see if it is a profanity
    def is_a_profanity(self, word):
        return profanity.contains_profanity(word)
        
    ##  Check each word to see if it is valid
    def check_word(self, word):
        return word.lower().strip('.,\?-') in self.words
    
    ##  Loop for checking every word in every sentence in the book/document
    def check_words(self, sentence, language, index=0):
        failed_words = []
        words_to_check = sentence.split(' ')
        caret_position = 0
        for word in words_to_check:
            if not self.check_word(word):
                failed_words.append(
                    {'word':word, 'line':index+1,
                        'pos':caret_position+1, 'type': 'spelling'})
            if self.is_a_profanity(word):
                failed_words.append(
                    {'word':word, 'line':index+1,
                        'pos':caret_position+1, 'type': 'profanity'})
            caret_position += len(word) + 1
        return failed_words

    ##  Check document
    def check_document(self, file_name, language):
        failed_words_in_sentences = []
        self.sentences = self.read_book(file_name)
        for index, sentence in enumerate(self.sentences):
            failed_words_in_sentences.extend(
                self.check_words(sentence, language, index))
        return failed_words_in_sentences

    def prepare_profanities(self, language):
        if language == "fr":
            badwords = ['merde', 'Putain', 'Enculer', 'Salaud']
        else:
            badwords = ['fuck', 'shit', 'cock']
        profanity.load_words(badwords)
                    
if __name__ == '__main__':  
    myLanguage = ""
    while myLanguage.lower() != "eng" and myLanguage.lower() != "fr":
        myLanguage = input('Enter Language : ')
    spell_checker = SpellChecker()
    spell_checker.load_words(myLanguage.lower())
    spell_checker.prepare_profanities(myLanguage.lower())
    
      
    file_wildcard = '*' + myLanguage.lower() + ".txt"
    print(file_wildcard)
    files_to_check = glob.glob(file_wildcard)
    for document in files_to_check:
        print("Document to check : " + document)
        for myitems in spell_checker.check_document(document, myLanguage.lower()):
            print(myitems)
    

    print(len(spell_checker.read_book("fr.txt")))
    # now check if the word zygotic is a word
    ### print(spell_checker.check_word('zygotic'))
    ### print(spell_checker.check_word('mistasdas'))
    ### print(spell_checker.check_words('zygotic mistasdas elementary'))
    ### print(spell_checker.check_words('zygotic mistasdas shit'))
    