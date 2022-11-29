def prime(n):
    c=0
    i=1
    while i<=n:
        if n%i==0:
            c+=1
        i+=1
    if c==2:
        return True
n=int(input())
temp=n
rev=0
while n:
    d=n%10
    rev=rev*10+d
    n=n//10
if prime(temp) and prime(rev):
    print("circular prime")
elif prime(temp):
    print("prime but not a circular prime")
else:
    print("not prime")