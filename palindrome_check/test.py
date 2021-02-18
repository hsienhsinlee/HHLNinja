#!/usr/local/bin/python3

def is_palindrome(input):
    start, end = 0, len(input) - 1
    while start <= end:
        if input[start] == input[end]:
            start += 1
            end -= 1
        else: # not matching
            if input[start] == " ":
                start += 1
            elif input[end] == " ":
                end -= 1
            else:
                return False
    return True


cache = {}

a = is_palindrome("ababa")
print(a)
