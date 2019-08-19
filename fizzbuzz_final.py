#Solution to problem #2

import math

def multiple_of_three(n):
    if (n % 3 == 0):
        return True
    else: return False

def multiple_of_five(n):
    if (n % 5 == 0):
        return True
    else: return False

def fizzbuzz(n):
    count = 100
    i = 1
    while (i <= count):
        if (multiple_of_five(i) == 1 and multiple_of_three(i) == 1):
            print("FizzBuzz")
        elif (multiple_of_five(i) == 1):
            print("Buzz")
        elif (multiple_of_three(i) == 1):
            print("Fizz")
        else: print(i)
        i+=1

n = 100
fizzbuzz(n)
    
    
