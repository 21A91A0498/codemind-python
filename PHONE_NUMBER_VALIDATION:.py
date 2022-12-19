def len(n):
    c=0
    while n:
        d=n%10
        c+=1
        n=n//10
    return c
n=int(input())
rev=int(str(n)[::-1])
if len(rev)==10:
    print("Valid")
else:
    print("Invalid")