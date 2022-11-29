def prime(n):
    c=0
    j=1
    while j<=n:
        if n%j==0:
            c+=1
        j+=1
    if c==2:
        return True
n=int(input())
m=int(input())
a=n+m
i=1
while i:
    b=a+i
    if prime(b):
        print(i)
        break
    i+=1
    