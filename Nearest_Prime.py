import math
def prime(n):
    sq=int(math.sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True
t=int(input())
i=0             
while i<t:

    n=int(input())
    p=n+1
    temp=n
    m=n
    while m<=n:
        if prime(m):
            k=m
            break
        m-=1
    while p>n:
        if prime(p):
            g=p
            break
        p+=1
    if abs(k-temp)>abs(g-temp):
        print(g)
    elif abs(k-temp)<abs(g-temp):
        print(k)
    else:
        print(k)
    i+=1