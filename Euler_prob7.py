"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""
import numpy as np

def is_prime(n):
    """Returns True if the number id prime.
    Args:
        Takes the input number
    Returns:
        True if number is prime, and false otherwise"""
    for i in range(2, n/2):
        if (n%i == 0):
            return False
    return True

n=1
num=3
prime = [2]
while n <10001:
    if is_prime(num):
        #print (num, n)
        prime.append(num)
        n+=1
    num+=2
print (prime[-1])

