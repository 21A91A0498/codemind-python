import math
def prime(n):
    sq=int(math.sqrt(n))
    if n==1:
        return "not a prime"
    for i in range(2,sq+1):
        if n%i==0:
            return "not a prime"
    return "prime"
n=int(input())
a=prime(n)
print(a)