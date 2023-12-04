#!/usr/bin/python3

def multiple_returns(sentence):
    if not sentence:
        return (0, None)

    first_character = sentence[0]
    length = len(sentence)
    return (length, first_character)
