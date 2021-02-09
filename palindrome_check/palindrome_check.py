#!/usr/local/bin/python3

"""
Check if a given string is Palidrome

*** Description ***

Given a case-sensitive string, we want to check if that string can form a palindrome.
Return a bool indicating true or false. Space is not considered as character(s).

+ Positive Examples: "aba", "abba", "rotator", "no lemon, no melon"
- Negative Examples: "acb", "aabc"

"""

while (True):
    in_str = input("")
    print("------------------------------")
    bw_str = in_str[::-1].replace(" ","") # write backward

    length = len(in_str)
    stack = []
    new_st = ""

    for ch in in_str:
        if (not ch.isspace()):
            stack.append(ch)

    new_st = ''.join(stack)

    if (bw_str == new_st):
        print(in_str, "is a palindrome")
    else:
        print(in_str, "is not a palindrome")

    print("------------------------------")
