"""
User Words
Doc2Doc has a spellchecker, but users often use slang words that aren't recognized. Create a feature to allow users to add their own words to the spellchecker.

Assignment
Complete the 'user_words' function. It accepts a tuple of initial_words as input and returns a function, add_word. Since tuples are immutable, you don't need to worry about modifying the initial_words. add_word should add a new word string to the words and return all words as a tuple.
"""

def user_words(initial_words):
    words = initial_words

    def add_word(word):
        nonlocal words
        words = words + (word,)
        return words
    
    return add_word