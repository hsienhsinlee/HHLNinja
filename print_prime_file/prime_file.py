# written by OpenAI ChatGPT
import os # for remove output file
import math # to use ceil function

# define a function to find the prime numbers up to a given number
def find_primes(start, end):
  # create an empty list to store the prime numbers
  primes = []
  count_prime = 0
  last_prime = start
  largest_distance = 0
  last_prime_with_largest_distance = 0
  is_first_num = False
  #if os.path.exists('./dist_prime.txt'):
  #  os.remove('./dist_prime.txt')
    
  if start <= 2:
    i = 2 # special taking care of 2
    distance = i - last_prime
    print("{:11d}".format(i),end="")
    print(", ",end="")
    count_prime+=1
    print(" | Count = ", "{:11d}".format(count_prime), end="")
    print(" | Dist = ", "{:9d}".format(distance), end="")
    if (distance >= largest_distance):
      largest_distance = distance
      with open('dist_prime.txt', 'a') as file:
        prime_gap = i - last_prime_with_largest_distance
        file.write('{:11d}'.format(i))
        file.write(' | Count = {:11d}'.format(count_prime))
        file.write(' | Latest Max Dist = {:9d}'.format(distance))
        file.write(' | Max-Dist Prime Gap = {:11d}\n'.format(prime_gap))
      last_prime_with_largest_distance = i
    print(" | Max Dist = ", "{:9d}".format(largest_distance), end="")
    print(" | Prime of Max Dist = ", "{:9d}".format(last_prime_with_largest_distance))
    last_prime = i
    primes.append(i)
    start = 3

    # loop through the numbers from 2 to n
  if start % 2 == 0:
    start += 1
  ####################################################################
  
  for i in range(start, end+1, 2):  # ignore 2 here
    # assume that the number is prime
    is_prime = True
    if (i % 2 == 0):
      is_prime = False
      next
    # loop through the numbers from 2 to the square root of i
    for j in range(3, math.ceil(i ** 0.5 + 1), 2):
      #print("j=",j)
      # if the number is divisible by j, it is not prime
      if i % j == 0:
        is_prime = False
        break

    # if the number is prime, add it to the list of primes
    if is_prime:
      distance = i - last_prime
      print("{:11d}".format(i),end="")
      print(", ",end="")
      count_prime+=1
      print(" | Count = ", "{:11d}".format(count_prime), end="")
      print(" | Dist = ", "{:9d}".format(distance), end="")
      if (distance >= largest_distance):
        largest_distance = distance
        with open('dist_prime.txt', 'a') as file:
          prime_gap = i - last_prime_with_largest_distance
          file.write('{:11d}'.format(i))
          file.write(' | Count = {:11d}'.format(count_prime))
          file.write(' | Latest Max Dist = {:9d}'.format(distance))
          file.write(' | Max-Dist Prime Gap = {:11d}\n'.format(prime_gap))
        last_prime_with_largest_distance = i
      print(" | Max Dist = ", "{:9d}".format(largest_distance), end="")
      print(" | Prime of Max Dist = ", "{:9d}".format(last_prime_with_largest_distance))
      last_prime = i
      primes.append(i)

  # return the list of primes
  return primes

# create a loop to allow the user to enter multiple maximum numbers
while True:
  # prompt the user to enter the maximum number
  low_num = int(input("Enter the minimum number: "))
  max_num = int(input("Enter the maximum number (0 to quit): "))

  # check if the user entered 0 to quit
  if max_num == 0:
    break

  # find the prime numbers up to the maximum number
  primes = find_primes(low_num, max_num)

  # print the list of prime numbers
  print("\n")
  # print(primes)
  print("total number of primes =", len(primes))

# print a message when the program ends
print("Thank you for using the program. Goodbye!")
