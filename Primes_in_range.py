import math
def prime(n):
    
    s=int(math.sqrt(n))
    if n==1:
        return False
    for i in range(2,s+1):
        if n%i==0 :
            return False
    return True
n=int(input())
m=int(input())
c=0
for i in range(n,m+1):
    if prime(i):
        c+=1
print(c)