import math
def isprime(n):
    k=int(math.sqrt(n))
    c=0
    if n==1:
        return 0
    for i in range(2,k+1):
        if n%i==0:
            c+=1
    if c==0:
        return True
    else:
        return False
n=int(input())
l=list(map(int,input().split()))
s=1
sum=1
for i in l:
    if isprime(i):
        s*=i
    else:
        sum*=i
print(abs(sum-s))