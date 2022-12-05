def unique(n,m):
    t=m
    c=0
    while t:
        d=t%10
        if d==n:
            c+=1
        t=t//10
    if c>=2:
        return False
    else :
        return True
n=int(input())
temp=n
co=0
i=0
while n:
    d=n%10
    i+=1
    if unique(d,temp):
        co+=1
    n=n//10

if co==i:
    print("Unique Number")
else:
    print("Not Unique Number")
    
