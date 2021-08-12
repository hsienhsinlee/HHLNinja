#!/usr/local/bin/python3

"""

Compute the Square Root of a given positve number (int or float).
If the result is not an integer, please round it
to the 6th decimal place

Example:

sqrt(2) = 1.414214
sqrt(10) = 3.162278
sqrt(9) = 3
sqrt(169) = 13
sqrt(144) = 12.0

end

"""


error = 0.0000009
number = float(input("input a number : "))
# The following syntax was not allowed byold Python
# while (number := float(input("input a number : "))) != 0.0:
while (number != 0.0):
    print("number = ", number)
    decimal_number = number - int(number)
    delta = number / 2
    candidate_root = delta
    new_number = candidate_root * candidate_root

    while (abs(new_number - number) >= error):
        delta = delta / 2
        if (new_number > number):
            candidate_root = candidate_root - delta
        else:
            candidate_root = candidate_root + delta
        new_number = candidate_root * candidate_root

        # take care of the integer cases
        int_candidate_root = round(candidate_root, 0)
        if (int_candidate_root*int_candidate_root) == number:
            candidate_root = int_candidate_root
            break

    print(number,"square root =", round(candidate_root,6))
    number = float(input("input a number : "))
