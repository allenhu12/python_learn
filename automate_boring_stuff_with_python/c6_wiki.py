#!/usr/bin/env python3
"""
version:            
name:               
functionality:
get the string from the clipboard
add star mark '*' at the begin of each line
copy the new string into the clipboard
"""
import pyperclip
def main():
    text = pyperclip.paste()
    list_wiki_line = text.split('\n')
    list_wiki_line_new = []
    new_text = ''
    for oneline in list_wiki_line:
        newline = '* '+oneline
        list_wiki_line_new.append(newline)
    new_text = '\n'.join(list_wiki_line_new)
    print(new_text)
    pyperclip.copy(new_text)


if __name__ == '__main__':
    '''
    '''
    main()