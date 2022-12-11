# written by OpenAI ChatGPT
import os # for remove output file

# define a function to find the prime numbers up to a given number
def find_primes(n):
  # create an empty list to store the prime numbers
  primes = []
  count_prime = 0
  last_prime = 0
  largest_distance = 0
  last_prime_with_largest_distance = 0
  if os.path.exists('./dist_prime.txt'):
    os.remove('./dist_prime.txt')

  # loop through the numbers from 2 to n
  for i in range(2, n+1):
    # assume that the number is prime
    is_prime = True

    # loop through the numbers from 2 to the square root of i
    for j in range(2, int(i ** 0.5) + 1):
      # if the number is divisible by j, it is not prime
      if i % j == 0:
        is_prime = False
        break

    # if the number is prime, add it to the list of primes
    if is_prime:
      distance = i - last_prime
      print("{:10d}".format(i),end="")
      print(", ",end="")
      count_prime+=1
      print(" | Count = ", "{:10d}".format(count_prime), end="")
      print(" | Dist = ", "{:5d}".format(distance), end="")
      if (distance >= largest_distance):
        largest_distance = distance
        with open('dist_prime.txt', 'a') as file:
          file.write('{:10d}'.format(i))
          file.write(' | Count = {:10d}'.format(count_prime))
          file.write(' | Latest Max Dist = {:5d}\n'.format(distance))
        last_prime_with_largest_distance = i
      print(" | Max Dist = ", "{:5d}".format(largest_distance), end="")
      print(" | Prime of Max Dist = ", "{:5d}".format(last_prime_with_largest_distance))
      last_prime = i
      primes.append(i)

  # return the list of primes
  return primes

# create a loop to allow the user to enter multiple maximum numbers
while True:
  # prompt the user to enter the maximum number
  max_num = int(input("Enter the maximum number (0 to quit): "))

  # check if the user entered 0 to quit
  if max_num == 0:
    break

  # find the prime numbers up to the maximum number
  primes = find_primes(max_num)

  # print the list of prime numbers
  print("\n")
  # print(primes)
  print("total number of primes =", len(primes))

# print a message when the program ends
print("Thank you for using the program. Goodbye!")
