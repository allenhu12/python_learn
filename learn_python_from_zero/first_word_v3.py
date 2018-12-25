#!/usr/local/bin/python3
"""
    Use Python Unit Test Class to test the first_word function
"""

import unittest

class TestFirstWord(unittest.TestCase) :
    """
        first_word functions
    """
    def test_first_word(self) :
        result = first_word("Hello word")
        self.assertEqual(result, "Hello")
        result = first_word(" a word ")
        self.assertEqual(result, "a")
        result = first_word("don't touch it")
        self.assertEqual(result, "don't")
        

def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    # your code here
    text =  text.replace(',',' ').replace('.',' ').strip()
    return text.split()[0]
      
unittest.main()
#def main() :
#    print("Example:")
#    print(first_word("Hello world"))
#    
#    # These "asserts" are used for self-checking and not for an auto-testing
#    assert first_word("Hello world") == "Hello"
#    assert first_word(" a word ") == "a"
#    assert first_word("don't touch it") == "don't"
#    assert first_word("greetings, friends") == "greetings"
#    assert first_word("... and so on ...") == "and"
#    assert first_word("hi") == "hi"
#    assert first_word("Hello.World") == "Hello"
#    print("Coding complete? Click 'Check' to earn cool rewards!")
#if __name__ == '__main__' :
#    main()
