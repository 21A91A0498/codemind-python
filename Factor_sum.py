def factors(n):
    cnt=0
    for i in range(1,n+1):
        if n%i==0:
            cnt+=i
    return cnt
n=list(map(int,input().split(",")))
a=[]
for i in n:
    b=i
    if factors(i) in n:
        a.append(b)
a.sort()
if len(a)==0:
    print("-1")
else:
    print(*a)
    
