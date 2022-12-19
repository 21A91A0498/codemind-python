def digicount(n):
    sum=0
    while n:
        d=n%10
        sum+=1
        n=n//10
    return sum
n=int(input())
a=digicount(n)
b=n*n
rev=0
while a:
    d=b%10
    rev=rev*10+d
    b=b//10
    a-=1
c=int(str(rev)[::-1])
if c==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
