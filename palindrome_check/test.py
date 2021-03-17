#!/usr/local/bin/python3

def is_palindrome(s: str) -> bool:

    if not s: return True

    left, right = 0, len(s)-1

    while left < right:

        if s[left] == s[right]:
            left += 1
            right -= 1
            continue

        else:
            if s[left] != ' ' and s[right] != ' ': return False

            if s[left] == ' ':
                left += 1
                continue

            if s[right] == ' ':
                right -= 1
                continue

    return True


if (is_palindrome("no lemon,no melon")):
    print("YES")
else:
    print("NO")
