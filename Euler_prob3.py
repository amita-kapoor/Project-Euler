"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import numpy as np

def is_prime(n):
    """Returns True if the number id prime.
    Args:
        Takes the input number
    Returns:
        True if number is prime, and false otherwise"""
    for i in range(2, int(np.sqrt(n))):
        if (n%i == 0):
            return False
    return True

def factors(num):
    """Lists all the possible factors of a number
    Args:
        Takes the input number
    Returns:
        Returns list of the factors"""
    prime = [i for i in range(2, int(np.sqrt(num))) if (num % i == 0 ) and is_prime(i) ]
    return prime
def prime_factors(num):
    prime=[1]
    if num % 2 == 0:
        prime= [2]
    upper=num
    i=3
    while upper != 1:
        if (upper % i == 0 ) and is_prime(i):
            prime.append(i)
            upper= upper // i
        i+=2
    return prime

if __name__ == "__main__":
    num=600851475143
    #num=13195
    print (prime_factors(num) [-1])
    print (factors(num))
    print[i for i in [i for i in range(1, int(num ** .5) + 1) if num % i == 0] if
          all(i % n != 0 for n in range(2, int(i ** .5) + 1))][-1]