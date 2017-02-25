## Finds the largest palindrome number obtained after multiplying two three digit numbers

def is_palindrome(str):
    if str== reversed(str): return True
    return False

def reverse_int(n):
    return int(str(n)[::-1])

n=10201
for i in range(999, 100, -1):
    for j in range(i,100, -1):
        num=i*j
        #print str(num), reversed(str(num))
        if (num == reverse_int(num)) and (num > n):
            n=num
print n
