import math
def prime(n):
    
    sq=int(math.sqrt(n))
    for i in range(2,sq+1):
        if n%i==0: 
            return False
    return True
            
for i in range(int(input())):
    n=int(input())
    temp=n
    for i in range(n,0,-1):
        if prime(i):
            k=i
            break
    for i in range(n+1,n*n*n):
        if prime(i):
            g=i
            break

    if abs(k-temp)>abs(g-temp):
        print(g)
    elif abs(k-temp)<=abs(g-temp):
        print(k)
    elif abs(k-temp)==abs(g-temp):
        print(k)
    