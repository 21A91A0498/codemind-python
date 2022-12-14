t=int(input())
i=1
while i<=t:
    c=0
    n,m=map(int,input().split())
    for j in range(n,m+1):
        d=j%10
        if d==2 or d==3 or d==9:
            c+=1
    if c>0:
        print(c)
    i+=1