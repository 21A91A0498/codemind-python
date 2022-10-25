def neon(n):
    sum=0
    c=n*n
    while c:
        d=c%10
        sum=sum+d
        c=c//10
    if sum==n:
        print("Neon Number")
    else:
        print("Not Neon Number")
n=int(input())
neon(n)