#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return (0, None)
    length = len(sentence)
    char = sentence[0]
    return (length, char)


if __name__ == '__main__':
    multiple_returns()
