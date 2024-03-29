# written by OpenAI ChatGPT
import os # for remove output file
import multiprocessing as mp
from multiprocessing import Pool

def check_prime(i):
  is_prime = True
  for j in range(2, int(i**0.5)+1):
    if i % j == 0:
      is_prime = False
      break

  if is_prime:
    print("{:11d}".format(i))
    #with open('dist_prime.txt', 'a') as file:
     #     file.write('{:11d}\n'.format(i))
    return i

# define a function to find the prime numbers up to a given number
def find_primes(n):
  # create an empty list to store the prime numbers
  print("HEY",n)
  primes = []
  count_prime = 0
  last_prime = 0
  largest_distance = 0
  last_prime_with_largest_distance = 0

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

#print("procs=", mp.cpu_count())
# create a loop to allow the user to enter multiple maximum numbers
primes = []
while True:
  # prompt the user to enter the maximum number
  low_num = int(input("Enter the minium number (0 to quit): "))
  max_num = int(input("Enter the maximum number (0 to quit): "))
  # check if the user entered 0 to quit
  if max_num == 0:
    break

  if os.path.exists('./dist_prime.txt'):
    os.remove('./dist_prime.txt')

  numbers = range(low_num, max_num)

  pool = mp.Pool(mp.cpu_count())
  pool.map(check_prime, numbers)
  #primes = pool.map(check_prime, numbers)
  
 # with multiprocessing.Pool() as pool:
    # find the prime numbers up to the maximum number
    #primes = pool.map(find_primes, numbers)

  # print the list of prime numbers
  print("\n")
  #print(primes)
  #print("total number of primes =", len(primes))

# print a message when the program ends
print("Thank you for using the program. Goodbye!")
