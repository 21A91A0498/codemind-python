import math 
def prime(n):
    sq=int(math.sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True
n=int(input())
p=n+1
m=n
temp=n
while m<=n:
    if prime(m):
        k=m
        break
    m-=1
while p>n:
    if prime(p):
        h=p
        break
    p+=1
a=abs(k-temp)
b=abs(h-temp)
if a>b:
    print(b)
elif a<=b:
    print(a)