#!/usr/local/bin/python3
"""

*** Description ***


"""


in_string = [
    '3 5 + 1 2 * /',
    '1 2 * 1 2 + 4 + *',
    '1 2 3 * +'
]

def string_conversion(input_string):
    print("input is", input_string)
    parsed_token = []
    token = in_string.split()

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
    print("parsed string =", input_string)
    stack = []
    result = 0
    for element in input_string:
        try:
            if (float(element) or int(element)):
                stack.append(element)
        except ValueError:
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

in_string2 = "3 5 + 1 2 * /"
new_string = string_conversion(in_string2)
res = postfix_process(new_string)
print("result of", new_string, "is", res)
# main program

"""for index, ele in enumerate(in_string):
    print(index, "Posftfix", ele)
    postfix = ele
    new_string = string_conversion(postfix)
    res = postfix_process(new_string)
    print("result of", new_string, "is", res)
"""
