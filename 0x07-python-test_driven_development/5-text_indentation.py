#!/usr/bin/python3
"""
Module text_indentation
text_indentation

"""


def text_indentation(text):
    """
       Prints indent text
    """

    if type(text) != str or text is None or len(text) < 0:
        raise TypeError("text must be a string")
    aux = 0
    for char in text:
        if char == '?' or char == ':' or char == '.':
            print(char, end="\n\n")
            aux = 1
        else:
            if aux == 0:
                print(char, end="")
            else:
                if char == ' ' or char == '\t':
                    pass
                else:
                    print(char, end="")
                    aux = 0
