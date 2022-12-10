# written by OpenAI ChatGPT

# define a function to find the factors of a given number
def find_factors(x):
  # create an empty list to store the factors
  factors = []

  # loop through the numbers from 1 to x
  for i in range(1, x+1):
    # if the number is a factor of x, add it to the list of factors
    if x % i == 0:
      factors.append(i)

  # return the list of factors
  return factors

# create a loop to allow the user to enter multiple numbers
while True:
  # prompt the user to enter a number
  number = int(input("Enter a number (0 to quit): "))

  # check if the user entered 0 to quit
  if number == 0:
    break

  # find the factors of the number
  factors = find_factors(number)

  # print the list of factors
  print(factors)

# print a message when the program ends
print("Thank you for using the program. Goodbye!")
