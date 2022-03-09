#!/usr/local/bin/python3

"""
Description

Find the min capacity of the ship to deliver the packages within D days.

A conveyor belt has packages that must be shipped from one port to another within
D days. The i-th package on the conveyor belt has a weight of weights[i].
Each day, we load the ship with packages on the conveyor belt (** in the order
given by weights **). We may not load more weight than the maximum weight capacity
of the ship. Please return the least weight capacity of the ship that will result
in all the packages on the conveyor belt being shipped within D days.

Input: weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], D = 5

Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Output: 15

"""
"""
Input: weights = [4, 1, 8, 2, 3, 3, 4, 2], D = 3

Explanation: A ship capacity of 15 is the minimum to ship all the packages in 3 days like this:
1st day: 4, 1
2nd day: 8, 2
3rd day: 3, 3, 4, 2

Output = 12
"""
def can_ship(pkg, per_day_weights, D):
    days = 1
    total = 0
    print("per day weights =",per_day_weights)
    for i in pkg:
        total += i
        print("L=",i, " ",end='')
        if total > per_day_weights :
            total = i
            days += 1
            print(" return ")

    if days > D:
        return False

    return True

def print_schedule(pkg, min_weights, D):
    days = 1
    total = 0
    print("day =",days," [ ",end='')
    for i in pkg:
        total += i
        if total > min_weights :
            total = i
            days += 1
            print("]")
            print("day =",days," [ ",end='')
            print(i,' ',end='')
        else:
            print (i,' ',end='')
    print("]")

Ainput_packages = [4, 1, 8, 2, 3, 3, 4, 2]
Dinput_packages = [7, 1, 3, 5, 6, 4, 4, 4, 8, 5, 7, 8, 6, 5, 1, 1, 1, 5] # D = 8   O = 12
Hinput_packages = [7, 1, 3, 5, 6, 4, 4, 9, 8, 10, 7, 8, 9 , 5, 1, 1, 1, 8] # D = 20   O = 10
input_packages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # D = 5  O = 15
Cinput_packages = [3, 2, 2, 4, 1, 4]  # D = 3    O = 6
Finput_packages = [1, 1, 2, 1] # D = 2   O  = 11
Einput_packages = [1, 2, 3, 1, 1]  # D = 4   O = 3
D = 5

max_load = max(input_packages)
print("max=",max_load)
all_load = sum(input_packages)
print("all=",all_load)
low  = max_load
high = all_load
mid = (low + high) // 2
load = 0 #final ship load

# Binary search
while (low <= high):
    result = can_ship(input_packages, mid, D)
    if (result):
        load = mid
        high = mid - 1
        mid = (low + high) // 2
        print("A low=", low, "mid=", mid, "high=", high, "load=", load)
    else:
        low = mid + 1
        mid = (low + high) // 2
        print("B low=", low, "mid=", mid, "high=", high, "Load", load)

print("load=", load)
print_schedule(input_packages, load, D)
