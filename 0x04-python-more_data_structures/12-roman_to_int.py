#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string == None or not isinstance(roman_string, str):
        return 0
    res = 0
    pos = 0
    rome_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                 'D': 500, 'M': 1000}
    while pos < len(roman_string):
        if roman_string[pos] == 'I':
            if pos + 1 < len(roman_string) and roman_string[pos + 1] == 'V':
                res += 4
                pos += 2
                continue
            elif pos + 1 < len(roman_string) and roman_string[pos + 1] == 'X':
                res += 9
                pos += 2
                continue
            else:
                res += rome_dict['I']
        elif roman_string[pos] == 'V':
            res += rome_dict['V']
        elif roman_string[pos] == 'X':
            if pos + 1 < len(roman_string) and roman_string[pos + 1] == 'L':
                res += 40
                pos += 2
                continue
            elif pos + 1 < len(roman_string) and roman_string[pos + 1] == 'C':
                res += 90
                pos += 2
                continue
            else:
                res += rome_dict['X']
        elif roman_string[pos] == 'L':
            res += rome_dict['L']
        elif roman_string[pos] == 'C':
            if pos + 1 < len(roman_string) and roman_string[pos + 1] == 'D':
                res += 400
                pos += 2
                continue
            elif pos + 1 < len(roman_string) and roman_string[pos + 1] == 'M':
                res += 900
                pos += 2
                continue
            else:
                res += rome_dict['C']
        elif roman_string[pos] == 'D':
            res += rome_dict['D']
        elif roman_string[pos] == 'M':
            res += rome_dict['M']
        pos += 1
    return res


if __name__ == "__main__":
    roman_to_int()
