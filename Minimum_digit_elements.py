def digicount(n):
    c=0
    while n:
        d=n%10
        c+=1
        n=n//10
    return c
n=int(input())
l=list(map(int,input().split()))
d={}
for i in l:
    k=digicount(i)
    d[i]=k
co=0
for i,j in d.items():
    if j==min(d.values()):
        co+=1
print(co)