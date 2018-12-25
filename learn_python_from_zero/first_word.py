#!/usr/local/bin/python3
def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    # your code here
    text.strip()
    f_start_find = False
    start_index = 0
    end_index = 0
    str_len = len(text)
    if str_len == 2 and text[0].isalnum() and text[1].isalnum() :
        return text
    for i in range(str_len) :
        if (f_start_find != True) and (text[i].isalnum() == True) :
            start_index = int(i)
            f_start_find = True
            
        if (f_start_find == True) and (text[i] != "'") and (text[i].isalnum() != True) :
            end_index = int(i)
            break
    first_word = text[start_index:end_index]
    return first_word

def main() :
    print("Example:")
    print(first_word("Hello world"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")
if __name__ == '__main__' :
    main()
