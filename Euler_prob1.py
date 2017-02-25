def sumofmultipleof3or5(n):
    """Find sum of all the natiural numbers that are multiples of 3 or 5 below n"""
    assert n > 0
    return sum([i for i in range(3,n) if (i%3 == 0) or (i%5 == 0)])

def summultipleof(x,n):
    """Finds sum of all natural numbers that are multiples of x and below n
    Args:
        x the number whose multiples are to be summed and n the largest natural number till we need to search
    Returns:
        The sum of the multiples"""
    assert x > 0
    assert n > 0
    return sum([i for i in range(x,n) if (i%x == 0)])

def non_abundant(n):
    assert n > 0
    s=sum([i for i in range(1,n) if n%i == 0])  # s is sum of all the divisors of n
    if s<=n:
        return  True  # Return 0 is n is a perfect (s==n) or deficient (s<n) number
    return False   # returns the abundant number

def add_int(x):
    add = False
    for a in range(12, x - 12):
        if (non_abundant(a) and non_abundant(x - a)):
            print ("can not be expressed as non abundant for", x)
            add = True
    return add


if __name__ == "__main__":


    print (sum([i for i in range(24,28123) if add_int(i)]))
    print("Sum is", summultipleof(3, 10) + summultipleof(5, 10))
