#!/usr/local/bin/python3
"""

*** Description ***

Write a function that takes a postfix input expression and outputs result
of the calculation.

"""


in_string = [
    '3 5 + 1 2 * /',
    '1 2 * 1 2 + 4 + *',
    '1 2 3 * +',
    '3.5 4.8 12.1 * 2.145 / /',
    '3 + 4',
    '2 5 6 8 10 * 9 - - * * '

]

def string_conversion(input_string):
    parsed_token = []
    token = input_string.split()

    for i in token:
        if i == "+":
            parsed_token.append(i)
        elif i == "-":
            parsed_token.append(i)
        elif i == "*":
            parsed_token.append(i)
        elif i == "/":
            parsed_token.append(i)
        else:
            try:
                parsed_token.append(int(i))
            except ValueError:
                try:
                    parsed_token.append(float(i))
                except ValueError:
                    print("Parsing error !!", i, "is a unsupported operator")
                    exit()
    return parsed_token

def postfix_process(input_string):

    stack = []
    result = 0
    for element in input_string:
        try:
            if (float(element) or int(element)):
                stack.append(element)
        except ValueError:
            if (len(stack)<2):
                return "Invalid"
            else:
                op1 = stack.pop() # higher in stack
                op2 = stack.pop() # lower in stack
            if (element == "+"):
                result = op2 + op1
            elif (element == "-"):
                result = op2 - op1
            elif (element == "*"):
                result = op2 * op1
            elif (element == "/"):
                result = op2 / op1
            stack.append(result)
    return result


# main program

for index, ele in enumerate(in_string):

    postfix = ele
    new_string = string_conversion(postfix)
    res = postfix_process(new_string)
    if (res != "Invalid"):
        print("[",ele,"]      =", res)
    else:
        print("[",ele,"] is not a valide Posix")
